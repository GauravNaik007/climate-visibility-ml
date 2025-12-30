# risk_logic.py
# Convert visibility value into risk & advisory

def get_risk_and_advisory(visibility):
    if visibility < 1:
        return "HIGH", "Fog likely. Delay spraying and field work."
    elif visibility < 3:
        return "MODERATE", "Light fog possible. Take precautions."
    else:
        return "SAFE", "Clear conditions. Normal operations can continue."
