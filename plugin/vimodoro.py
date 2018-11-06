from datetime import datetime, timedelta


start_time = None
end_time = None

POMODORO_INTERVAL = 20 # minutes


def start_pomodoro():
    global start_time, end_time

    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=POMODORO_INTERVAL)


def stop_pomodoro():
    global start_time, end_time
    start_time = end_time = None


def get_time_remaining():
    current_time = datetime.now()
    time_left = end_time - current_time
    seconds = time_left.seconds
    minutes_left = seconds // 60
    seconds_left = seconds % 60
    return str(minutes_left) + ':' + str(seconds_left)

