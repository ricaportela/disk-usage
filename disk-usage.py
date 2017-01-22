import os
import sys
import json


def get_mount_point():
    """ Retrieve Mount points """
    # print subprocess.call([df --output=avail -h "$PWD" | sed '1d;s/[^0-9]//g'])
    print os.system('df -h > text.txt')


def get_from_text():
    """ Update Json file with Text information """
    
    with open('out.json','w') as outfile:
        with open('text.txt', 'r') as f_file:
            for line in f_file:
                dicionario = line.split()
                jsondata = json.dumps({"Sist. Arq": dicionario[0],
                "Tamanho   ": dicionario[1],
                "Usado     ": dicionario[2],
                "Disponivel": dicionario[3],
                "Uso       ": dicionario[4],
                "Montado em": dicionario[5]
                }, separators=(',', ': '))
                               
                outfile.write(jsondata)

        
if __name__ == ("__main__"):
    get_mount_point()
    get_from_text()
