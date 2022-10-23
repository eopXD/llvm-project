#!/usr/bin/python3
import sys

def decode_uleb(bits):
  result = 0
  shift = 0
  while True:
    byte = bits.pop(0)
    result |= (byte & 0x7f) << shift
    shift += 7
    if byte & 0x80 == 0:
      break
  return result

def get_name(int_arr):
  ret = ''
  for ival in int_arr:
    ret += chr(ival)
  return ret

def parse_one_function(data):
  term_char = ord(',')
  sep = data.index(term_char)
  name = get_name(data[:sep])
  data = data[sep+1:]
  iws = decode_uleb(data)
  latency = decode_uleb(data)
  # print('{},{},{}'.format(name, iws, latency))
  data_str = '{},{},{}'.format(name, iws, latency)
  return data, data_str

out = open(sys.argv[2], "w")

with open(sys.argv[1], 'rb') as f:
  data = [ord(x) if int(sys.version[0]) < 3 else x for x in f.read()]
  while len(data) > 0:
    data, data_str = parse_one_function(data)
    out.write(data_str)
    out.write('\n')
