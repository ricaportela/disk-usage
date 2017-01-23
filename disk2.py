""" Retrieve Data from Command line """

from collections import namedtuple
import subprocess
import json

FData = namedtuple("FData", "filesystem size used avail perc_used mounted_on")

def get_mount_point():
    """ Retrieve Mount points """
    output = subprocess.check_output(['df', '-h'])
    output = output.decode('utf-8')
    f_file = output.split('\n')
    usage_list = []
    with open('out.json', 'w') as outfile:
        for item in f_file[1:-1]:
            line = item.split()
            usage_list.append(FData(*line)._asdict())
            print(usage_list)
        outfile.write(json.dumps(usage_list))

if __name__ == ("__main__"):
    get_mount_point()
