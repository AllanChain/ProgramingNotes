# Annoying Tab width

When using `vim` on `termux`, only in `python` file did `vim` use 4-space-width tab.
And in other files(e.g. `.html`), a tab, a `>>` and a backspace are all 8 spaces.

And I tried to set the following in `~/.vimrc` file. But it does not work.
```vim
set autoindent
set smartindent
set tabstop=4 " 统一缩进为4
set shiftwidth=4 "自动缩进长度
set expandtab " Tab转空格
set softtabstop=4
```
After Googling for a while, I found that it is said that there are some file specific settings which affects the setting in `~/.vimrc` file.

> Discussion on StackOverflow:
> <https://stackoverflow.com/questions/14173766/vim-ignores-shiftwidth-specified-in-vimrc>

> And the struct of vim plugin:
> <http://learnvimscriptthehardway.stevelosh.com/chapters/42.html#vimplugin>

Finally, I wrote the config above to `~/.vim/after/settab.vim`. And problem solved!
