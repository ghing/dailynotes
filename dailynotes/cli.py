import argparse
import os
import os.path

from dailynotes.util import get_date, get_note_path


def get_date_heading(date_expr):
    d = get_date(date_expr)
    return d.strftime("# %A, %B %-d, %Y")


def main():
    """Open a daily notes file for editing"""
    description = "Open a daily notes file in your text editor"
    parser = argparse.ArgumentParser(description=description)
    date_expr_help = (
        "Show notes for this day. Examples: 'yesterday', 'tomorrow', 'monday'"
    )
    parser.add_argument('date_expr', nargs='?', default='',
                        help=date_expr_help)
    args = parser.parse_args()

    note_path = get_note_path(args.date_expr)
    # TODO: initialize note from template
    if not os.path.isfile(note_path):
        with open(note_path, 'w') as f:
            f.write("{0}\n".format(get_date_heading(args.date_expr)))

    cmd = "{0} {1}".format(os.environ.get('EDITOR'), note_path)
    os.system(cmd)
