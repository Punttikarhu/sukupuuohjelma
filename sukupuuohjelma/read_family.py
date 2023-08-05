import csv

def read_family():
    with open("documents/family.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        family = list(reader)
    return family    
          
if __name__ == "__main__":
   print(read_family())
    
    
