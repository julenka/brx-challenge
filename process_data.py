#!/usr/bin/env python
import array
import datetime
import os
import sys

def get_outdir():
    out_dir = os.path.join("out", datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    return out_dir

def get_outpath(out_dir, in_path):
    in_file = os.path.basename(in_path)
    return os.path.join(out_dir, in_file)

def read_doubles(f):
    result = array.array('L')
    while True:
        try:
            result.fromfile(f, 1000)
        except EOFError:
            break
    return result

def trim_doubles(count, arr):
    for _ in xrange(count):
        arr.pop(0)
    return arr

def xor_bytes(to_xor, data_array):
    result_array = array.array('L')
    for data_double in data_array:
        xor_result = data_double ^ to_xor
        result_array.append(xor_result)
    return result_array

def process_file_path(out_dir, file_path):
    out_path = get_outpath(out_dir, file_path)
    with open(file_path) as in_file:
        with open(out_path, 'w') as out_file:
            bts = read_doubles(in_file)
            bts = trim_doubles(8, bts)
            bts = xor_bytes(0xb8b1a8beb6aaffb7, bts)
            bts.tofile(out_file)

def main():
    if len(sys.argv) <= 1:
        print "usage: {} path".format(sys.argv[0])
        sys.exit(1)
    file_paths = sys.argv[1:]
    out_dir = get_outdir()
    for file_path in file_paths:
        process_file_path(out_dir,file_path)

if __name__ == '__main__':
    main()
