# ProgramingNotes
My notes for programing.
## Table of Contents
- [Python](#python)
    - [Read the Character Straight](#read-the-character-straight)
	- [Downloading Binary Package on Windows](#downloading-binary-package-on-windows)
	- [QtDisigner Install](#qtdisigner-install)
    - [Python the Language](#python-the-language)
- [Termux](#termux)
    - [Initial Setup](#initial-setup)
- [Git](#git)
    - [Push without Password in Linux](#push-without-password-in-linux)
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
`pip install pyqt5_tools`
### Python the Language
## Termux
#### Initial Setup
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
