"""
测试发帖的异常场景
https://docs.pytest.org/en/6.2.x/example/parametrize.html#paramexamples
"""

import requests
import pytest
import json

data = json.load(open('data/topics.json',mode='r',encoding='utf-8'))
test_data = data["test_data"]

@pytest.mark.parametrize('topic_data,code,msg',test_data)
def test_create_topic(topic_data,code,msg):
    print(topic_data,code,msg)
    res = requests.post('https://cnodejs.org/api/v1/topics',topic_data)
    print(res.json())

    assert res.status_code == code

    assert res.json()['error_msg'] == msg