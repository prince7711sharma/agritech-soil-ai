def classify_soil_fertility(n, p, k, ph):
    score = 0

    if n > 280:
        score += 1
    if p > 22:
        score += 1
    if k > 140:
        score += 1
    if 6.0 <= ph <= 7.5:
        score += 1

    if score <= 1:
        return "Low"
    elif score <= 3:
        return "Medium"
    else:
        return "High"
