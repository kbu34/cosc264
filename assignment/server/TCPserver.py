import socket
import sys
import os.path

HOST = '127.0.0.1'
PORT = int(sys.argv[1])

def readfilerequest(clisocket):
    data = bytearray(clisocket.recv(1024))
    if (data[0] << 8) | data[1] != 0x497E:
        print("Magic number error.")
        return -1, -1
    elif data[2] != 1:
        print("Packet type error.")
        return -1, -1
    elif (data[3] << 8) | data[4] > 1024:
        print("Name size error.")
        return -1, -1
    n = (data[3] << 8) | data[4]
    name = data[5:]
    while len(name) != n:
        data = bytearray(clisocket.recv(1024))
        name += data[5:]
    return name, n

def openfile(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

def fileresponse(validity, sock, content=''):
    if validity is True:
        content = bytearray(content, "utf-8")
        fileresponseheader = bytearray(((0x497E << 48) + (2 << 40) + (1 << 32) + len(content)).to_bytes(8, "big"))
        first = True
        bytecount = 0
        while len(content) >= 88 or first is True:
            pkt = fileresponseheader + content[:88]
            sock.sendall(pkt)
            content = content[88:]
            first = False
            bytecount += len(pkt)
        if len(content) != 0:
            pkt2 = fileresponseheader + content
            sock.sendall(pkt2)
            bytecount += len(pkt2)
        print(bytecount, "bytes sent.\n")
        return bytecount
    else:
        sock.sendall(bytearray(((0x497E << 48) + (2 << 40) + (0 << 32) + len(content)).to_bytes(8, "big")))
        print("The file does not exist or cannot be opened.")

def server(port):
    if port <= 1024 or port >= 64000:
        print("Invalid port number.")
        sys.exit(0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((HOST, port))
    except:
        print("Binding failed.")
        sys.exit(0)
    try:
        sock.listen()
    except:
        print("Listening failed.")
        sys.exit(0)
    loop = 0
    while loop == 0:
        clisocket, cliip = sock.accept()
        print("Connected to", cliip[0])
        
        try:
            dataarray, n = readfilerequest(clisocket)
            if dataarray != -1:
                filename = dataarray.decode("utf-8")
                print("File name", filename)
                if len(dataarray) != n:
                    print("Data does not match the actual name size.")
                    clisocket.close()
                if os.path.exists(filename):
                    print("File found.")
                    content = openfile(filename)
                    bytecount = fileresponse(True, clisocket, content)
                    clisocket.close()    
                else:
                    print("file does not exist.")
                    fileresponse(False, clisocket)
                    clisocket.close()
            else:
                clisocket.close()
        except:
            fileresponse(False, clisocket)
            clisocket.close()
            


server(PORT)