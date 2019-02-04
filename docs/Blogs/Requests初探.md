# Requests 初探
`requests` 模块获取http回复十分方便，一句`requests.get(url)`即可搞定。
下面贴上从`mliucixin.zuopinj.com/`抓取刘慈欣小说全集的代码：

```python
import requests
from re import findall
from time import sleep


end, start = 202227+1, 201980
num = end-start
with open('lcx.html', 'w', encoding='utf-8') as f:
    last_novel = ''
    for i in range(num):
        r = requests.get(
            'http://mliucixin.zuopinj.com/5561/%d.html' % (start+i))
        text = r.text.replace('\r\n', '')
        novel, chapter = findall(
            pattern='<meta name="keywords" content="(.*?)" />', string=text)[0].split(',')
        p = findall(pattern='<p>(.*?)</p>', string=text)[0]
        if novel != last_novel:
            f.write('<h1>%s</h1>\n' % novel)
            last_novel = novel
        f.write('<h2>%s</h2>\n' % chapter)
        print('writing', start+i, novel, chapter)
        f.write(p)
        f.write('\n')
        sleep(0.2)
```
几点说明：

- 该网站url十分简单，只需改变最后.html前的数字即可抓取全集。
- 在re.findall时，如果html中含有换行符，将导致匹配不成功。
- 生成html后，使用Calibre转换为AZW3直接用USB发至Kindle中，二级目录才有效。
