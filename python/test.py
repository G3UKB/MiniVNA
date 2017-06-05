#!/usr/bin/env python3

import os, sys
import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(('127.0.0.1', 10002), pickle.dumps(['fres', 1800, 1850])


