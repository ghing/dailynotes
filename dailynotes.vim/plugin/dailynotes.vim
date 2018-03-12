if !has('python') && !has('python3')
   finish
endif

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
let s:pyfile_cmd = (has('python3') ? 'py3file' : 'pyfile')
let s:python_cmd = (has('python3') ? 'py3' : 'python')

exe s:pyfile_cmd . escape(s:plugin_path, ' ') . '/dailynotes.py'


function! s:DailyNotesOpen(...)
        let g:dailynotes_date_expr = a:1
        exe s:python_cmd . ' open_note()'
endfunction

command! -nargs=? DailyNotes call s:DailyNotesOpen(<q-args>)
