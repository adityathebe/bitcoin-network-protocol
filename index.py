import struct
import codecs
import socket

from message_utils import make_version_msg, make_ping_msg

# Almost all integers are encoded in little endian. Only IP or port number are encoded big endian.

host = '35.173.57.227'
port = 8333


if __name__ == "__main__":
    # Establish the tcp connection

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))

    # Get the version msg
    version_msg = make_version_msg()
    print("version message", codecs.encode(version_msg, 'hex'))

    # Get ping msg
    # ping_msg = make_ping_msg()
    # print("ping message", codecs.encode(ping_msg, 'hex'))

    # Send that over the tcp socket
    clientsocket.send(version_msg)

    msg = clientsocket.recv(1024)
    print(f"Bytes Length: {len(msg)}\nResponse: {codecs.encode(msg, 'hex')}")
