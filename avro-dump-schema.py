#!/usr/bin/python3
import sys
import getopt
import avro.datafile


def read_avro_schema(filename):
    reader = avro.datafile.DataFileReader(
        open(filename[0], "rb"), avro.io.DatumReader())
    print(reader.meta)


if __name__ == "__main__":
    read_avro_schema(sys.argv[1:])
