from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

import config
BUCKET=config.BUK

def conn():
   d=config.cos_conn_cfg
   c=CosConfig(**d)
   return CosS3Client(c)

def upload_stream(file_name="/test/ccc",Body=b'abcdefg'):
    client=conn()
    response = client.put_object(
        Bucket=BUCKET,
        Body=Body,
        Key=file_name
    )
    return response

def upload_local(LocalFilePath='upload.py'):
    client=conn()
    response = client.upload_file(
        Bucket=BUCKET,
        LocalFilePath=LocalFilePath,
        Key="test/"+LocalFilePath,
        PartSize=10,
        MAXThread=10
    )
    return response

def list(z={ "Bucket":BUCKET,"Prefix":'douban' }):
    client=conn()
    return client.list_objects(**z)

def list_b():
    client=conn()
    return client.list_buckets()

def remove_b(Bucket=BUCKET):
    client=conn()
    response = client.delete_bucket(
    Bucket=Bucket
    )
    return response

def get_acl(Bucket=BUCKET):
    client=conn()
    response = client.get_bucket_acl(
        Bucket=Bucket
    )
    return response

def insert_b():
    client=conn()
    response = client.create_bucket(
        Bucket=BUCKET,
        #ACL='private'|'public-read'|'public-read-write',
        GrantFullControl='string',
        GrantRead='string',
        GrantWrite='string'
    )


def upload_sfile( file_name = 'test.txt' ):
    client=conn()
    with open(file_name , 'rb') as fp:
        response = client.put_object(
            Bucket=BUCKET,
            Body=fp,
            Key=file_name,
            StorageClass='STANDARD',
            ContentType='text/html; charset=utf-8'
        )
        print(response['ETag'])

# 本地路径 简单上传
def upload_sfile0():
    client=conn()
    response = client.put_object_from_local_file(
        Bucket=BUCKET,
        LocalFilePath='local.txt',
        Key=file_name,
    )
    print(response['ETag'])


# 设置HTTP头部 简单上传
def upload_sfile1():
    client=conn()
    response = client.put_object(
        Bucket=BUCKET,
        Body=b'test',
        Key=file_name,
        ContentType='text/html; charset=utf-8'
    )
    print(response['ETag'])

def upload_sfile2():
    client=conn()
    response = client.put_object(
        Bucket=BUCKET,
        Body=b'test',
        Key=file_name,
        Metadata={
            'x-cos-meta-key1': 'value1',
            'x-cos-meta-key2': 'value2'
        }
    )
    print(response['ETag'])


def download(file_name,filename1='output.txt'):
    client=conn()
    response = client.get_object(
        Bucket=BUCKET,
        Key=file_name,
    )
    response['Body'].get_stream_to_file(filename1)

def download2(file_name="/test/upload.py"):
    client=conn()
    response = client.get_object(
        Bucket=BUCKET,
        Key=file_name,
    )
    fp = response['Body'].get_raw_stream()
    print(fp.read(2))

def remove(Key='exampleobject'):
    response = client.delete_object(
        Bucket=BUCKET,
        Key=Key,
    )
    return response

def removes(kk=[]):
    if len(kk) < 1 : return []
    o= [{'Key':x} for x in kk]
    response = client.delete_objects(
        Bucket=BUCKET,
        Delete={
            'Object': o,
            'Quiet': 'true'
        }
    )
    return response

