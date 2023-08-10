def calculateExtras(generations: list) -> list:
    """Calculates extra } to be added if generation decreases

    Args:
        generations (list): generation of family tree member

    Returns:
       extras (list): extra } to be added in tex file
    """
    extras = []
    for i in range(1, len(generations)):
        if generations[i]<generations[i-1]:
            extras.append(i-1)
    return extras  

def generate_tex(names: list, genders: list, generations: list) -> None:
    """Generates tex file

    Args:
        names (list): names in family tree
        genders (list): genders in family tree
        generations (list): generations in family tree
    """
    extras = calculateExtras(generations)
    with open("documents\example.gauss.graph.tex", "w") as f:
        f.write("sandclock{ \n \t child{\n")
        f.write("\t\t")
        f.write(r"g{")
        f.write("\n")
        f.write("\t\t")
        if genders[0] == "male":
            f.write("male,") 
        else:
            f.write("female,")             
        f.write("\n")
        f.write("\t\t")
        f.write(r"name={\pref{")
        f.write(f"{names[0]}")
        f.write(r"}}")
        f.write("\n")
        f.write("\t\t}\n")
        f.write("\t}\n")
        for i in range(1, len(names)):
            f.write("\t")
            f.write(r"parent{")
            f.write("\n")
            f.write("\t\t")
            f.write(r"g{")
            f.write("\n")
            f.write("\t\t")
            if genders[i] == "male":
                f.write("male,") 
            else:
                f.write("female,")                       
            f.write("\n")
            f.write("\t\t")
            f.write(r"name={\pref{")
            f.write(f"{names[i]}")
            f.write(r"}")
            f.write("\n")
            if i in extras:
                f.write(r"}") 
            for _ in range(generations[i]+1):
                f.write(r"}") 
                    
        for _ in range(max(generations)):             
            f.write(r"}")
            
if __name__ == "__main__":
    pass