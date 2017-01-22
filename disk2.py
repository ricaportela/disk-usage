""" Retrieve data from command line """
import subprocess
import json


def get_mount_point():
    """ Retrieve Mount points """
    jsondata = {}
    output = subprocess.check_output(['df', '-h'])
    output = output.decode('utf-8')
    f_file = output.split('\n')
    with open('out.json', 'w') as outfile:
        for item in f_file:
            linha = item.split()
            if linha[2:10] <> 'Filesystem':
                jsondata = json.dumps(linha, separators=(',', ': '), indent=4)
                outfile.write(jsondata)

if __name__ == ("__main__"):
    get_mount_point()
