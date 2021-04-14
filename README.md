Daily Notes
===========

An opinionated tool for managing daily notes as Markdown files.

This was inspired by a former colleague at the Chicago Tribune who kept a daily log of things he learned as a developer. It's also inspired by some of the conventions in [bullet journaling](https://bulletjournal.com/), a method I struggle to use in my personal life, but makes sense for work-related notes.

Installation
------------

You can install this package with `pip`:

    pip install git+https://github.com/ghing/dailynotes


If you want this package for the `dailynotes` command-line utility, you might want to use [pipx](https://pipxproject.github.io/).

    pipx install git+https://github.com/ghing/dailynotes

Or, [pipsi](https://github.com/mitsuhiko/pipsi):

    pipsi install git+https://github.com/ghing/dailynotes

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

### Open a notes file for a specific date

```
dailynotes 20180716
```

or

```
dailynotes 2018-07-16
```

Configuration
-------------

Configuration is through environment variables.

### `DAILYNOTES_DIR`

The directory where daily note files will be stored.

Default: `~/Documents/notes/daily`

## Visual Studio code Snippets

If you use Visual Studio Code, there is a snippets JSON file to create items commonly used in these notes. You can find this file in `snippets/markdown.json`.

See the [Code documentation on snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets) for where to paste these snippets.

Here are the prefixes that trigger snippets and what they provide.

- `dn`: Skeleton for a daily notes file
- `todo`: To do item using GitHub Markdown syntax (`* [ ] item`)
- `evt`: An event, such as a meeting

## Vim Plugin

There is also a vim plugin that you can install if that's your text editor of choice.

### Installation

Make sure you've installed the CLI first, per the instructions above.

Make sure that the dependencies are installed in the version of Python used by vim.

You can get a sense of vim's Python by running `vim --version`.

Then run the appropriate version of `pip install dailynotes` for that version of Python.

I use [Vundle](https://github.com/VundleVim/Vundle.vim) to manage my plugins, so I just had the add the following line to my `.vimrc`:

    Plugin 'ghing/dailynotes', {'rtp': 'dailynotes.vim/'}

and then I ran the `PluginInstall` command in vim.

### Usage

The vim plugin provides a `DailyNotes` command that accepts the same arguments as the CLI.

### Troubleshooting

The vim plugin will use the version of Python with which vim was compiled rather than one in a virtualenv if you install the dailynotes CLI using something like pipsi.  You can see the Python version used by vim by running `vim --version`.

If you run into errors because the plugin can't find a dependency of the dailynotes package, such as Jinja2, you might hae to install that explicitely using the systemwide pip:

```
pip install Jinja2
```
