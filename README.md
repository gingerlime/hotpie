hotpie
======

OATH HOTP/TOTP implementation in python

based on http://tools.ietf.org/html/rfc4226

parameter and function names kept inline with the rfc
(e.g. hotp, truncate, k, c etc)

also including a simple unit test based on test vectors in the RFC

usage
=====

```python
from hotpie import HOTP, TOTP

key = 'secret'
HOTP(key, 0)             # '814628'
HOTP(key, 0, digits=8)   # '31814628'
HOTP(key, 13, digits=8)  # '81315566'
TOTP(key, digits=6)      # <time-based-value>
```

tests
=====

To run the tests, simply run `python ./hotpie.py`
