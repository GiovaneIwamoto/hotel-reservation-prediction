# Install dependencies
# pip install -r requirements.txt

# Run server
# uvicorn main:app --reload

import numpy as np
import pickle
import xgboost as xgb
import boto3
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from botocore.exceptions import NoCredentialsError, ClientError

from classes.dummy_params import DummyParamsReq
from classes.user_params import UserParamsReq
from services.service_dynamo_log import create_dynamodb_table
from services.service_dynamo_log import log_inference_result
from services.service_s3_bucket import save_model_from_s3
from services.service_map_values import map_categorical_values

# Service save model from S3
save_model_from_s3()

# Load XGBoost model from model folder
with open('./models/xgboost-model', 'rb') as model_file:
    model = pickle.load(model_file)
    
feature_names = model.feature_names

# Service DynamoDB create table
table_name = os.environ.get('DYNAMODB_TABLE_NAME')
create_dynamodb_table(table_name)    

# Launch API
app = FastAPI()

# Post route
@app.post("/api/v1/predict")
def predict(request: UserParamsReq):
    user_params = UserParamsReq(**request.dict())

    # Map User params to Dummy params format
    dummy_params = DummyParamsReq(
        no_of_adults=user_params.no_of_adults,
        no_of_children=user_params.no_of_children,
        no_of_weekend_nights=user_params.no_of_weekend_nights,
        no_of_week_nights=user_params.no_of_week_nights,
        required_car_parking_space=user_params.required_car_parking_space,
        lead_time=user_params.lead_time,
        arrival_year=user_params.arrival_year,
        arrival_month=user_params.arrival_month,
        arrival_date=user_params.arrival_date,
        repeated_guest=user_params.repeated_guest,
        no_of_previous_cancellations=user_params.no_of_previous_cancellations,
        no_of_previous_bookings_not_canceled=user_params.no_of_previous_bookings_not_canceled,
        no_of_special_requests=user_params.no_of_special_requests,
        type_of_meal_plan_Meal_Plan_1=user_params.type_of_meal_plan == "1",
        type_of_meal_plan_Meal_Plan_2=user_params.type_of_meal_plan == "2",
        type_of_meal_plan_Meal_Plan_3=user_params.type_of_meal_plan == "3",
        type_of_meal_plan_Not_Selected=user_params.type_of_meal_plan == "Not Selected",
        room_type_reserved_Room_Type_1=user_params.room_type_reserved == "1",
        room_type_reserved_Room_Type_2=user_params.room_type_reserved == "2",
        room_type_reserved_Room_Type_3=user_params.room_type_reserved == "3",
        room_type_reserved_Room_Type_4=user_params.room_type_reserved == "4",
        room_type_reserved_Room_Type_5=user_params.room_type_reserved == "5",
        room_type_reserved_Room_Type_6=user_params.room_type_reserved == "6",
        room_type_reserved_Room_Type_7=user_params.room_type_reserved == "7",
        market_segment_type_Online=user_params.market_segment_type == "Online",
        market_segment_type_Offline=user_params.market_segment_type == "Offline",
        market_segment_type_Corporate=user_params.market_segment_type == "Corporate",
        market_segment_type_Complementary=user_params.market_segment_type == "Complementary",
        market_segment_type_Aviation=user_params.market_segment_type == "Aviation",
        booking_status_Canceled=user_params.booking_status_Canceled == "Yes",
        booking_status_Not_Canceled=user_params.booking_status_Canceled == "No"
    )
    
    # Inference
    input_data = np.array([[value for value in dummy_params.dict().values()]])
    dmatrix = xgb.DMatrix(input_data, feature_names=feature_names)
    prediction = model.predict(dmatrix)
    
    # Determine the class with the highest probability
    predicted_class = int(np.argmax(prediction, axis=1)[0] + 1)  
    
    # Save inference result to DynamoDB
    inference_params = user_params.dict()
    result = {"result": predicted_class}
    log_inference_result(inference_params, result)
   
    return {"result": predicted_class}