def nutrient_status(n, p, k, ph):
    return {
        "Nitrogen": "Low" if n < 280 else "Adequate",
        "Phosphorus": "Low" if p < 22 else "Adequate",
        "Potassium": "Low" if k < 140 else "Adequate",
        "pH Status": "Acidic" if ph < 6 else "Alkaline" if ph > 7.5 else "Neutral"
    }
