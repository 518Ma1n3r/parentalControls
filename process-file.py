import json
import sys
import getopt
import re


def main(argv):
   inputfile = ''
#    outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
   except getopt.GetoptError:
      print ('process-file.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('process-file.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
#    print ('Output file is "', outputfile)

   return inputfile

if __name__ == "__main__":

    iFilePath = main(sys.argv[1:])

    newRows = []

    with open(iFilePath, 'r') as hostFile:
        for row in hostFile:
            # res = re.findall(r'(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))',row)
            newRows.append(str('0.0.0.0') + " " + str(row))
    

    newFilePath = iFilePath + '-hosts'

    with open(newFilePath, 'w') as filehandle:
        filehandle.writelines("%s\n" % row for row in newRows)

