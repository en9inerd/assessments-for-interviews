import itertools
import json
import requests
import time


def main():
    urls = ['https://api1.example.com/v1/payments/',
            'https://api2.example.com/v6/order/history/']

    print unifies_api(urls)


def unifies_api(urls):
    unified_api = []

    # for url in urls:
    #     unified_api = unified_api + json.loads(requests.get(url).text)
    for api in APIs:
        unified_api = unified_api + json.loads(api)

    unified_api = [first_non_none(v(d) for v in vers) for d in unified_api]

    return json.dumps(unified_api)


def ver1(d):
    if 'id' not in d:
        return None
    d['remote_payment_id'] = d.pop('id')
    d['total'] = d.pop('amount')
    d['details'] = d.pop('memo')
    return d


def ver6(d):
    if 'orderID' not in d:
        return None
    d['remote_payment_id'] = d.pop('orderID')
    d['details'] = d.pop('description')
    return d

vers = [ver1, ver6]
APIs = ["""
[
    {
        "id": "42d213d2-cdc2-4655-99ec-9335b91c9a8f",
        "amount": "20.99",
        "last_4": "1111",
        "memo": "For the bill"
    }
]
""",
        """
[
    {
        "orderID": "32342302010102",
        "total": "9.99",
        "last_4": "1111",
        "description": "Services rendered"
    }
]
"""
        ]


def first_non_none(i):
    ''' return first non-None element in list '''
    return list(filter(None, i))[0]

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("\n%s seconds" % (time.time() - start_time))
