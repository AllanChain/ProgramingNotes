# Standard Library
In this section, some of python standard library and the magic operation are introduced
## Table of Contents
- [Read the Character Straight](#read-the-character-straight)
- [Module readline](#module-readline)

### Read the Character Straight
#### On Linux
```python
import  os
import  sys
import  tty, termios
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
try :
   tty.setraw( fd )
   ch = sys.stdin.read( 1 )
finally :

   termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
```
#### On Windows
```python
import  msvcrt
ch = msvcrt.getch()
```

### Module readline
Here is my simple script on readline.

```python
import readline
import os

def completer(text,state):
    ds=os.listdir()
    rs=list(filter(lambda s:s.startswith(text),ds))
    if state<len(rs):
        return rs[state]
    return None
readline.parse_and_bind("tab: complete")
readline.set_completer(completer)
input()
```

必须注意如果在函数中有错误的话，在你按下tab键后什么都不会发生（新手会在这里卡壳。`readline`非常高级地封装了你的函数，但这对debug来说不见得是一件好事。较好的方法是先调用一下你的函数`completer('c',0)`并检查输出。
Expecially notice that if there's any exception raised in your script, nothing would happen when you pressed <tab>.The best way I thought of is to call `completer('c',0)` first and check the return value when debugging.
