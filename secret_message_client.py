import argparse
import sys
i, e, o = sys.stdin, sys.stderr, sys.stdout
from scapy.all import *
sys.stdin, sys.stderr, sys.stdout = i, e, o

__author__ = 'Gilad Barak'
__name__ = 'main'

IP_CURRENT = '172.16.1.3'
IP_SERVER = '172.16.1.104'
PORT = 3899
RAW = ''


def send_empty_to_port(given_port):
    """
    :param given_port: port number for packet to be sent to
    :return : true if process was successful otherwise false
    """
    ip_layer = IP(src=IP_CURRENT, dst=IP_SERVER)
    udp_layer = UDP(sport=PORT, dport=given_port)
    packet_send = ip_layer / udp_layer / RAW
    try:
        send(packet_send)
        return True
    finally:
        return False


def send_message(message):
    """
    :param message: message given by user as input
    :return : true if process was successful otherwise false
    """
    for port in message:
        if not send_empty_to_port(ord(port)):
            return False
    return True


def get_message_from_user():
    """
    :return : message from user given by input
    """
    parser = argparse.ArgumentParser(description='Gets message from user as input.')
    parser.add_argument('message', help="Enter message to send secretly.")
    parsed = parser.parse_args()

    return parsed.message


def main():
    user_message = get_message_from_user()
    send_message(user_message)

if __name__ is 'main':
    main()