# foobar-with-google

[![Build Status](https://travis-ci.com/mike-stephens/foobar-with-google.svg?branch=master)](https://travis-ci.com/mike-stephens/foobar-with-google)

Problems from https://foobar.withgoogle.com/


How can I get invited?
https://www.google.com/search?q=unlock+foobar+with+google

## Getting Started

1. Clone this repository.

2. Get virtualenv if you don't already have it.

```
$ pip install virtualenv
```

3. Create a new virtual environment in your local directory.

```
$ virtualenv env
```

4. Activate the virtual environment.

```
$ source env/bin/activate
```

5. Install dependencies via pip & requirements.txt.
```
$ pip install -r requirements.txt
```

6. When finished, deactivate the virtual environment.

```
$ deactivate
```

## Solution Constraints

Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.