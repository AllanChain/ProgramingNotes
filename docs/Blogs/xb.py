from os import popen
from sys import argv
import subprocess
from re import findall


app_nickname = {'j': 'jupyter notebook --no-browser',
                'd': 'grip',
                'k': 'mkdocs serve'}
XB_STATUS = False


def guess_app():
    from os import listdir

    app_trait = {'.ipynb': 'j',
                 '.md': 'd',
                 'mkdocs.yml': 'k'}
    for i in listdir():
        for j in ('.ipynb', '.md', 'mkdocs.yml'):
            if i.endswith(j):
                return app_trait[j]


def get_app():
    if len(argv) > 1 and argv[1] in app_nickname:
        app = app_nickname[argv[1]]
        arg = ' '.join(argv[2:])
    else:
        app = app_nickname[guess_app()]
        arg = ' '.join(argv[1:])
    return ' '.join((app, arg))


def start_app(cmd):
    global XB_STATUS
    try:
        backup = subprocess.Popen(
            cmd.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(backup.stdout.readline, b''):
            line = line.rstrip().decode('utf8')
            r = findall('http://.*/', line) or findall('http://.*$', line)
            if len(r) > 0 and not XB_STATUS:
                print(r[0])
                popen('termux-open-url "%s"' % r[0])
                XB_STATUS = True
            print(line)

    except KeyboardInterrupt:
        from os import _exit

        print('Quiting')
        backup.kill()
        _exit(0)


if __name__ == '__main__':
    cmd = get_app()
    start_app(cmd)
