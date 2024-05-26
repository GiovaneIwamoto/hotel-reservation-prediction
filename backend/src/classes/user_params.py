from pydantic import BaseModel

class UserParamsReq(BaseModel):
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
    type_of_meal_plan: str # 1 | 2 | 3 | Not Selected
    room_type_reserved: str # 1 | 2 | 3 | 4 | 5 | 6 | 7
    market_segment_type: str # Online | Offline | Corporate | Complementary | Aviation
    booking_status_Canceled: str # Yes | No