import os
import sys
import re

def main():
    _, path, substring, new_filename = sys.argv
    
    for filename in os.listdir(path):
        source = path + '/' + filename
        print('Before:', os.listdir(source))
        if os.path.isdir(source):
            rename_files_in_dir(source, substring, new_filename)
            print( 'After:', os.listdir(source) )
        elif os.path.isfile(source):
            rename_file(source, filename, substring, new_filename)
            print( 'After:', os.listdir(source) )

def rename_files_in_dir(source, substring, new_filename):
    for filename in os.listdir(source):
        if substring in filename:
            rename_file(source, filename, substring, new_filename)

def rename_file(source, filename, substring, new_filename):
    os.rename(source + '/' + filename, source + '/' + re.sub(substring, new_filename, filename))

if __name__ == '__main__':
    main()
