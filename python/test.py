#!/usr/bin/env python3

import os, sys
import socket
import pickle

CMD_PORT = 10002
RESPONSE_PORT = 10003
ARDUINO_IP = '192.168.1.108'

# Create a datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to the response port
sock.bind(('', RESPONSE_PORT))
sock.settimeout(20)

# Query the resonant frequency between the lower and upper bounds
sock.sendto(pickle.dumps(['fres', 1800000, 1900000]), (ARDUINO_IP, CMD_PORT))
# Wait for the response
data, address = sock.recvfrom(1000)
print('Resonant at - ', pickle.loads(data))

# Query the SWR at the given frequency
f = 1837000
sock.sendto(pickle.dumps(['fswr', f]), (ARDUINO_IP, CMD_PORT))
data, address = sock.recvfrom(1000)
print('SWR at %d - ' % (f), pickle.loads(data))
