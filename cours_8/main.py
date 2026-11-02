# classic library import
import os
import sys

# get folder of current file
# __file__ = current file
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path)

# add absolute folder path to python path, so that it can detect the library
sys.path.append(absolute_folder_path)

from ui import MyClass

def my_func():
    absolute_path = os.path.abspath(os.path.curdir)
    print(absolute_path)

my_class = MyClass()
my_class.print_variable() 

