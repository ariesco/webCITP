# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from subprocess import Popen, PIPE, STDOUT

from websocket_server import WebsocketServer

#==============================================================================   
# res = proc.stdin.write(b"red 3 .\n")
# proc.stdin.flush()
# outs = proc.stdout
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline().decode("utf-8"))
# 
# res = proc.stdin.write(b"red 4 .\n")
# proc.stdin.flush()
# res = proc.stdin.write(b"red 5 .\n")
# proc.stdin.flush()
# outs = proc.stdout
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
# print(outs.readline())
#==============================================================================

#==============================================================================
# async def citp_mediator(ws, path):
#     path = '/Applications/maude-darwin/maude.darwin64'
#     proc = Popen(path, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
#     clean_header(proc)
#     
#     while True:
#     
#         msg = await ws.recv()
#         msg_bytes = bytes(msg, "utf-8")
#     
# #==============================================================================
# #         proc.stdin.write(msg_bytes)
# #         proc.stdin.flush()
# #     
# #         outs = proc.stdout
# #         print(outs.readline())
# #==============================================================================
#     
#         print("Received '%s'" % msg)
#     
#     
# 
#==============================================================================
#    while True:
#        now = datetime.datetime.utcnow().isoformat() + 'Z'
#        await ws.send(now)
#        await asyncio.sleep(100)


def clean_header(maude):
    outs = maude.stdout
    for i in range(9):
        print(outs.readline())

# Called for every client connecting (after handshake)
def new_client(client, server):
    add = client['address'][0]
    if not (add in maude_dict):
        path = '/Applications/maude-darwin/maude.darwin64'
        maude = Popen(path, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        maude.stdin.write(b"load /Users/adrian/Documents/Maude/webCITP/citp.maude\n")
        maude.stdin.flush()
        clean_header(maude)
        maude_dict[add] = maude
        print("Nuevo")

# Called for every client disconnecting
def client_left(client, server):
    print("Cerrado")

# Called when a client sends a message
def message_received(client, server, msg):
    msg.replace("\r\n", "\n")
    msg_bytes = bytes(msg, "utf-8")
    add = client['address'][0]
    maude = maude_dict[add]
    print(msg)
#==============================================================================
    maude.stdin.write(msg_bytes)
    maude.stdin.flush()
    maude.stdin.write(b"\n")
    maude.stdin.flush()
    maude.stdin.write(b"red 3 .\n")
    maude.stdin.flush()
    outs = maude.stdout
    print(outs.readline())
    print(outs.readline())
#==============================================================================


maude_dict = {}


PORT = 5678
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()