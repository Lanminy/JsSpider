&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;今天带大家分析一下某建筑市场监管平台的数据加密

链接:

> aHR0cDovL2p6c2MubW9odXJkLmdvdi5jbi9kYXRhL2NvbXBhbnk=

点击企业查询, 发现返回的数据是经过加密后的数据

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d7d13efb22?w=2874&h=1568&f=png&s=629586"/>

> 1. 寻找返回的数据

既然数据是通过这个 url 返回的, 全局搜索url

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d7d25f2180?w=2880&h=1566&f=png&s=868978"/>

[http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15](http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15)

尝试全局模糊搜索 `/query/comp/list` 

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d7cf4874d2?w=2880&h=1590&f=png&s=671714"/>



点击进入 js 函数

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d7d185f6fe?w=2880&h=1560&f=png&s=863664"/>



返回的结果是请求 url `/dataservice/query/comp/list `得到的, 打上断点 点击搜索 一步一步调式js代码

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d7cd1ea1af?w=2870&h=1486&f=png&s=689594"/>



调试过程就不一步一步分析了,  最终定位到, 感觉像我们想要的数据, 进入Console打印一下 **t**  和 **e**

![](http://mingyang920.com/blog/img/Snipaste_2020-02-19_20-22-30.png)



t 的打印结果

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d80f416a2b?w=2874&h=1538&f=png&s=734322"/>





**t** 中 **data** 是 最初我们请求`http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15` 所返回的加密后数据



然后接着执行下一步, 你会发现,  **e** 这其中的数据不正是我们想要的数据

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d819a938c2?w=2846&h=1548&f=png&s=903069"/>

> 2. 分析加密方式

既然我们已经知道了数据的加密方式, 那我们就重点分析一下这个地方

![](http://mingyang920.com/blog/img/Snipaste_2020-02-19_20-17-55.png)



其中t.data我们在第一步已经分出来了 使我们第一步请求 `http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15`得到的结果

<img src="https://user-gold-cdn.xitu.io/2019/10/20/16de70d83c5d4d7c?w=2874&h=1490&f=png&s=404741"/>



那我们重点分析 **m** 函数 的处理过程, 点击进入 **m** 函数, 结果如下

![](http://mingyang920.com/blog/img/Snipaste_2020-02-19_20-12-40.png)



对数据经过层层加密处理后,调用toString方法, 既然加密函数已经找到,我们就可以编写代码了

> 3. 代码实现

我们将函数 **m** 的代码复制出来, data是加密后返回的数据,我们先复制出来用一下，在这里因为我们使用了 **crypto-js**，所以我们要先进行安装一下

![](http://mingyang920.com/blog/img/Snipaste_2020-02-19_20-11-39.png)



运行一下项目

![](http://mingyang920.com/blog/img/Snipaste_2020-02-19_20-10-02.png)



报错的原因 , 其中  **p**  和 **f** 没有进行初始化 我们寻找一下 p 和 f , 就在函数 m 的上方

![](http://mingyang920.com/blog/img/Snipaste_2020-02-20_15-01-07.png)我们添加到代码把 p 和 f 添加到代码中

![](http://mingyang920.com/blog/img/Snipaste_2020-02-19_20-08-38.png)



运行项目 进行测试

![](http://mingyang920.com/blog/img/Snipaste_2020-02-19_20-07-13.png)

其中返回的数据 , 正是我们想要的结果

##  

以上就是今天的内容了，本文仅供学习交流使用，如有任何利益问题请联系笔者删除，祝大家学习愉快