# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import asyncio

import websockets

#==============================================================================
# import socket
# import sys
#==============================================================================

from subprocess import Popen, PIPE, STDOUT

#==============================================================================
# async def citp_mediator(websocket, path):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_address = ('127.0.0.1', 8811)
#     sock.connect(server_address)
#     sock.sendall(b"10")
#     data = sock.recv(16)
#     print(data)
#==============================================================================
#    while True:
#        now = datetime.datetime.utcnow().isoformat() + 'Z'
#        await websocket.send(now)
#        await asyncio.sleep(100)

path = '/Applications/maude-darwin/maude.darwin64'
proc = Popen(path, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    
res = proc.stdin.write(b"red 3 .\n")
proc.stdin.flush()
outs = proc.stdout
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline().decode("utf-8"))

res = proc.stdin.write(b"red 4 .\n")
proc.stdin.flush()
res = proc.stdin.write(b"red 5 .\n")
proc.stdin.flush()
outs = proc.stdout
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())
print(outs.readline())


async def citp_mediator(websocket, path):
    path = '/Applications/maude-darwin/maude.darwin64'
    proc = Popen(path, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    
    
    outs, errs = proc.communicate(input=b"red 3 .\n", timeout=15)
    print(outs)
    print(errs)
#    while True:
#        now = datetime.datetime.utcnow().isoformat() + 'Z'
#        await websocket.send(now)
#        await asyncio.sleep(100)

# start_server = websockets.serve(citp_mediator, '127.0.0.1', 5678)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()