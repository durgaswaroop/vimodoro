let vimodoro_path = escape(expand('<sfile>:p:h'), '\')
let python_file_path = vimodoro_path . '/vimodoro.py'
execute 'py3file ' . python_file_path

function! Vimodoro()
	python3 vimodoro()
endfunction

function! GetTimeRemaining()
	python3 get_time_remaining()
	return full_time
endfunction

