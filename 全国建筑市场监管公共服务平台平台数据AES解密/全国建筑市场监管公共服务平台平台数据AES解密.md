

[http://jzsc.mohurd.gov.cn/data/company](http://jzsc.mohurd.gov.cn/data/company)击企业查询, 发现返回的数据是经过加密的

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-14-38.png"/>

### 1.寻找返回的数据

既然数据是通过这个 url 返回的, 全局搜索url

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-21-57.png"/>

[http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15](http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15)

尝试全局模糊搜索 `/query/comp/list` 

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-25-42.png"/>



点击进入 js 函数

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-27-33.png"/>



返回的结果是请求 url `/dataservice/query/comp/list `得到的, 打上断点 点击搜索 一步一步调式js代码



<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_01-47-46.png"/>



调试过程就不一步一步分析了,  最终定位到, 感觉像我们想要的数据, 进入Console打印一下`t` 和 `e`

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-33-15.png"/>





`t`

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-35-05.png"/>





t 中data 是 最初我们请求`http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15` 所返回的数据



`e` 这其中的数据不正是我们想要的数据

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-38-23.png"/>



### 2.分析加密方式

既然我们已经知道了数据的加密方式, 那我们就重点分析一下这个地方

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-44-25.png"/>



其中t.data我们在第一步已经分出来了 使我们第一步请求 `http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15`得到的结果

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-46-24.png"/>



那我们重点分析 p函数 的处理过程, 点击进入 p函数, 结果如下

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-48-21.png"/>



对数据经过层层加密处理后,调用toString方法, 既然加密函数已经找到,我们就可以编写代码了



### 3.代码实现

我们将函数 p 的代码复制出来, data是加密后返回的数据,我们先复制出来用一下

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-57-46.png"/>



运行一下项目

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_00-59-50.png"/>



报错的原因 , 其中 `u` 和 `d` 没有进行初始化 我们寻找一下 u 和 d , 就在函数 p的上方

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_01-01-54.png"/>

我们添加到代码把 u 和 d 添加到代码中

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_01-03-24.png"/>



运行项目 进行测试

<img src="http://mingyang920.com/blog/img/Snipaste_2019-10-20_01-04-21.png"/>



其中返回的数据 , 正是我们想要的结果

##  

请勿用于非法用途



