import os 
path = "C:\\Users\\sande\\OneDrive\\Desktop\\PersonalProjects25"

if os.path.exists(path):
    print("The path exists")
    if os.path.isfile(path):
        print("The path is a file")
    elif os.path.isdir(path):
        print("The path is a directory")
else:
    print("The path does not exist")
# The os.path module provides a way to work with file and directory paths in a platform-independent manner.
# It allows you to check if a path exists, if it is a file or directory, and perform other operations related to file paths.