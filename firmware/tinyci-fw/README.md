# TinyCI Relay Firmware

## Build
```
. /path/to/esp-idf/export.sh
idf.py build
```

## Ground IO0
```
idf.py flash
```

## Test
```
python2.7 tinyci-relay.py 192.168.1.12 PWR0
python2.7 tinyci-relay.py 192.168.1.12 OFF2
```
