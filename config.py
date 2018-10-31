# -*- coding:utf-8 -*-
from api.wallet import WalletClient
from rest.api.api import Client

# 企业钱包签名参数
ent_sign_param = {
    "creator": "did:axn:bb46d69f-6bff-4106-b57c-67851ef55e1e",  # 企业钱包用户DID
    "nonce": "nonce",  # 企业钱包签名随机数
    "privateB64": "o+RpUZpjBhSuDbn4HuV3KghNic227hCnLaK+rTHRd8wN+OW8IToLSvq2l0s4HeKOYOgUYu5atAvbYEwiz/a5kg=="  # 企业钱包BASE64私钥，即交易签名凭证
}

client = Client(
    r"z_pGym - Tp15288809805",  # API-KEY
    r"D:\suyako-to-be-coder\python-env\blockchain\Lib\site-packages\py_common-2.0.1-py2.7.egg\cryption\ecc\certs",
    # CERTS-PATH
    ent_sign_param,
    r"http://139.198.15.132:9143"  # 网关
)

header = {"Bc-Invoke-Mode": "sync"}