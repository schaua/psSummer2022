# Sprint 2 Challenge 
## Python Automation Challenge for Production Support

Python is frequently used to script toil (boring and repetitive tasks) that are sometimes part of Production Support.  For this challenge consider the need to clean up files on your own, or another machine.  The goal is to provide a robust tool for deleting these file.

>>> Do NOT actually delete any files.  

### Create a Python application to simulate the deletion of certain files based on path and size.
* Provide a default target directory and a default size filter
* Allow Linux like command line arguments for path and size (-p --path -s --size)
* Update the target directory and/or size filter with any provided values
* Step through the files in the target directory
* Print out a delete message for those files that exceed the size filter to simulate the deletion.  The application should display information about which files would have been deleted instead of actually deleting any files


### Stretch Goals
* Modify the program to accept an optional command line argument for pattern matching (-m --match)
* Use RegEx with the pattern option to only process files that match the pattern
* Add support for recursive processing (-r --recursive) that starts at the target directory
* Add support for "deleting" directories and their contents (-d --directory)
* Add support for different operatings systems use of / or \ as path delimiters
* Create a similar utility using Linux (hint research awk and find commands)

### Open Ended Goals:
* Consider what other toil type activities that would benefit from being automated
* Write a prototype to demonstrate

### Suggested References
There are many modules that could be used to solve this challenge.  As a starting point consider researching these two.  Feel free to discover other, possible better modules as well with your independent research.
* OS Module https://docs.python.org/3/library/os.html
* ArgParse Module https://docs.python.org/3/library/argparse.html
* Linux awk command https://www.gnu.org/software/gawk/manual/gawk.html
* Linux find command https://man7.org/linux/man-pages/man1/find.1.html
