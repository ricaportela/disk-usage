import os
import sys
import json
# Sist. Arq.                           Tam. Usado Disp. Uso% Montado em
# /dev/mapper/vg_oc3060845136-lv_root  285G   35G  236G  13% /

jsonData = { "Sist. Arq": "/dev/mapper/vg_oc3060845136-lv_root",
              "Tam": "285G",
              "Usado": "35G",
              "Uso": "236G",
              "Montado": "/"
          }


def get_mount_point():
    # print subprocess.call([df --output=avail -h "$PWD" | sed '1d;s/[^0-9]//g'])
    print os.system('df -h > text.txt')

def get_from_text():
    with open('text.txt', 'r') as f_file:
        for line in f_file:
            dicionario = line.split()
            print "Sist. Arq. ", dicionario[0]
            print "Tam        ", dicionario[1]
            print "Usado      ", dicionario[2]
            print "Disponivel ", dicionario[3]
            print "Em Uso     ", dicionario[4]
            print "Montado em ", dicionario[5]

            #with open('out.json', 'w') as j_file:
            #     json.dump(jsonData, f_file)


if __name__ == ("__main__"):
    get_mount_point()
    get_from_text()
