from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hi", "hello", "sup"):
        return "hey! adil is not here i am lara wanna play with me"

    if user_message in ("adil", "aadil", "your crush"):
        return "HE is busy in her schedule. you can tell me i inform her"
    if user_message in ("bsdk", "madharchod", "bkl", "behanchod", "cgutiya", "gaandu"):
        return "Adil baap ke bina gaali mat bak aane de use"

    if user_message in ("time", "time?", "waqt"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return f"chal ab time dekh {str(date_time)}. haa dekh liya na time ab bhaag"
    return "I don't understand"
