"""
测试发帖的异常场景
https://docs.pytest.org/en/6.2.x/example/parametrize.html#paramexamples
"""

import requests
import pytest

test_data = [
    ({'accesstoken': '','title': 'aaaaaaaaa','tab': 'ask','content': 'bbbbbbbbbb'},401,'错误的accessToken'),
    ({'accesstoken': 'd1de094d-8418-41d3-8d21-7a2b06a39203','title': '','tab': 'ask','content': 'bbbbbbbbbb'},400,'标题不能为空'),
    ({'accesstoken': 'd1de094d-8418-41d3-8d21-7a2b06a39203','title': 'aaaaaaaaa','tab': '','content': ''},400,'必须选择一个版块')
]

@pytest.mark.parametrize('topic_data,code,msg',test_data)
def test_create_topic(topic_data,code,msg):
    print(topic_data,code,msg)
    res = requests.post('https://cnodejs.org/api/v1/topics',topic_data)
    print(res.json())

    assert res.status_code == code

    assert res.json()['error_msg'] == msg