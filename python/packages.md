# Package Notes
## Table of contents
- [QtDisigner Install](#qtdisigner-install)
- [Previewing Markdown](#previewing-markdown)
### QtDisigner Install
QtDisigner is convenient, but it doesn't come along with the none GPL version. Then it is for you.
```shell
pip install pyqt5_tools
```
### Previewing Markdown
`grip` is an excellent Flask app and python module to view markdown and easy to use. Just run:
```shell
pip install grip
```
And it installed:
- Flask-1.0.2
- Werkzeug-0.14.1
- certifi-2018.4.16
- chardet-3.0.4
- docopt-0.6.2
- grip-4.5.2
- idna-2.7
- itsdangerous-0.24
- path-and-address-2.0.1
- requests-2.19.1
--------
Since Termux does not have a browser, I wrote the python script below:
```python
from os import popen,system
from time import sleep
import sys
from threading import Thread
def open_xbrowser():
    sleep(2)
    popen('termux-open-url "http://localhost:5555/"')
    return
def start_grip():
    mdfile=sys.argv[1]
    try:
        system('grip '+mdfile+' 5555')
    except KeyboardInterrupt as e:
        pass
    return
if __name__=='__main__':
    Thread(target=open_xbrowser).start()
    start_grip()
```
And alias it as `mkdn` (`md` is the alias of `mkdir`). It is rather convenient.
