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

Vim Plugin
----------

There is also a vim plugin that you can install if that's your text editor of choice.

### Installation

Make sure you've installed the CLI first, per the instructions above.

I use [Vundle](https://github.com/VundleVim/Vundle.vim) to manage my plugins, so I just had the add the following line to my `.vimrc`:

    Plugin 'ghing/dailynotes', {'rtp': 'dailynotes.vim/'}

and then I ran the `PluginInstall` command in vim.

### Usage

The vim plugin provides a `DailyNotes` command that accepts the same arguments as the CLI.
