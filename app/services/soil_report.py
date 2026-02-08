def build_soil_report(input_data, fertility, nutrients):
    return {
        "soil_fertility": fertility,
        "nutrient_status": nutrients,
        "input_summary": {
            "Nitrogen": input_data.nitrogen,
            "Phosphorus": input_data.phosphorus,
            "Potassium": input_data.potassium,
            "pH": input_data.ph,
            "Organic Carbon": input_data.organic_carbon
        }
    }
