"<sfile> gives the file path of the plugin. :p gets the full path
"and :h gets the head (parent) With escape, we are replacing \ with \\
let vimodoro_path = escape(expand('<sfile>:p:h'), '\')

" Once vimodoro_path has the plugin's directory, we can get the vimodoro.py's
" file path
let python_file_path = vimodoro_path . '/vimodoro.py'

" Run the python file
execute 'py3file ' . python_file_path

function! Vimodoro()
	python3 vimodoro()
endfunction

function! GetTimeRemaining()
	python3 get_time_remaining()
	return full_time
endfunction

