#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')


  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    id = data[4]
    year =data[6]
    major = data[7]

    studesnt_id = makeID(id, year, major) 
    output = id +"," + year + "," + major +"\n"
    outFile.write()
    #print(student_id)

    makeID("751417733", "FreshmanCivil", "Engineering") 
    


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(id_num, year, major):
  #print(id_num, year, major)
  idLen = len(idnum)

  while len(id_num) < 8:
    id_num = id_num + "x"

  id = id_num[0]+ "7"+ "freshmanCivil" + "733"


if __name__ == '__main__':
  main()
