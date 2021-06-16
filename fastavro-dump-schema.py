#!/usr/bin/python3
import sys
import getopt
from fastavro import reader


def read_avro_schema(filename):
    with open(filename[0], 'rb') as fo:
        avro_reader = reader(fo)
    print(avro_reader.schema)


if __name__ == "__main__":
    read_avro_schema(sys.argv[1:])
