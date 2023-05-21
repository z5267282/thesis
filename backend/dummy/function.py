def get_hours(seconds):
    minutes = seconds // 60
    return minutes // 60

clock = 10800
hours = get_hours(10800)
print(hours)
