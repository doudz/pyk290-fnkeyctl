# pyk290-fnkeyctl

Reconfigures the way the function keys on Logitech K290 keyboards work
This a python port of https://github.com/milgner/k290-fnkeyctl

Requires python-libusb1, to install
    sudo pip install libusb1

Works with python 2 and python 3

Tested on Ubuntu 15.04
## Running it

### Manually

Opening the device with libusb requires advanced permissions, so run it with
    sudo python k290_fnkeyctl.py
or
    sudo ./k290_fnkeyctl.py

Afterwards, you'll have regular function key behaviour. If you want to switch
back, just append `-r` or `--reset`.
