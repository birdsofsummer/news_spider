api={

    "base": "https://www.enlightent.cn/research/rank/weiboSearchRank",
    "word_cloud":{
                "url":"https://www.enlightent.cn/research/top/getHotSearchWordcloud.do",
                "method":"POST",
                "params":{"dayType":"today"}, #	yesterday,now
                "res":[{"size":260,"keyword":"哪吒"}],
    },
    "search":{
                "url":"https://www.enlightent.cn/research/top/getWeiboRankSearch",
                "method":"GET",
                "params":{
                    "keyword":"坐地铁",
                    "from":"1",
                    "type":"realTimeHotSearchList", #不填为全平台
                },
                "types":["realTimeHotSearchList","douyin","toutiao","douban"],
                "res":{
                        "rows": [
                                {
                                        "duration": 134400,
                                        "searchNums": 591467,
                                        "keywords": "偶遇姚明坐地铁",
                                        "updateTime": "1564971600",
                                        "type": "douyin",
                                        "topRanking": 3,
                                        "url": "null",
                                        "firstRankingTime": "1564831200"
                                }
                        ],
                        "total": 1
                }
     },
    "weibo":{
                "url":"https://www.enlightent.cn/research/top/getWeiboRank",
                "method":"GET",
                "params":{
                    "type":"realTimeHotSearchList", # "realTimeHotSearchList"|"douyin"|"toutiao"|"douban"
                    "date":"2019/08/04", # history
                 },
                "res":[
                    {
                            "type": "realTimeHotSearchList", #
                            "keywords": "人民币破7",
                            "ranking": 1,
                            "searchNums": 3730984,
                            "firstRankingTime": 1564969506,
                            "topRanking": 1,
                            "topRankingToday": 1,
                            "duration": 12000,
                            "updateTime": 1564981800000,
                            "others": "null",
                            "url": "http://s.weibo.com/weibo?q=%23%E4%BA%BA%E6%B0%91%E5%B8%81%E7%A0%B47%23",
                            "rankTotalCount": 20
                    }
                ]
        },
    "videoTop":{
            "url":"https://www.enlightent.cn/analytics/videoTop.do",
            "method":"POST",
            "data":{
                    "channelType": "tv", # "tv"|"movie"|"art"
                    "day": "1",
                    "sort": "playTimesPredicted",
                    "size": "30",
                    "channel": "total",
                    "net": "1", # ? 0|1
            },

            "params":{},
            },
    "videoTop1":{
            "url":"https://www.enlightent.cn/analytics/public/getVideoOpinionTop.do",
            "method":"POST",
            "data":{
                    "sort": "weixinScore", # "weiboScore"|"searchScore"|"yunheScore"
                    "channelType": "tv",   # "movie"|"tv"|"art"
                    "size": "30",
                    "date": "2019/08/04",  #?
            },
            "params":{ },
            },
    "star":{
            "url":"https://www.enlightent.cn/analytics/public/starBaPingTop",
            "method":"POST",
            "data":{
                    "channel": "total", # ? total|notNet|isNet
                    "sort": "screenIndex", #? screenIndex|yunheScore yunheScore? [sort,size]
                    "size": "30",
                    "day": "1"
                },
            },

    }

