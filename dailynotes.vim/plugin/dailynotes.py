import vim

try:
    from dailynotes.util import get_note_path

except ModuleNotFoundError:
    # Couldn't find dailynotes.util.
    # This is likely because of issues with multiple versions of Python.
    # If it's not already on our path, point it up a few directories, which is
    # where the Python package will also live.
    import os.path
    import sys

    path = os.path.abspath(os.path.join(
        os.path.dirname(vim.eval('expand(\"<sfile>\")')),
        '..',
        '..'
    ))
    sys.path.append(path)
    from dailynotes.util import get_note_path


def open_note():
    date_expr = vim.eval('g:dailynotes_date_expr')
    note_path = get_note_path(date_expr)
    vim.command("edit {0}".format(note_path))
