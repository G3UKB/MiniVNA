#!/usr/bin/env python3

import os, sys
import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 10003))
#sock.sendto(pickle.dumps(['fres', 1800, 1850]), ('127.0.0.1', 10002))
#sock.sendto(pickle.dumps(['fswr', 1800]), ('127.0.0.1', 10002))
sock.sendto(pickle.dumps(['scan', 1800, 1850]), ('127.0.0.1', 10002))
data, address = sock.recvfrom(1000)
print(pickle.loads(data))
