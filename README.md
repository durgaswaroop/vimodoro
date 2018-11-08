# vimodoro
Pomodoro Timer for Vim

## Usage
To start/stop the timer, run `:Vimodoro`

To see the time left, `:GetTimeRemaining`.

To add the timer to the statusline, execute `:set statusline +=\ %{GetTimeRemaining()}`

To update the status continuously, run `:call timer_start(1000, {-> execute(':let &stl=&stl')}, {'repeat': -1})` 

