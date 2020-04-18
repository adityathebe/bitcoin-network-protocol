import socket
import struct


def get_net_addr(host, port):
    services = 1
    ipv4 = socket.inet_aton(host)
    return struct.pack('<Q8s8sH', services, b'0', ipv4, port)
