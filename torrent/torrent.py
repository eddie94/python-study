from hashlib import md5, sha1
from random import choice
import socket
from struct import pack, unpack
from threading import Thread
from time import sleep, time
import types
from urllib.request import urlopen
from urllib.parse import urlencode
from torrent.util import collapse, slice
from torrent.bencode import decode, encode

CLIENT_NAME = 'pytorrent'
CLIENT_ID = 'PY'
CLIENT_VERSION = '0001'

def make_info_dict(file):

    with open(file) as f:
        contents = f.read()

    piece_length = 524288

    info = {}

    info['piece length'] = piece_length
    info['length'] = len(contents)
    info['name'] = file
    info['md5sum'] = md5(contents).hexdigest()

    pieces = slice(contents,piece_length)
    pieces = [sha1(p).digest() for p in pieces]
    info['pieces'] = collapse(pieces)

    return info

def make_torrent_file(file = None, tracker=None, comment=None):
    pass