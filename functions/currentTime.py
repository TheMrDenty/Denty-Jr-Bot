from datetime import date

today = date.today()

def year():
    current_year = today.strftime("%Y") 
    return current_year

def month():
    current_month = today.strftime("%m") 
    return current_month

def day():
    current_day = today.strftime("%d") 
    return current_day

def hour():
    current_hour = today.strftime("%H") 
    return current_hour

def minute():
    current_minute = today.strftime("%M") 
    return current_minute