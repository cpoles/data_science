# count the seconds since midnight

def seconds_since_midnight(hour, minute, second):
    hour_in_seconds = hour * 60 ** 2
    minute_in_seconds = minute * 60
    return hour_in_seconds + minute_in_seconds + second

secs = seconds_since_midnight(13, 30, 45) # 48645
print(f'Total seconds: {secs}')
