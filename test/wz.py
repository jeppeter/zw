#! python


import zipfile
import sys
import os


def main():
	f = zipfile.ZipFile(sys.argv[1],'w')
	for s in sys.argv[2:]:
		f.write(s)
 
if __name__ == '__main__':
	if len(sys.argv) < 3 :
		sys.stderr.write('%s zip files...\n'%(sys.argv[0]))
	main()
