import pyasn
import os

'''
parpare work
First:download v6 AS and BGP repository
    pyasn_util_download.py --latestv6
then:Parse out the AS and BGP repository
    pyasn_util_convert.py --single <Downloaded RIB File> <ipasn_db_file_name>
    eg:pyasn_util_convert.py --single rib.20190924.0600.bz2 ipasn.dat.dat
'''

ansdb=pyasn.pyasn(<ipasn_db_file_name>)
# ip2as inquire
def ip2as(IPv6):
    
    as_number=ansdb.lookup(IPv6)[0]
    return as_number

# ip2bgp inquire
def ip2bgp(IPv6):
    bgp=ansdb.lookup(IPv6)[1]
    return bgp
