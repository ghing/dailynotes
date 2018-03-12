if !has('python') && !has('python3')
   finish
endif

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

exe (has('python3') ? 'py3file' : 'pyfile') . escape(s:plugin_path, ' ') . '/dailynotes.py'

function! s:DailyNotesOpen(...)
        let g:dailynotes_date_expr = a:1
        python open_note()
endfunction

command! -nargs=? DailyNotes call s:DailyNotesOpen(<q-args>)
