import os
import shutil

path = "folder"

try:
    #os.remove(path)        delete a file
    #os.rmdir(path)         delete an empty directory
    #shutil.rmtree(path)    delete a directory containing files
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delee hat using that function")
else:
    print("Path was deleted")
