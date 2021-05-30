import requests

def create_topic(topicdata):
    url = 'https://cnodejs.org/api/v1/topics'
    r = requests.post(url=url, json=topicdata)
    return r


def topic_detail(id):
    url = 'https://cnodejs.org/api/v1/topic/'+id
    return requests.get(url)


def get_token():
    return 'd1de094d-8418-41d3-8d21-7a2b06a39203'