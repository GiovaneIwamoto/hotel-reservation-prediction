from pydantic import BaseModel

class DummyParamsReq(BaseModel):
    no_of_adults: int
    no_of_children: int
    no_of_weekend_nights: int
    no_of_week_nights: int
    required_car_parking_space: int
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_not_canceled: int
    no_of_special_requests: int
    type_of_meal_plan_Meal_Plan_1: bool
    type_of_meal_plan_Meal_Plan_2: bool
    type_of_meal_plan_Meal_Plan_3: bool
    type_of_meal_plan_Not_Selected: bool
    room_type_reserved_Room_Type_1: bool
    room_type_reserved_Room_Type_2: bool
    room_type_reserved_Room_Type_3: bool
    room_type_reserved_Room_Type_4: bool
    room_type_reserved_Room_Type_5: bool
    room_type_reserved_Room_Type_6: bool
    room_type_reserved_Room_Type_7: bool
    market_segment_type_Aviation: bool
    market_segment_type_Complementary: bool
    market_segment_type_Corporate: bool
    market_segment_type_Offline: bool
    market_segment_type_Online: bool
    booking_status_Canceled: bool
    booking_status_Not_Canceled: bool
    