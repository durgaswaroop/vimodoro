from datetime import datetime, timedelta

import vim


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
    if end_time is None:
        return ""

    current_time = datetime.now()
    time_left = end_time - current_time
    seconds = time_left.seconds
    minutes_left = seconds // 60
    seconds_left = seconds % 60
    #print(str(minutes_left) + ':' + str(seconds_left))
    return str(minutes_left) + ':' + str(seconds_left)

def set_status_line():
    time_remaining = get_time_remaining()
    #vim.command(f"let tr = {time_remaining}")
    if time_remaining:
        vim.command("set statusline +=\ " + get_time_remaining())
