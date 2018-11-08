let vimodoro_path = escape(expand('<sfile>:p:h'), '\')
let python_file_path = vimodoro_path . '/vimodoro.py'
execute 'py3file ' . python_file_path

function! StartPomodoro()
	python3 start_pomodoro()
endfunction

"let timer = timer_start(1000, 'GetTimeRemaining', {'repeat':-1})
function! UpdateStatuBar()
	"execute 'let &ro = &ro'
	"execute 'set statusline +=hello'
	python3 set_status_line()
endfunction

function! GetTimeRemaining()
	let m = 'hello'
	python3 get_time_remaining()
	"let time = execute 'python3' get_time_remaining()
	"echom time
	"echom full_time
	return full_time
endfunction

function! StopPomodoro()
	python3 stop_pomodoro()
endfunction

command! VGTR call GetTimeRemaining()
