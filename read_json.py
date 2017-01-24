""" Module Read json File """
import json


def read_json():
    """ Read values from Json File """
    data = []
    with open('out.json') as f_json:
        data = json.load(f_json)
        for p in data[1:1]:
            print p['size'], ' ', p['used'], ' ', p['avail']


if __name__ == ("__main__"):
    read_json()


