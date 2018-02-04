#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Atieno
#
# Created:     22/05/2017
# Copyright:   (c) Atieno 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from math import*
from csv import*
import os
import shutil
os.chdir('C:\\Portable Python 3.2.5.1\\temp')
from pandas import DataFrame, read_csv
csv_data = read_csv("sample_assess2.csv")
print(csv_data[0:])
print(csv_data.head())
print(csv_data.dtypes)
print(csv_data['j_id'].max())
print(csv_data['j_id'].plot())
if csv_data['j_id'].any==4:
    print("j_id has 4")

import math
everything = dir(math)
print (everything)