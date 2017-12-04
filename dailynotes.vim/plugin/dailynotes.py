import vim

from dailynotes.util import get_note_path


def open_note():
    date_expr = vim.eval('g:dailynotes_date_expr')
    note_path = get_note_path(date_expr)
    vim.command("edit {0}".format(note_path))
