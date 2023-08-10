import csv

def read_family() -> list:
    """read family information from text file

    Returns:
        family (list): family information as list
    """
    with open("documents/family.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        family = list(reader)
    return family    
          
if __name__ == "__main__":
   print(read_family())
    
    
