Daily Notes
===========

An opinionated tool for managing daily notes as Markdown files.

Installation
------------

You can install this package with `pip`:

    pip install git+https://github.com/ghing/dailynotes


Usage
-----

### Open a notes file for today's notes

```
dailynotes
```

### Open a notes file for yesterday's notes

```
dailynotes yesterday
```

### Open a notes file for tomorrow's notes

```
dailynotes tomorrow
```

### Open a notes file for last Friday's notes

```
dailynotes friday
```

Configuration
-------------

Configuration is through environment variables.

### `DAILYNOTES_DIR`

The directory where daily note files will be stored.

Default: `~/Documents/notes/daily`
