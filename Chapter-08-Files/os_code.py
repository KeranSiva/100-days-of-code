import os
import shelve

# Wrangling with path

os.path.join() # Joins String into system Path
os.getcwd() # Current Working Directory
os.chdir(path="") # Change folder to path
os.makedirs() # Create new folders

os.path.abspath('.') # Return absolute path
os.path.basename() # Returns filename
os.path.dirname() #Returns dir name
os.listdir() # Return list of files in the folder

os.path.exists() # Check if path exists
os.path.isdir() # Check if dir


# Wrangling with Files

hello_file = open(path=) # Opens File
hello_file.read() # Read File as single big string
hello_file.readlines() # Read file as lines
hello_file.readline() # Read file line by line

hello_file.write() # Write to file

# Saving Variables

shel_file = shelve.open('file_name')
shel_file = hello_file # Assining saves automatically to file
shel_file.close()