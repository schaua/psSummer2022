#1//usr/bin/python
import os
from argparse import ArgumentParser

# define starting directory and max file size
# either from commmand line arguments or

# default the path to the current working directory
pathDelimiter = '\\' # windows path delimiter
initialPath = os.getcwd() + pathDelimiter

# default the max size to 5GB
sizeLimit = int(5000000 * 1024)

def readCommandLine():
    # Allow the global variables to be updated in this function
    global sizeLimit
    global initialPath
   
    # ArgumentParser adds automatic support of -h and --help
    # and to add arguments that 
    parser = ArgumentParser()
    parser.add_argument("-p", "--path", dest="myDir", help="Open specified directory")
    parser.add_argument("-s", "--size", dest="mySize", help="Process files larger than this")
    args = parser.parse_args()

    if args.myDir :
        initialPath = args.myDir + pathDelimiter
    if args.mySize:
        sizeLimit = int(args.mySize)
        

def processFiles(): # using the global functions to specify path and size
    print(f'\n\nProcessing files in {initialPath}:')
    
    # get all the files from the specified path
    files = os.listdir(initialPath)
    # step through the files 
    for file in files:
        filepath = initialPath + file
        file_size = os.path.getsize(filepath)
        # and only "delete" those that meet the size criteria
        if file_size >= sizeLimit:
            print(f'Deleting {file} with size: {file_size} bytes')

def main():
    readCommandLine()
    processFiles()

if __name__ == "__main__":
    main()