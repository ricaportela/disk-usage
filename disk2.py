import subprocess
import sys
import json


def get_mount_point():
    """ Retrieve Mount points """
    output = subprocess.check_output(['df', '-h'])
    output = output.decode('utf-8')
    f_file = output.split('\n')

    print type(f_file)
    print len(f_file)

    for i in f_file:
        print i.split('\n')

if __name__ == ("__main__"):
    get_mount_point()
