"""
Retrieve information from operational system with os.system using df -h
"""
import os
import json


def get_mount_point():
    """ Retrieve Mount points """
    # print subprocess.call([df --output=avail -h "$PWD" | sed '1d;s/[^0-9]//g'])
    print os.system('df -h > text.txt')


def get_from_text():
    """ Update Json file with Text information """

    with open('out.json', 'w') as outfile:
        with open('text.txt', 'r') as f_file:
            for line in f_file:
                dicionario = line.split('\n')
                jsondata = json.dumps(
                    {
                        "disk-usage": {
                            "filesystem": dicionario[0],
                            "sizetotal": dicionario[1],
                            "occupied": dicionario[2],
                            "available": dicionario[3],
                            "perc-used": dicionario[4],
                            "mounted-on": dicionario[5]
                        }
                    }, separators=(',', ': '), indent=4)

                outfile.write(jsondata)


if __name__ == ("__main__"):
    get_mount_point()
    get_from_text()
