import os

CONFIG={
	"db_url": os.environ['mongo'],
	"db": "test",
	"table": "douban",
	"sendbackHost0": "https://service-d6p7no2y-1252957949.ap-hongkong.apigateway.myqcloud.com/test/hello",
	"sendbackHost": "http://set-hk_adaptor_set1.cb-guangzhou.apigateway.tencentyun.com/api-jvucznm6",
	"internalDomain": "http://set-hk_adaptor_set1.cb-guangzhou.apigateway.tencentyun.com/api-jvucznm6",
	"front_end": "wss://service-afbgj3k2-1252957949.ap-hongkong.apigateway.myqcloud.com/release/ws",
	"ApiId": "api-jvucznm6",
	"domain": "service-afbgj3k2-1252957949.ap-hongkong.apigateway.myqcloud.com",
	"cos_cfg": {
		"SecretId": "AKIDlQ2ZnrCd2iI1bx5F9i9dtSn374tsacZc",
		"SecretKey": "aO7QfZBKGNROEtcI7GONLD2H1a1Ll17B",
		"Bucket": "ttt-1252957949",
		"Region": "ap-hongkong",
		"Prefix": "douban"
	}
}

BUK='zzz-1252957949'
cos_conn_cfg= {
            'SecretId': 'AKIDlQ2ZnrCd2iI1bx5F9i9dtSn374tsacZc',
            'SecretKey': 'aO7QfZBKGNROEtcI7GONLD2H1a1Ll17B',
            'Region': 'ap-hongkong',
            'Token': None,
}

upload_auth_config= {
        'duration_seconds': 1800,
        'secret_id': 'AKIDlQ2ZnrCd2iI1bx5F9i9dtSn374tsacZc',
        'secret_key': 'aO7QfZBKGNROEtcI7GONLD2H1a1Ll17B',
        'bucket': BUK,
        'region': 'ap-hongkong',
        'allow_prefix': '*',
        'allow_actions': ["*"],
    }

