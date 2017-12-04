if !has('python')
        finish
endif

function! DailyNotes()
        pyfile dailynotes.py
endfunc

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

exe 'pyfile ' . escape(s:plugin_path, ' ') . '/dailynotes.py'

function! s:DailyNotesOpen(...)
        let g:dailynotes_date_expr = a:1
        python open_note()
endfunction

command! -nargs=? DailyNotes call s:DailyNotesOpen(<q-args>)
