import requests
from loguru import logger
import json

def get_h5st(data):
    params = {
        'group': 'test_web3',
        'clientId': 'jd33',
        'action': 'jd',
        'pp': data,
        'param': 22
    }
    for i in range(50):

        res=requests.get('http://127.0.0.1:5612/business/invoke',params=params)
        if('fb5df' in res.text):
            # logger.info(json.loads(res.text).get('data'))
            return json.loads(res.text).get('data')
