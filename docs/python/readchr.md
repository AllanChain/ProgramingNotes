# Read the Character Straight
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
