from os import popen
from sys import argv
import subprocess
from re import findall


app_nickname = {'j': 'jupyter notebook --no-browser',
                'd': 'grip',
                'k': 'mkdocs serve'}


def guess_app():
    from os import listdir, getcwd, chdir
    from os.path import splitext

    app_trait = {'.ipynb': 'j',
                 '.md': 'd'}
    # Support launch mkdocs even deep inside the directory
    chdir(getcwd().split('docs')[0])
    if 'mkdocs.yml' in listdir():
        return 'k'
    exts = {}
    # Convert to only extentions
    all_file = list(map(lambda x: splitext(x)[1], listdir()))
    for k in app_trait:
        exts[k] = all_file.count(k)
    # Get the most frequent one
    most = sorted([(k, v)for k, v in exts.items()],
                  key=lambda x: x[1], reverse=True)[0][0]
    return app_trait[most]


def get_app():
    if len(argv) > 1 and argv[1] in app_nickname:
        app = app_nickname[argv[1]]
        arg = ' '.join(argv[2:])
    else:
        app = app_nickname[guess_app()]
        arg = ' '.join(argv[1:])
    return ' '.join((app, arg))


def start_app(cmd):
    XB_STATUS = False
    try:
        backup = subprocess.Popen(
            cmd.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(backup.stdout.readline, b''):
            line = line.rstrip().decode('utf8')
            r = findall('http://.*/', line) or findall('http://.*$', line)
            if r and not XB_STATUS:
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
    start_app(get_app())
