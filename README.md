# ProgramingNotes
My notes for programing.
## Table of Contents
- [Python](#python)
    - [Read the Character Straight](#read-the-character-straight)
	- [Downloading Binary Package on Windows](#downloading-binary-package-on-windows)
	- [QtDisigner Install](#qtdisigner-install)
    - [Previewing Markdown](#previewing-markdown)
    - [Python the Language](#python-the-language)
- [Termux](#termux)
    - [Initial Setup](#initial-setup)
	- [ImportError dlopen failed](#importerror-dlopen-failed)
- [Git](#git)
    - [Push without Password in Linux](#push-without-password-in-linux)
	- [Add SSH Keys](#add-ssh-keys)
## Python
#### Read the Character Straight
##### On Linux
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
##### On Windows
```python
import  msvcrt
ch = msvcrt.getch()
```
#### Downloading Binary Package on Windows
Copied from StackOverflow
> As the other responses pointed out, one solution is to install Visual Studio 2015. However, it takes a few GBs of disk space. One way around is to install precompiled binaries. 
> 
> The webpage [http://www.lfd.uci.edu/~gohlke/pythonlibs](http://www.lfd.uci.edu/~gohlke/pythonlibs) contains precompiled binaries for many Python packages.
#### QtDisigner Install
QtDisigner is convenient, but it doesn't come along with the none GPL version. Then it is for you.
```shell
pip install pyqt5_tools
```
#### Previewing Markdown
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
### Python the Language
Visit [`LanguagePython.md`](https://github.com/AllanChain/ProgramingNotes/blob/master/LanguagePython.md)
## Termux
#### Initial Setup
- First,run:
```shell
termux-setup-storage
ln -s ~/storage/shared/123/pythonPro
```
- Then, in directory `pythonPro`,run `sh setup.sh`. 
- And the content of `setup.sh` is as followed:
```shell
apt install clang python python-dev fftw libzmq libzmq-dev freetype freetype-dev libpng libpng-dev pkg-config curl vim-python zsh
curl -L https://its-pointless.github.io/setup-pointless-repo.sh | sh
pkg install numpy
pip install matplotlib
pip install jupyter
sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"
ln -s /data/data/com.termux/files/usr/lib/python3.6/site-packages
ln -s ~/storage/shared/qpython
ln -s ~/storage/shared/123/cppPro
cp ~/pythonPro/jupyter_notebook_config.py ~/.jupyter/
```
#### ImportError dlopen failed
I haven't clearly figure out what's happening, but uninstall and reinstall the packege absolutely helps.
## Git
#### Push without Password in Linux
- First
```shell
cd ~
touch .git-credentials
vim .git-credentials
```
- Then type:
`https://{username}:{password}@github.com`
- Finally:
```shell
git config --global credential.helper store
```
- And you will see `[credential]helper = store` in `.gitconfig`
#### Add SSH Keys
- Open Terminal.
- Paste the text below, substituting in your GitHub email address.
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
- This creates a new ssh key, using the provided email as a label.
```
Generating public/private rsa key pair.
```
- When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
```
 Enter a file in which to save the key (/home/you/.ssh/id_rsa): [Press enter]
 ```
- At the prompt, type a secure passphrase. For more information, see "Working with SSH key passphrases".
```
 Enter passphrase (empty for no passphrase): [Type a passphrase]
 Enter same passphrase again: [Type passphrase again]
 ```
