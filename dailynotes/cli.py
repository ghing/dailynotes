import argparse
import os
import os.path

from dailynotes.util import initialize_note


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
    note_path = initialize_note(args.date_expr)

    cmd = "{0} {1}".format(os.environ.get('EDITOR'), note_path)
    os.system(cmd)
