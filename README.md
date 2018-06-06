hotpie
======

[![Build Status](https://secure.travis-ci.org/gingerlime/hotpie.png?branch=master)](http://travis-ci.org/gingerlime/hotpie)
[![PyPI](https://img.shields.io/pypi/v/hotpie.svg)](https://pypi.python.org/pypi/hotpie)

[read more](http://blog.gingerlime.com/2010/once-upon-a-time/)

OATH HOTP/TOTP implementation in python

based on http://tools.ietf.org/html/rfc4226
         http://tools.ietf.org/html/rfc6238

parameter and function names kept inline with the rfc
(e.g. hotp, truncate, k, c etc)

also including a simple unit test based on test vectors in the RFC

usage
=====

```bash
pip install hotpie
```

```python
from hotpie import HOTP, TOTP

key = 'secret'
HOTP(key, 0)             # '814628'
HOTP(key, 0, digits=8)   # '31814628'
HOTP(key, 13, digits=8)  # '81315566'
TOTP(key, digits=6)      # <time-based-value>

# you can also use different hash implementations by passing `digestmod`
# (RFC4226 only specifies SHA-1,
#  but RFC6238 explicitly mentions SHA-256 and SHA-512)
from hashlib import sha512, sha256

HOTP(key, 0, digits=8, digestmod=sha512)
TOTP(key, digits=8, digestmod=sha256)
```

tests
=====

To run the tests, simply run `python ./hotpie.py`
