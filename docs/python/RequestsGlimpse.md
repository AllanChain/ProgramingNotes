# Requests初探
`requests` 模块获取http回复十分方便，一句`requests.get(url)`即可搞定。
下面贴上从`mliucixin.zuopinj.com/`抓取刘慈欣小说全集的代码：

Download [lcx_spider.py](lcx_spider.py)

几点说明：

- 该网站url十分简单，只需一个for循环改改变最后.html前的数字即可抓取全集。
```python
end, start = 202227+1, 201980
num = end-start
for i in range(num):
    r = requests.get('http://mliucixin.zuopinj.com/5561/%d.html' % (start+i))
```
抓到的网页大概是这样的：
```html
<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>全频段阻塞干扰 第2章 “万年炎帝”号_手机小说在线阅读_刘慈欣作品集</title>
<meta name="keywords" content="全频段阻塞干扰,第2章 “万年炎帝”号" />
<meta name="description" content="刘慈欣作品集整理全频段阻塞干扰全集无弹窗手机小说在线阅读,当前章节：第2章 “万年炎帝”号" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, target-densitydpi=medium-dpi">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="translucent">
<link rel="apple-touch-icon" href="http://zuopinj.com/images/logo_64.png">
<link rel="apple-touch-icon-precomposed" href="http://zuopinj.com/images/logo_64.png">
<meta name="apple-mobile-web-app-title" content="作品集">
<meta name="msapplication-tap-highlight" content="no">
<meta name="format-detection" content="telphone=no, email=no">
<meta http-equiv="Cache-Control" content="no-transform" />
<link rel="stylesheet" type="text/css" href="http://zuopinj.com/css/ydread.css"/>
<script src="http://zuopinj.com/js/wap.js"></script>
</head>
<body>
<div id="readerWarp">
<h1 id="title">第2章 “万年炎帝”号</h1>
<div class="ad-mb01"><script>ad_zpjhf_wap();</script></div>
<div id="conWp">
<p>　　1月5日，近日轨道，&ldquo;万年炎帝&rdquo;号<br />
<br />
庄宇感到了一个人独居一座城市的孤独。<br />
<br />
&ldquo;万年炎帝&rdquo;号太空组合体确实有一座小城市那么大，它的体积相当于两艘巨型航空母舰，能使5000人同时在太空中生活。当组合体处于旋转重力状态时，里面甚至有一个游泳池和一条小河流，这在当今的太空工作环境中，可以说是绝无仅有的奢侈。但事实是，&ldquo;万年炎帝&rdquo;号是中国航天界一贯的节检思维的结果。它的设计思想是：在一个构造中组合太阳系内太空探索的所有功能，这样虽一次性投资巨大，但从长远看还是十分经济的。&ldquo;万年炎帝&rdquo;号被西方戏称为太空的瑞士军刀，它可做为空间站在地球各个高度的轨道上运行，它可以方便地移动到绕月球轨道，或做行星际探索飞行。&ldquo;万年炎帝&rdquo;号已进行过金星和火星飞行，并探测过小行星带。以它那巨大的体积，等于把一个研究院搬到了太空中，就太空科学研究而言，它比西方那些数量众多但小巧玲珑的飞船具有更大的优势。<br />
<br />
当&ldquo;万年炎帝&rdquo;号准备开始前往木星的为期三年的航行时，战争爆发了。当时它上面的一百多名乘员全都返回了地面，他们大部分是空军军官，只留下了庄宇一个人。这时&ldquo;万年炎帝&rdquo;号暴露出它的一个缺陷：在军事上它目标太大，且没有任何防御能力，没有预见到后来太空军事化的进程，是设计者的一个失误。战争爆炸后，&ldquo;万年炎帝&rdquo;号只能进行躲避飞行。向外太空是不行的，在木星轨道之内，有大量的北约无人航行器，它们都体积不大，武装或非武装，每一个对&tp://mliucixin.zuopinj.com/5558/202095.html"  class="section section-next">下一章</span>
<script>ad_zpjhf2_wap();</script>
<div class="chapter" id="chapter">
<span id="chapterPre" data-url="http://mliucixin.zuopinj.com/5558/202093.html" class="chapter-pre">上一章</span>
<a class="chapter-bt" href="http://mliucixin.zuopinj.com/5558/">目录</a>
<span id="chapterNext" data-url="http://mliucixin.zuopinj.com/5558/202095.html"  class="chapter-next">下一章</span>
</div>
<div style="margin-top:1px;"><script>ad_zpjhf3_wap();</script></div>
<div id="tipBg" class="tip-bg"></div>
<script type="text/javascript">
var CONFIG = {catalog: 1,tj: "",pos: '["","load"]',basehis : '{}',error : ""};CONFIG.pos = JSON.parse(CONFIG.pos);
</script>
<script>ad_zpjxf_wap();</script>
<script type="text/javascript" src="http://zuopinj.com/js/zepto.js"></script>
<script type="text/javascript" src="http://zuopinj.com/js/read.js"></script>
<div style="display: none;"><script>waptj();</script></div>
</body>
</html>
```
- 在re.findall时，如果html中含有换行符，将导致匹配不成功。
```python
text = r.text.replace('\r\n', '')
```
- 当然re是必须的
```python
novel, chapter = findall(pattern='<meta name="keywords" content="(.*?)" />', string=text)[0].split(',')
p = findall(pattern='<p>(.*?)</p>', string=text)[0]
```
- 生成html后，使用Calibre转换为AZW3直接用USB发至Kindle中，二级目录才有效。
