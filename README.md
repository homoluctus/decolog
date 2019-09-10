# DecoLog
Sample for Python logging decorator<br>

Python version 3.7

# Usage
Please add `@log(logger)` before a function that you want to get logging.<br>

```
from log import log, get_logger


logger = get_logger()

@log(logger)
def sample():
    pass
```

# Example
When main.py is executed, the log is displayed.

```
$ python main.py

[2019-09-11 04:49:48,719] INFO  main.py - main:23 -> [START] main
[2019-09-11 04:49:48,719] INFO  main.py - main:18 -> Hello world
[2019-09-11 04:49:48,719] ERROR main.py - main:23 -> Error!!!!
Traceback (most recent call last):
  File "~/test/log.py", line 90, in wrapper
    return func(*args, **kwargs)
  File "main.py", line 19, in main
    return raise_error()
  File "main.py", line 8, in raise_error
    raise Exception('Error!!!!')
Exception: Error!!!!
[2019-09-11 04:49:48,720] ERROR main.py - main:23 -> [KILLED] main
```