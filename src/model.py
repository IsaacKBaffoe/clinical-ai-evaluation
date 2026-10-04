# Modelcode
def predict_risk(age, heart_rate):
    """
    Simple demonstration model.

    This is NOT a clinical model.
    It is only for learning Git and ML project structure.
    """

    if age > 65 and heart_rate > 100:
        return "higher_risk"

    return "lower_risk"


if __name__ == "__main__":
    result = predict_risk(age=70, heart_rate=110)
    print("Predicted risk:", result)


def is_high_risk(score):
    # Return True when the risk score is high
    return score >= 0.7

