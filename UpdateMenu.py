from os import walk


def handle_file(md, root, files):
    depth = root.count('/')
    md.write('    ' * (depth - 1) + '- %s\n' % root.split('/')[-1])
    md_files = filter(lambda f: f.endswith('.md'), files)
    for f in sorted(md_files):
        with open(root + '/' + f, 'r', encoding='utf-8') as fi:
            title = fi.readline()[2:-1]
        s = '    ' * depth + '- [%s](%s/%s)\n' % (title, root, f)
        md.write(s)


with open('index.md', 'w', encoding='utf-8') as md:
    md.write('# Table of Contents\n')
    for root, dirs, files in walk('.'):
        if root != '.':
            handle_file(md, root, files)
