# import xlwt
# from pandas import DataFrame
import pandas as pd
import os
import requests

path = '../../_data_tmp/W3SVC2/'
data = []

def read_file(file): 
    data_t = []
    bad_words = ['#Software','#Version','#Date','#Fields']
    with open(path + file) as oldfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                row = line.split()
                data_t.append(row)
    return data_t

def read_files(): 
    global data
    files = os.listdir(path)
    for i in range(len(files)): 
        if files[i].startswith("u_ex"): 
            print(files[i])
            data = data + read_file(files[i])
            #create_excel(files[i])
    print("end")

def fill_pandas():
    for dat in data: 
        print(len(dat))


# main    
if __name__ == '__main__':
    read_files()
    fill_pandas()