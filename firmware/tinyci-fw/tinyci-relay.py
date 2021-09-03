# This example code is in the Public Domain (or CC0 licensed, at your option.)

# Unless required by applicable law or agreed to in writing, this
# software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.

# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
import re
import socket


# -----------  Config  ----------
PORT = 1234
INTERFACE = 'eth0'
# -------------------------------

def udp_client(address, payload):
    for res in socket.getaddrinfo(address, PORT, socket.AF_UNSPEC,
                                  socket.SOCK_DGRAM, 0, socket.AI_PASSIVE):
        family_addr, socktype, proto, canonname, addr = res
    try:
        sock = socket.socket(family_addr, socket.SOCK_DGRAM)
    except socket.error as msg:
        print('Could not create socket: ' + str(msg[0]) + ': ' + msg[1])
        raise
    try:
        sock.sendto(payload.encode(), addr)
        reply, addr = sock.recvfrom(128)
        if not reply:
            return
        print('Reply[' + addr[0] + ':' + str(addr[1]) + '] - ' + str(reply.decode()))
    except socket.error as msg:
        print('Error Code : ' + str(msg[0]) + ' Message: ' + msg[1])
        sock.close()
        raise
    return reply


if __name__ == '__main__':
    udp_client(sys.argv[1], sys.argv[2])
