from datetime import datetime, timedelta
import vim

start_time = None
end_time = None

POMODORO_INTERVAL = 20 # minutes

def pomodoro():
    if _is_timer_running():
        _start_pomodoro()
    else:
        _stop_pomodoro()

def _is_timer_running():
    return start_time is None and end_time is None

def _start_pomodoro():
    global start_time, end_time
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=POMODORO_INTERVAL)

def _stop_pomodoro():
    # Reset the times
    global start_time, end_time
    start_time = end_time = None

def get_time_remaining():
    if end_time is None:
        vim.command(f"let full_time = '00:00'")
        return

    current_time = datetime.now()

    if current_time > end_time:
        seconds = 0
    else:
        time_left = end_time - current_time
        seconds = time_left.seconds

    minutes_left = seconds // 60
    seconds_left = seconds % 60
    full_time = str(minutes_left) + ':' + str(seconds_left)
    vim.command(f"let full_time = '{full_time}'")

