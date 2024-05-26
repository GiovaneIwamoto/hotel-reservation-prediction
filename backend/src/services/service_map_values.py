def map_categorical_values(request):
    meal_plan_mapping = {
        "1": False,
        "2": False,
        "3": False,
        "Not Selected": False
    }
    meal_plan_mapping[request.type_of_meal_plan] = True

    room_type_mapping = {
        "1": False,
        "2": False,
        "3": False,
        "4": False,
        "5": False,
        "6": False,
        "7": False
    }
    room_type_mapping[request.room_type_reserved] = True

    market_segment_mapping = {
        "Aviation": False,
        "Complementary": False,
        "Corporate": False,
        "Offline": False,
        "Online": False
    }
    market_segment_mapping[request.market_segment_type] = True
        
    booking_status_mapping = {
        "Yes" : False,
        "No" : False
    }
    booking_status_mapping[request.booking_status_Canceled] = True
    
    setattr(request, "type_of_meal_plan_Meal_Plan_1", meal_plan_mapping["1"])
    setattr(request, "type_of_meal_plan_Meal_Plan_2", meal_plan_mapping["2"])
    setattr(request, "type_of_meal_plan_Meal_Plan_3", meal_plan_mapping["3"])
    setattr(request, "type_of_meal_plan_Not_Selected", meal_plan_mapping["Not Selected"])

    setattr(request, "room_type_reserved_Room_Type_1", room_type_mapping["1"])
    setattr(request, "room_type_reserved_Room_Type_2", room_type_mapping["2"])
    setattr(request, "room_type_reserved_Room_Type_3", room_type_mapping["3"])
    setattr(request, "room_type_reserved_Room_Type_4", room_type_mapping["4"])
    setattr(request, "room_type_reserved_Room_Type_5", room_type_mapping["5"])
    setattr(request, "room_type_reserved_Room_Type_6", room_type_mapping["6"])
    setattr(request, "room_type_reserved_Room_Type_7", room_type_mapping["7"])

    setattr(request, "market_segment_type_Aviation", market_segment_mapping["Aviation"])
    setattr(request, "market_segment_type_Complementary", market_segment_mapping["Complementary"])
    setattr(request, "market_segment_type_Corporate", market_segment_mapping["Corporate"])
    setattr(request, "market_segment_type_Offline", market_segment_mapping["Offline"])
    setattr(request, "market_segment_type_Online", market_segment_mapping["Online"])
    
    setattr(request, "booking_status_Canceled", booking_status_mapping["Yes"])
    setattr(request, "booking_status_Not_Canceled", booking_status_mapping["No"])