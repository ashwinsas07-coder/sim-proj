import csv 

with open("c:/Users/Aswin/Downloads/salary-dataset (1).csv", "r" , encoding="latin-1") as file: 
reader = csv.reader(file) 
for row in reader: 
print(row)