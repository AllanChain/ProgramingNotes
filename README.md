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
## Termux
#### ImportError dlopen failed
I haven't clearly figure out what's happening, but uninstall and reinstall the packege absolutely helps.
## Git
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
