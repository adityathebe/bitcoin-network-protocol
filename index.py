import struct
import codecs
import socket

from message_utils import make_version_msg, make_ping_msg, make_tx_msg

# Almost all integers are encoded in little endian. Only IP or port number are encoded big endian.

host = '35.173.57.227'
port = 8333


if __name__ == "__main__":
    # Establish the tcp connection
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))

    # Get the version msg
    # version_msg = make_version_msg()
    # print("version message", codecs.encode(version_msg, 'hex'))

    # Get ping msg
    # ping_msg = make_ping_msg()
    # print("ping message", codecs.encode(ping_msg, 'hex'))

    # Signed transaction
    tx_msg = make_tx_msg(codecs.decode("0100000001484d40d45b9ea0d652fca8258ab7caa42541eb52975857f96fb50cd732c8b481000000008a47304402202cb265bf10707bf49346c3515dd3d16fc454618c58ec0a0ff448a676c54ff71302206c6624d762a1fcef4618284ead8f08678ac05b13c84235f1654e6ad168233e8201410414e301b2328f17442c0b8310d787bf3d8a404cfbd0704f135b6ad4b2d3ee751310f981926e53a6e8c39bd7d3fefd576c543cce493cbac06388f2651d1aacbfcdffffffff0162640100000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac00000000", 'hex'))
    print("Tx message", codecs.encode(tx_msg, 'hex'))

    # Send that over the tcp socket
    clientsocket.send(tx_msg)

    msg = clientsocket.recv(1024)
    print(f"Bytes Length: {len(msg)}\nResponse: {codecs.encode(msg, 'hex')}")
