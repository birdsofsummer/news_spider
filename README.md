#  scf 新闻爬虫

## web
    [news](https://douban.qing.workers.dev/)

## 站点
    [hackernews][1]
    [sputniknews][2]
    [reuters][3]
    [环球网][4]
    [微博热搜][5]

    [1]: http://hackernews.betacat.io/
    [2]: http://sputniknews.cn/
    [3]: http://cn.reuters.com/
    [4]: http://www.huanqiu.com/
    [5]: https://www.enlightent.cn/research/rank/weiboSearchRank 

## 文件路径

    [依赖列表](./depend.txt)
    [安装包](./vendor)
    [入口](./index.py)
    [爬虫](./spider.py)
    [解析](./parser)

## 接口

    [base](https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/)

    +  /hack_news
    +  /sputni
    +  /vbc?n=1
    +  /huanqiu?n=1
    +  /news    

    + https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/hack_news
    + https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/sputni
    + https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/vbc?n=2    
    + https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/huanqiu?n=1
    + https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/news

```shell
    #安装 
    ./setup i
    #部署到腾讯云 
    ./setup 
```
