#!/usr/bin/env python
# -*- coding: utf-8 -*-
u'''
Разбиение XML-я на куски
'''
from copy import deepcopy
import logging
from optparse import OptionParser
import os.path as osp
import sys

def main(opts):
  parse = start_parse
  tables = set(opts.tables)
  if not tables:
    return
  ofile = opts.ofile
  for line in opts.ifile:
    parse = parse(line, ofile, tables)
    if not parse:
      return

def start_parse(line, ofile, tables):
  if not line.startswith('-- Table structure for table '):
    return start_parse
  tbl = line.split('`')[1].lower()
  if tbl not in tables:
    return start_parse
  tables.remove(tbl)
  print>>ofile, line.rstrip()
  return copy_table

def copy_table(line, ofile, tables):
  if not line.startswith('-- Table structure for table '):
    print>>ofile, line.rstrip()
    return copy_table
  if not tables:
    return None
  return start_parse(line, ofile, tables)

def __parse_opt():
  parser = OptionParser(usage='usage: %prog [options] url or file')
  parser.add_option(
    "-t", "--tables", dest="tables",
    help="tables for extract (split comma) ")
  parser.add_option(
    "-i", "--input", dest="ifile", default="stdin",
    help="input file FILE [default: %default]", metavar="FILE")
  parser.add_option(
    "-o", "--output", dest="ofile", default="stdout",
    help="output file FILE [default: %default]", metavar="FILE")
  parser.add_option(
    "-l", "--log", dest="log", default="",
    help="log file FILE [default: %default]", metavar="FILE")
  parser.add_option(
    "-q", "--quiet", action="store_true", dest="quiet", default=False,
    help="don't print status messages to stdout")
  parser.add_option(
    '-v', '--verbose', action='store_true', dest='verbose', default=False,
    help='print verbose status messages to stdout')
  (opts, args) = parser.parse_args()
  opts.tables = frozenset(
    tbl.strip().lower() for tbl in opts.tables.split(','))
  opts.ifile = open(opts.ifile) if opts.ifile != 'stdin' else sys.stdin
  opts.ofile = open(opts.ofile, 'w') if opts.ofile != 'stdout' else sys.stdout
  return opts, args

def __init_log(opts):
  u'Настройка лога'
  format = '%(asctime)s %(levelname)-8s %(message)s'
  datefmt = '%Y-%m-%d %H:%M:%S'
  level = logging.DEBUG if opts.verbose else (
    logging.WARNING if opts.quiet else logging.INFO)
  logging.basicConfig(
    level=level,
    format=format, datefmt=datefmt)
  if not opts.log:
    return
  log = logging.FileHandler(opts.log, 'a', 'utf-8')
  log.setLevel(level) #logging.INFO) #DEBUG) #
  formatter = logging.Formatter(fmt=format, datefmt=datefmt)
  log.setFormatter(formatter)
  logging.getLogger('').addHandler(log)

if __name__ == '__main__':
  opts, args = __parse_opt()
  __init_log(opts)
  main(opts)
