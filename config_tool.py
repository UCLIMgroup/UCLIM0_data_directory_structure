''' Module to run the main code of the tool.'''

# -*- coding: utf-8 -*-

#%%
#Function to read the path to the #Data folder
def read_first_line(file_path):
    '''
    Reads the first line of a file and returns it as a string, removing any leading/trailing quotes.
    '''
    with open(file_path, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
    # Remove leading/trailing quotes if present
    cleaned_line = first_line.strip('\'"')
    return cleaned_line

#Data folder
#read first line of *.txt file with name path_to_data
cwd_data = read_first_line('path_to_data.txt')
