import requests
from pprint import pprint


def get_stack_q():
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=1665532800&todate=1665705600&order=desc&sort=activity&tagged=python&site=stackoverflow'
    resp = requests.get(url)
    return resp.json()


pprint(get_stack_q())
