# -*- coding: utf-8 -*-

# import threading
import time
#
# flag = True
#
#
# def loop():
#     mydata = threading.local()
#     mydata.t0 = time.time()
#     for i in range(10000):
#         time.sleep(0.002)
#         # a = i ** i
#         # if not flag:
#         #     break
#     print('loop', threading.get_ident(), time.time() - mydata.t0)
#
#
# def proc(n):
#     mydata = threading.local()
#     mydata.t0 = time.time()
#     for i in range(n):
#         a = i ** i
#     print('proc', threading.get_ident(), time.time() - mydata.t0)
#
#
# # loop()
# # proc(10000)
#
# t0 = time.time()
#
# # th1 = threading.Thread(target=proc, args=(5000,))
# th1 = threading.Thread(target=loop)
# th2 = threading.Thread(target=proc, args=(10000,))
#
# th2.start()
# th1.start()
#
# # flag = False
# th2.join()
# # flag = False
# th1.join()
#
# !/usr/bin/env python3

t0 = time.time()

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('Received:', data)
            if not data:
                break
            conn.sendall(data)

print('End', time.time() - t0)
