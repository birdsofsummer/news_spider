import env
import json
import os
from sts.sts import Sts
import config

cfg=config.upload_auth_config

#os.environ
def to_json(r):
    return json.dumps(r, indent=4)

def main():
    r={"ok":False,"data":{}}
    try:
        sts = Sts(cfg)
        response = sts.get_credential()
        r['data']=response
        r['ok']=True
    except Exception as e:
        print(e)
    finally:
        return r

# 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
ddd=[
            'name/cos:PutObject',
            'name/cos:PostObject',
            'name/cos:InitiateMultipartUpload',
            'name/cos:ListMultipartUploads',
            'name/cos:ListParts',
            'name/cos:UploadPart',
            'name/cos:CompleteMultipartUpload',
            'name/cos:SliceUploadFile',
            'name/cos:GetObject',
        ]

