from datetime import datetime

def current_time():
    time_str = str(datetime.now().time())
    return int(time_str[:2]), int(time_str[3:5])

def task():
    hr, minute = current_time()
    print("Current time: ", hr, ":", minute)
    if 22 <= hr <= 23 or 0 <= hr < 6:
        print("Have to Sleep")
    elif 6 <= hr < 7:
        print("Fresh Up")
    elif hr == 7 and  0<= minute <= 15:
        print("To Do Plan")
    elif 8 <= hr < 9:
        print("Prepare for college")
    elif 12 <= hr < 12 and 15 <= minute < 60:
        print("Lunch")
    elif 9 <= hr < 15:
        print("College classes")
    elif 15 <= hr < 17:
        print("Study or complete assignments")
    elif 17 <= hr < 19:
        print("Play or relax time")
    elif 19 <= hr < 20:
        print("Dinner")
    elif 20 <= hr < 22:
        print("Study")
    else:
        print("Prepare for bedtime")

task()