import os

SecretId=os.environ["SecretId"]
SecretKey=os.environ["SecretKey"]
Bucket=os.environ["Bucket"]
Region=os.environ["Region"]
Prefix=os.environ["Prefix"]

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
		"SecretId": SecretId,
		"SecretKey": SecretKey,
		"Bucket": Bucket,
		"Region": Region,
		"Prefix": Prefix
	}
}

cos_conn_cfg= {
            'SecretId': SecretId,
            'SecretKey': SecretKey,
            'Region': Region,
            'Token': None,
}

upload_auth_config= {
        'duration_seconds': 1800,
        'secret_id': SecretId,
        'secret_key': SecretKey,
        'bucket': Bucket,
        'region': Region,
        'allow_prefix': '*',
        'allow_actions': ["*"],
    }

