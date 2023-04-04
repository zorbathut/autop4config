[![Language: Python](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This tool generates p4config files for you automatically, by listing all the Perforce workspaces you own and generating files on the fly.

* Make sure you have the P4CONFIG environment variable set (traditionally, to .p4config)
* Copy `autop4config.conf.example` to `autop4config.conf` and fill it out
* Install Python (3.7 or later) and Python Poetry (I don't know what version is needed, "latest" is probably a good idea)
* `poetry install`
* `poetry run python autop4config.py`
* Enter your password at the prompt

Yay!

----

At the moment this was written by me for me, without any real expectation that someone else would want to use it. You're welcome to use it. If you want a cleaner setup, like a standalone package you can download and run with a GUI or something, let me know. I'm not adverse to doing it, I just don't want to put the time in unless someone else cares.

This was mostly generated with ChatGPT.
