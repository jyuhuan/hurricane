[![Build Status](https://travis-ci.org/jyuhuan/hurricane.svg?branch=master)](https://travis-ci.org/jyuhuan/hurricane)

# Hurricane

__Hurricane__ is an extension package for [Tornado](https://github.com/tornadoweb/tornado).


## Highlights

Suppose we have a function that returns a Future such as

```py
@gen.coroutine
def sample_str():
    raise gen.Return('hello')
```

The following are possible with Hurricane but not with the original Tornado:

```py
import hurricane.future_extensions

uppercased = sample_str().map(lambda s: s.upper())

# TODO: Add more higher-order functions (such as flat_map)
```