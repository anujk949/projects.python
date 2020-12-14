import re

def set_new_password(password):
    with open('/etc/wpa_supplicant/wpa_supplicant.conf','r') as f:
            in_file = f.read()
            f.close()

    out_file =  re.sub(r'psk=".*"','psk='+'"'+password+'"',in_file)

    with open('/etc/wpa_supplicant/wpa_supplicant.conf','w') as f:
            f.write(out_file)
            f.close()

set_new_password("hello")