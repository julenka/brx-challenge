#!/usr/bin/env python
import array
import sys

def read_bytes(f):
	result = array.array('l')
	while True:
		try:
			result.fromfile(f, 1000)
		except EOFError:
			break;
	return result

def main():
	if len(sys.argv) <= 1:
		print "usage: {} path".format(sys.argv[0])
		sys.exit(1)
	filepath = sys.argv[1]
	with open(filepath) as f:
		bts = read_bytes(f)
		print len(bts)

if __name__ == '__main__':
	main()