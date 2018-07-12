# ProgramingNotes
My notes for programing.
## Table of Contents
- [Python](#python)
    - [Python the Language](#python-the-language)
- [Termux](#termux)
    - [Initial Setup](#initial-setup)
- [Git](#git)
    - [Push without Password in Linux](#push-without-password-in-linux)
## Python
### Python the Language
## Termux
### Initial Setup
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
### Push without Password in Linux
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
