import requests
import json


def main():
    url = "https://gist.githubusercontent.com/jkatz/2432c6d0c88af56e7162/raw/06a2c04adcf273c7bf542576874b01c26b586f3b/1.json"
    resp = requests.get(url)
    l = json.loads(resp.text)

    print create_list(l, 0)


def create_list(l, i):
    els = []
    i = i + 1
    for el in l:
        els.append("\t" * i + "<li>" + el['name'] + "</li>\n")
        if el['sections']:
            els.append(create_list(el['sections'], i))

    return "\t" * (i - 1) + "<ul>\n" + ''.join(els) + "\t" * (i - 1) + "</ul>\n"


if __name__ == "__main__":
    main()
