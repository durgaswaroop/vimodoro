let vimodoro_path = escape(expand('<sfile>:p:h'), '\')
let python_file_path = vimodoro_path . '/vimodoro.py'
execute 'py3file ' . python_file_path

function! StartPomodoro()
	python3 start_pomodoro()
endfunction

let timer = timer_start(1000, 'UpdateStatuBar', {'repeat':-1})
function! UpdateStatuBar(timer)
	"execute 'let &ro = &ro'
	"execute 'set statusline +=hello'
	python3 set_status_line()
endfunction

function! GetTimeRemaining()
	python3 get_time_remaining()
endfunction

function! StopPomodoro()
	python3 stop_pomodoro()
endfunction

