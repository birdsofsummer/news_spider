import re,sys, time, os, json, random
from ajax import get1
from task import run1

en_news={
        "sputni":"https://sputniknews.com/export/rss2/archive/index.xml",
        "usni":"https://news.usni.org/feed",
        "nationalreview":"https://www.nationalreview.com/news/",
        "msn":"https://www.msn.com/en-us/news/",
        "stripes":"https://www.stripes.com/news",
        "cnn":"https://edition.cnn.com/",
        "hill":"https://thehill.com/",
}

#curl https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/hack_news
def hack_news():
    from parser.hack_news import  hack_news_parser
    u="http://hackernews.betacat.io/"
    r=get1(u)
    return hack_news_parser.hack_news_parser(r)

# curl https://service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com/release/weibo/sputni
def sputniknews():
    from parser.sputniknews.main  import parse
    u=["http://sputniknews.cn/export/rss2/archive/index.xml","https://sputniknews.com/export/rss2/archive/index.xml"]
    r=get1(u[0])
    return parse(r)


def rt_news():
    u={
	"general": "https://www.rt.com/rss/",
	"news": "https://www.rt.com/rss/news/",
	"usa": "https://www.rt.com/rss/usa/",
	"uk": "https://www.rt.com/rss/uk/",
	"sport": "https://www.rt.com/rss/sport/",
	"russia": "https://www.rt.com/rss/russia/",
	"business": "https://www.rt.com/rss/business/",
	"op-ed": "https://www.rt.com/rss/op-ed/",
	"rt360": "https://www.rt.com/rss/applenews/rt360/",
	"newsline": "https://www.rt.com/rss/newsline/",
	"podcasts": "https://www.rt.com/rss/podcasts/"
    }

#u="http://cn.reuters.com/rssFeed/vbc_homepagetopnews/"
def reutersmedia(n=3):
    from parser.vbc.main  import parse
    m={
	"chinaNews": "中国财经",
	"CNAnalysesNews": "深度分析",
	"CNIntlBizNews": "国际财经",
	"CNTopGenNews": "时事要闻",
	"CNEntNews": "娱乐体育",
	"CNTechNews": "科技电子",
	"CNEnvNews": "气候环境",
	"CNTravelNews": "旅游休闲",
	"oddlyenoughNews": "寰宇花絮",
	"CNMgtNews": "职场管理",
	"CNColumn": "中国财经专栏",
	"IntColumn": "国际财经专栏",
	"ComColumn": "大宗商品专栏",
	"vbc_homepagetopnews": "今日要闻集合",
	"vbc_livestyle_landing": "生活类新闻集合",
	"vbc_CN_columnist_all": "路透专栏集合",
	"cnBizNews": "财经报道",
	"cnInvNews": "投资资讯",
	"companyNews": "公司新闻",
	"cnMktNews": "市场报道",
	"stocksNews": "股票",
	"fundsNews": "基金",
	"bondsNews": "债券",
	"currenciesNews": "外汇",
	"industryNews": "产业",
	"macroeconomicsNews": "宏观经济",
	"commoditiesNews": "商品期货",
	"optionsNews": "期货期权",
	"mergersNews": "兼并收购",
	"newIssueNews": "新股公告",
	"hedgeFundsNews": "对冲基金",
	"privateEquityNews": "私募投资",
	"regulatoryNews": "政策信息",
	"realEstateNews": "地产资讯",
	"techMediaTelcoNews": "科技资讯",
	"healthDrugsNews": "医药健康",
	"transportationNews": "汽车交通",
	"financialServicesNews": "金融服务",
	"usMktNews": "美国市场",
	"eurMktRpt": "欧洲市场",
	"tokyoMktRpt": "日本市场",
	"hongkongMktRpt": "香港市场",
	"sasiaMktRpt": "东南亚市场"
    }
    kk=[k for k,v in m.items()]
    n1= n if n>0 and n< len(kk) else 3
    prefix="http://cn.reuters.com/rssFeed/"
    u=prefix+kk[n1]
    r=get1(u)
    return parse(r)


def huanqiu(n=12):
       from parser.huanqiu.main  import parse
       m={
            "国际热点": "http://rss.huanqiu.com/world/hot.xml",
            "环球博览": "http://rss.huanqiu.com/world/well_read.xml",
            "国际军事": "http://rss.huanqiu.com/mil/world.xml",
            "环球时报独家": "http://rss.huanqiu.com/mil/paper.xml",
            "军事图库": "http://rss.huanqiu.com/mil/Focus_photo.xml",
            "移动互联网": "http://rss.huanqiu.com/tech/net.xml",
            "科学探索": "http://rss.huanqiu.com/tech/discovery.xml",
            "科技人物": "http://rss.huanqiu.com/tech/per.xml",
            "国际财经": "http://rss.huanqiu.com/finance/world.xml",
            "壹周刊": "http://rss.huanqiu.com/society/Newsweek.xml",
            "世界风云录": "http://rss.huanqiu.com/history/world.xml",
            "今日话题": "http://rss.huanqiu.com/opinion/topic.xml",
            "最新": "http://rss.huanqiu.com/topnews.xml",
            "国际新闻": "http://rss.huanqiu.com/world/roll.xml",
            "国内新闻": "http://rss.huanqiu.com/china/roll.xml",
            "中国军事": "http://rss.huanqiu.com/mil/china.xml",
            "科技新闻": "http://rss.huanqiu.com/tech/news.xml",
            "财经头条": "http://rss.huanqiu.com/finance/roll.xml",
            "两岸时政": "http://rss.huanqiu.com/taiwan/news.xml",
            "娱乐头条": "http://rss.huanqiu.com/ent/yuletoutiao.xml",
            "素食养生": "http://rss.huanqiu.com/health/health_promotion.xml",
            "网聚焦": "http://rss.huanqiu.com/society/focus.xml",
            "法天下": "http://rss.huanqiu.com/society/law.xml",
            "图说世界": "http://rss.huanqiu.com/photo/gallery.xml",
            "环球视觉": "http://rss.huanqiu.com/ifoto/globalvisual.xml",
            "健康资讯": "http://rss.huanqiu.com/health/health_news.xml",
            "数码资讯": "http://rss.huanqiu.com/tech/digi.xml",
            "家电资讯": "http://rss.huanqiu.com/tech/elec.xml",
            "中国财经": "http://rss.huanqiu.com/finance/china.xml",
            "财经独家": "http://rss.huanqiu.com/finance/view.xml",
            "时政要闻": "http://rss.huanqiu.com/oversea/political.xml"
       }
       kk=[v for k,v in m.items()]
       n1= n if n>0 and n< len(kk) else 12
       u=kk[n1]
       r=get1(u)
       return parse(r)



def nationalreview():
    pass

def msn():
    pass

def usni():
    pass

def stripes():
    pass

def cnn():
    pass


def news():
    t=[sputniknews,reutersmedia,huanqiu]
    return run1(t)
