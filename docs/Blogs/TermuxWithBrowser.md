# 让Termux对浏览器更友好
Download [xb.py](xb.py)

难点：

- 获取jupyter等应用的实时输出
```python
import subprocess
backup = subprocess.Popen(
	cmd.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in iter(backup.stdout.readline, b''):
	line = line.rstrip().decode('utf8')
```
- 使Ctrl+C能使让应用结束
    - 只有以`shell=False`启动的`Popen`才能收到中止信号，不要问我为什么。
```python
try:
    do_something()
except KeyboardInterrupt:
    from os import _exit
    
    print('Quiting')
    backup.kill()
    _exit(0)
```
- 能自动识别使用什么应用
```python
app_nickname = {'j': 'jupyter notebook --no-browser',
                'd': 'grip',
                'k': 'mkdocs serve'}
def guess_app():
    from os import listdir

    app_trait = {'.ipynb': 'j',
                 '.md': 'd',
                 'mkdocs.yml': 'k'}
    for i in listdir():
        for j in ('.ipynb', '.md', 'mkdocs.yml'):
            if i.endswith(j):
                return app_trait[j]
```
- 有时候应用不止一次地输出应打开的地址，这时要立一个flag
```python
XB_STATUS = False
def start_app(cmd):
    global XB_STATUS
	......
	r = findall('http://.*/', line) or findall('http://.*$', line)
	if len(r) > 0 and not XB_STATUS:
		print(r[0])
		popen('termux-open-url "%s"' % r[0])
		XB_STATUS = True
```
