import requests
import json
import time

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


def main():
    urls = ['https://api1.example.com/v1/payments/',
            'https://api2.example.com/v6/order/history/']

    print unifies_api(urls)


def unifies_api(urls):
    payment_id = ['id', 'orderID']
    total = ['amount']
    last_4 = []
    details = ['memo', 'description']

    unified_api = []

    # for url in urls:
    #     j = json.loads(requests.get(url).text)
    for api in APIs:
        j = json.loads(api)
        for d in j:
            for key in d:
                if key in payment_id:
                    d['remote_payment_id'] = d.pop(key)
                elif key in total:
                    d['total'] = d.pop(key)
                elif key in last_4:
                    d['last_4'] = d.pop(key)
                elif key in details:
                    d['details'] = d.pop(key)
        unified_api = unified_api + j

    return json.dumps(unified_api)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("\n%s seconds" % (time.time() - start_time))
