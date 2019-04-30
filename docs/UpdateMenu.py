from os import listdir, walk
from os.path import isdir


def handle_file(md, item):
    directory, files = item[0], item[2]
    if directory == '.':
        return
    depth = directory.count('/')
    md.write('    ' * (depth - 1) + '- %s\n' % directory.split('/')[-1])
    md_files = filter(lambda f: f.endswith('.md'), files)
    for f in md_files:
        with open(directory + '/' + f, 'r', encoding='utf-8') as fi:
            title = fi.readline()[2:-1]
        s = '    ' * depth + '- [%s](%s/%s)\n'%(title, directory, f)
        md.write(s)

with open('index.md','w',encoding='utf-8') as md:
    md.write('# 目录\n')
    for item in walk('.'):
        handle_file(md, item)
