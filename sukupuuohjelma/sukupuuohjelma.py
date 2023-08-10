import os, sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from generate_familytree import generate_familytree
from anytree import PreOrderIter
from generate_tex import generate_tex
from GUI import GUI
        
if __name__ == "__main__":
    """starts the program
    """
    
    root = generate_familytree()
    names = [node.name for node in PreOrderIter(root)]
    genders = [node.gender for node in PreOrderIter(root)]
    generations = [node.generation for node in PreOrderIter(root)]
    generate_tex(names, genders, generations)
    os.system('cmd /c "pdflatex --enable-write18 --extra-mem-bot=10000000 --synctex=1 documents/family_tree_test.tex"')
    
    app = QApplication(sys.argv)

    window = GUI()
    window.show()
    window.webView.setUrl(QUrl.fromLocalFile(r"C:\Users\janne\sukupuuohjelma\family_tree_test.pdf"))
    sys.exit(app.exec())	