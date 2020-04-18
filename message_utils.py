import random
import struct
import hashlib
import codecs
import time
from hashlib import sha256

from utils import get_net_addr


magic = 0xD9B4BEF9  # main net


def make_message(cmd, payload):
    payload_hash = sha256(sha256(payload).digest()).digest()
    checksum = payload_hash[:4]

    return struct.pack('<L12sL4s', magic, codecs.encode(cmd, 'ascii'), len(payload), checksum) + payload


def make_ping_msg():
    payload = struct.pack('<Q', random.randint(0, 1000000))
    return make_message('ping', payload)


def make_tx_msg(signed_transaction):
    return make_message('tx', signed_transaction)


def make_version_msg():
    version = 70015
    services = 1
    timestamp = int(time.time())
    addr_recv = get_net_addr('127.0.0.1', 8333)
    addr_from = get_net_addr('127.0.0.1', 8333)
    nonce = random.randint(0, 10000000)
    user_agent = 0x00
    start_height = 0
    relay = 1

    payload = struct.pack('<LQQQ26s26sbL?', version, services, timestamp,
                          nonce, addr_recv, addr_from, user_agent, start_height, relay)
    return make_message('version', payload)
