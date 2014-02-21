#!/usr/bin/python

import sys
import os.path
import argparse
import json
import xml.dom.minidom

def param():
	parser = argparse.ArgumentParser()
	group_jx = parser.add_mutually_exclusive_group(required=True)
	group_jx.add_argument('-j', '--json', default=False, action='store_true', help='Input is of JSON format')
	group_jx.add_argument('-x', '--xml',  default=False, action='store_true', help='Input is of XML')
	group_bc = parser.add_mutually_exclusive_group(required=True)
	group_bc.add_argument('-b', '--beautify', default=False, action='store_true', help='beautify the output')
	group_bc.add_argument('-c', '--compress', default=False, action='store_true', help='compress the output')
	parser.add_argument('-i', '--ifile', default=None, required=True, help='Input file to pick data from');
	parser.add_argument('-o', '--ofile', default=None, help='Output file to place data in, default destination SCREEN');
	
	largs = parser.parse_args()
	return largs;

def userNotify(args):
	userNotify="";
	if (args.beautify == True):
		userNotify += "Beautifying ";
	else:
		userNotify += "Compressing ";

	if (args.json == True):
		userNotify += "JSON in ";
	else:
		userNotify += "XML in ";

	userNotify += "'" + args.ifile + "' to ";

	if (args.ofile == None):
		userNotify += "SCREEN"
	else:
		userNotify += "'" + args.ofile + "'" ;

	return userNotify;


def formatJson(infile, outfile, beautify):
	json_ip = open(infile)
	json_data = json.load(json_ip)

	if (outfile == None):
		out = sys.stdout
	else:
		out = open(outfile, 'w')
	try:
		if (beautify):
			out.write(json.dumps(json_data, indent=4, separators=(',', ': ')) + '\n')
		else:
			out.write(json.dumps(json_data) + '\n')
	finally:
		if (outfile != None):
			out.close


def formatXml(infile, outfile, beautify):
	xml_ip = open(infile)
	xml_data = xml.dom.minidom.parse(xml_ip)

	op_to_file = ''
	if (beautify):
		op_to_file = xml_data.toprettyxml(indent="\t")
		op_to_file = removeEmptyLines(op_to_file)
	else:
		op_to_file = xml_data.toprettyxml(indent="")
		op_to_file = removeEmptyLines(op_to_file)
		op_to_file = convertToSingleLine(op_to_file)

	if (outfile == None):
		out = sys.stdout
	else:
		out = open(outfile, 'w')
	
	try:
		out.write(op_to_file + '\n')
	finally:
		out.close


def removeEmptyLines(ip):
	ip_arr = ip.split("\n")
	op = ''
	for line in ip_arr:
		if line.strip():
			op += line + "\n"
	return op;


def convertToSingleLine(ip):
	ip_arr = ip.split("\n")
	op = ''
	for line in ip_arr:
		op += line
	return op;


def main():
	args = param();

	if(not os.path.exists(args.ifile)):
		print "Input File '" + args.ifile + "' does not exists";
		exit(1);

	sys.stderr.write(userNotify(args) + '\n')
	if (args.json):
		formatJson(args.ifile, args.ofile, args.beautify)
	else:
		formatXml(args.ifile, args.ofile, args.beautify)


if __name__ == '__main__':
	main()

