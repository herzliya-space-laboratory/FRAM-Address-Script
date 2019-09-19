import pandas as pd
import numpy as np

data = pd.read_csv("FRAM_Addresses.csv")

def print_Define(data, file_name):
    file = open(file_name, 'w')
    for row in range(1, len(data.index)):
        if(validNan(data["define address name"][row], data["End Addr.[hex] (not included)"][row])):
            if(len(data["End Addr.[hex] (not included)"][row]) == 1):
                define_row = "#define" + " " + str(data["define address name"][row]) + " 0x0" + str(data["End Addr.[hex] (not included)"][row])
                print(define_row)
                file.write("\n" + define_row + "\n")
            else:
                define_row = "#define " + str(data["define address name"][row]) + " 0x" + str(data["End Addr.[hex] (not included)"][row])    
                print(define_row)
                file.write("\n" + define_row + "\n")
    file.close()

def validNan(adrres_name, end_adrres):
        if (pd.notna(adrres_name) and pd.notna(end_adrres)):
            return True
        return False
    
print_Define(data, "file_Test.txt")