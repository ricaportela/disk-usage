import sys
import json
# Sist. Arq.                           Tam. Usado Disp. Uso% Montado em
# /dev/mapper/vg_oc3060845136-lv_root  285G   35G  236G  13% /


jsondata = {
    "disk-usage": {
        "filesystem": "/dev/mapper/vg_oc3060845136-lv_root",
        "size": "285G",
        "used": "35G",
        "available": "236G",
        "use-perc": "13%",
        "mounted-on": "/"
    }
}


json.dump(jsondata, sys.stdout)
