import sys
import json
# Sist. Arq.                           Tam. Usado Disp. Uso% Montado em
# /dev/mapper/vg_oc3060845136-lv_root  285G   35G  236G  13% /

jsonData = {  "Sist. Arq ": "/dev/mapper/vg_oc3060845136-lv_root",
              "Tamanho   ": "285G",
              "Usado     ": "35G",
              "Disponivel": "236G",
              "Uso       ": "13%",
              "Montado em": "/"
          }


json.dump(jsonData, sys.stdout)
