# -*- coding: utf-8 -*-
import socket
import hashlib,base64
import struct

HOST = 'localhost'
PORT = 8008
MAGIC_STRING = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
HANDSHAKE_STRING = "HTTP/1.1 101 Switching Protocols\r\n" \
      "Upgrade: websocket\r\n" \
      "Connection: Upgrade\r\n" \
      "Sec-WebSocket-Accept: {1}\r\n" \
      "Sec-WebSocket-Origin: null\r\n" \
      "Sec-WebSocket-Location: ws://{2}/chat\r\n" \
      "WebSocket-Protocol: chat\r\n\r\n"

def main():
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("create socket suc!")
        
        sock.bind((HOST,PORT))
        print('bind socket suc!')
 
        sock.listen(5)
        print('listen socket suc!')      
        
    except:
        print("init socket err!")
        con.close()
        
    while True:
        print('listren for client...')
        con,addr = sock.accept()
        print('get client')
        print('addr',addr)
        if handshake(con):
            print('handshake success')
        

def handshake(con):
    headers = {}
    shake = con.recv(1024)

    if not len(shake):
        return false

    header,data = shake.decode('utf-8').split('\r\n\r\n',1)
    for line in header.split('\r\n')[1:]:
        key,val = line.split(':',1)
        headers[key] = val

    if 'Sec-WebSocket-Key' not in headers:
         print('This socket is nor websocket,client close')
         con.close()
         return False    

    sec_key = headers['Sec-WebSocket-Key']
    print('sec_key',sec_key)
    encodeKey = str.encode(sec_key + MAGIC_STRING)
    res_key = base64.b64encode(hashlib.sha1(encodeKey).digest())
    print('res_key',res_key)  
    str_handshake = HANDSHAKE_STRING.replace('{1}', bytes.decode(res_key)).replace('{2}', HOST + ':' + str(PORT))
    print('str_handshake',str_handshake)
    con.send(str_handshake.encode())
    return True          



if "__main__" == __name__: 
    main()




