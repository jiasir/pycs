__author__ = 'Taio'

from vulpo.scs.connection import SCSConnection
import sys
from keys import keys

k = keys.Keys()
access_key = k.get_access_key()
security_key = k.get_security_key()
conn = SCSConnection(access_key, security_key)
bn = sys.argv[1]
key = sys.argv[2]


def all_buckets():
    rs = conn.get_all_buckets()
    return rs


def bucket_name(name):
    return conn.get_bucket(name)


my_bucket = bucket_name(bn)


def delete_key(my_bucket, key):
    return my_bucket.delete_key(key)


def main():
    print 'Spaces:'
    for i in all_buckets():
        print i.name

    print 'delete key from: ', my_bucket.name
    delete_key(my_bucket, key)


if __name__ == '__main__':
    if len(sys.argv) is 3:
        main()
