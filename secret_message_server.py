import sys
i, e, o = sys.stdin, sys.stderr, sys.stdout
from scapy.all import *
sys.stdin, sys.stderr, sys.stdout = i, e, o

__author__ = 'Gilad Barak'
__name__ = 'main'

IP_CURRENT = '172.16.1.104'
PORTS = [x for x in range(ord('A'), ord('Z'))] + ([y for y in range(ord('a'), ord('z'))])  # All optional ports
CONDITION = [(lambda pckt: 'UDP' in pckt), (lambda pckt: pckt[UDP].sport in PORTS)]


def filter_packets(pckt):
    """
    :param pckt: sniffed packet
    :return : True if pckt is in standards
    """
    for condition in CONDITION:
        if not condition(pckt):
            return False
    return True


