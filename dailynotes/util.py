from datetime import date, datetime, timedelta
import os
import os.path


DEFAULT_DAILYNOTES_DIR = os.path.join(
    os.path.expanduser('~'),
    'Documents',
    'notes',
    'daily'
)
DAILYNOTES_DIR = os.environ.get('DAILYNOTES_DIR', DEFAULT_DAILYNOTES_DIR)
DAY_NAME_TO_NUMBER = {
    'sunday': 6,
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
}


def get_days_delta(date_expr, base_date):
    if date_expr == 'yesterday':
        return -1

    if date_expr == 'tomorrow':
        return 1

    if date_expr in DAY_NAME_TO_NUMBER:
        # We assume we mean the previous day of the week
        diff = base_date.weekday() - DAY_NAME_TO_NUMBER[date_expr]
        if diff > 0:
            step_back = -1 * diff
        else:
            step_back = -7 - diff

        return step_back

    return 0


def get_date(date_expr, base_date=None):
    # First, try to parse the date expression as an explict date specified in
    # either `YYYY-MM-DD` or `YYYYMMDD` formats.
    try:
        dt = datetime.strptime(date_expr, '%Y-%m-%d')
        return dt.date()

    except ValueError:
        pass

    try:
        dt = datetime.strptime(date_expr, '%Y%m%d')
        return dt.date()

    except ValueError:
        pass

    if base_date is None:
        base_date = date.today()

    days_delta = get_days_delta(date_expr, base_date)
    return base_date + timedelta(days=days_delta)


def get_note_path(date_expr, base_date=None,
                  notes_dir=DAILYNOTES_DIR):
    if base_date is None:
        base_date = date.today()

    d = get_date(date_expr, base_date)
    filename = d.strftime('%Y%m%d.md')
    return os.path.join(notes_dir, filename)


def get_date_heading(date_expr, base_date=None):
    if base_date is None:
        base_date = date.today()


    d = get_date(date_expr, base_date)
    return d.strftime("# %A, %B %-d, %Y")


def initialize_note(date_expr, base_date=None):
    if base_date is None:
        base_date = date.today()

    note_path = get_note_path(date_expr, base_date)
    # TODO: initialize note from template
    if not os.path.isfile(note_path):
        with open(note_path, 'w') as f:
            f.write("{0}\n".format(get_date_heading(date_expr, base_date)))

    return note_path
