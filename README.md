# pyk290-fnkeyctl

Reconfigures the way the function keys on Logitech K290 keyboards works.
This is a python port of https://github.com/milgner/k290-fnkeyctl

Requires python-libusb1, to install
    ```sudo pip3 install libusb1```
    
or
     ```sudo apt install python3-libusb1```

Works with python 2 and python 3

Tested on Ubuntu 15.04, 16.04, 17.04 and 18.04
## Running it

### Manually

Opening the device with libusb requires advanced permissions, so run it with
```
    sudo python3 k290_fnkeyctl.py
or
    sudo ./k290_fnkeyctl.py
```
Afterwards, you'll have regular function key behaviour. If you want to switch
back, just append `-r` or `--reset`.

### Automatically (udev)

To automatically run the program when the device is plugged in, you can use the included udev rules script as a template. Or just automatically install them along with the executable with
```
sudo ./install.sh
```

Which will copy the executable to /usr/local/sbin and install the udev rules into /etc/udev/rules.d. Now you'll just need to tell udev to apply the new rules:
```
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=input
```
