from datetime import datetime


#def convert_to_unix_time(day:int, month:int, year:int, hour:int, minute:int, timezone:str):
def convert_to_unix_time(day:int, month:int, year:int, hour:int, minute:int):
        #from_date = f"{year}-{month}-{day} {hour}:{minute}:00 {timezone}"
        from_date = f"{year}-{month}-{day} {hour}:{minute}:00"
        #print(from_date)
        #time1 = int(datetime.strptime(from_date, "%Y-%m-%d %H:%M:%S $Z").timestamp())
        time1 = int(datetime.strptime(from_date, "%Y-%m-%d %H:%M:%S").timestamp())
        #time1 = int(time.time())
        #print(time1)
        return f'<t:{time1}:F>'