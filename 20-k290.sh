#!/bin/bash

case "$1" in
    thaw|resume)
        /usr/local/sbin/k290_fnkeyctl.py > /dev/null
        ;;
    *) exit $NA
        ;;
esac
exit $?
