# git-demo

[![Build Status](https://travis-ci.org/cheah/git-demo.svg?branch=master)](https://travis-ci.org/cheah/git-demo)    

This is a simple Python Webapp to demonstrate the usage of Git.

## Prerequisites
We assume that you already have the following prerequisites installed. If not, check out the links for more info:
- [Python 2 / Python 3](https://www.python.org/downloads/)
- [Virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html)

## Usage
The following commands assume that you run it from the root directory of the repository

```bash
# Create and activate virtualenv
~ $ virtualenv hello_git
~ $ . hello_git/bin/activate

# Install requirements for webapp
(hello_git) ~ $ pip install -r hello_git/requirements.txt

# Run the webapp.
(hello_git) ~ $ python hello_git/wsgi.py
```

The webapp will be accessible from http://127.0.0.1:5000
