# mysqldump_get_tabe
Extract one or more tables from mysql dump script

```
Usage: mysqldump_get_tabe.py [options]

Options:
  -h, --help            show this help message and exit
  -t TABLES, --tables=TABLES
                        tables for extract (split comma)
  -i FILE, --input=FILE
                        input file FILE [default: stdin]
  -o FILE, --output=FILE
                        output file FILE [default: stdout]
  -l FILE, --log=FILE   log file FILE [default: ]
  -c START_COMM, --start-comment=START_COMM
                        start comment for table struct (--|#|auto) [default:
                        auto]
  -g, --gzip            input gzipped
  -b, --bzip2           input bzipped
  -a, --autotar         input tar file with auto compression
  -q, --quiet           don't print status messages to stdout
  -v, --verbose         print verbose status messages to stdout
  --version             print version and license to stdout
```
