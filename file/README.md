prettifier.py
=============
Script that can help beautify a JSON or XML file or convert it into a single line of data

usage: prettifier.py [-h] (-j | -x) (-b | -c) -i IFILE [-o OFILE]

optional arguments:
  -h, --help            show this help message and exit
  -j, --json            Input is of JSON format
  -x, --xml             Input is of XML
  -b, --beautify        beautify the output
  -c, --compress        compress the output
  -i IFILE, --ifile IFILE
                        Input file to pick data from
  -o OFILE, --ofile OFILE
                        Output file to place data in, default destination
                        SCREEN
