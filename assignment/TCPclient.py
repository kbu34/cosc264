import socket
import sys
import os.path

if len(sys.argv) != 4:
    print("parameter error")
    sys.exit(0)

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
FILENAME = str(sys.argv[3])
    
def readdata(sock):
    initdata = bytearray(sock.recv(1024))
    bytecount = 0
    if (initdata[0] << 8) | initdata[1] != 0x497E:
        print("Magic number error.")
        sys.exit(0)
    elif initdata[2] != 2:
        print("Packet type error.") 
        sys.exit(0)
    elif initdata[3] != 1:
        print("file not found.")
        sys.exit(0)
    else:
        contentlen = ((initdata[4] << 24) | (initdata[5] << 16) | (initdata[6] << 8) | initdata[7]) 
        content = initdata[8:]
        bytecount += len(initdata)
        data = bytearray(sock.recv(1024))
        while len(data) != 0:
            bytecount += len(data)
            content += data[8:]
            data = bytearray(sock.recv(1024))
        print("Received data")
        if len(content) != contentlen:
            print("file length does not match the length.")
            return -1
        else:
            print(bytecount, "bytes received.")
            return content
        
def client(host, port, filename):
    try:
        info = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
        ipv4 = info[-1]
        ipport = ipv4[-1]
        ip, num = ipport
    except:
        print("invalid address.")
        sys.exit(0)
    if port <= 1024 or port >= 64000:
        print("Invalid port number.")
        sys.exit(0)    
    elif os.path.exists(filename):
        print("File already exists.")
        sys.exit(0)
    else:
        try:
            csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            csock.settimeout(2)
        except:
            print("Socket creation failed.")
            sys.exit(0)
        try:
            csock.connect((host, port))
            print("connected")
        except:
            csock.close()
            print("socket error")
            sys.exit(0)
        name = bytearray(filename.encode("utf-8"))
        nameleng = len(name)
        if nameleng < 1024:
            filerequest = bytearray(((0x497E << (24)) + (1 << (16)) + (nameleng)).to_bytes(5, "big"))
            filerequest += name
            csock.sendall(filerequest)
            content = readdata(csock)
            if content != -1:
                decoded = content.decode('utf-8')
                file = open(filename, "w")
                file.write(decoded)
                file.close()
    sys.exit(0)
        
        
client(HOST, PORT, FILENAME)