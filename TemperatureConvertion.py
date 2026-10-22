import json

def lambda_handler(event, context):
    temp = event.get("temp", "")
    unit = event.get("unit", "")

    if unit == "c":
        temp = (temp * 9/5) + 32
        return f"{temp}C"
    elif unit == "f":
        temp = (temp - 32) * 5/9
        return f"{temp}F"

    else:
        return "Invalid Unit use C or F"
