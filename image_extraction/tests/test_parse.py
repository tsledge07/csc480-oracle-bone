from parse import parser

document = "table_p1.pdf"
with open(document, 'rb') as f:
    p = parser(f)
    p.readPage(0)
    print(p.getTextInPercentArea(0.4266129032258065, 0.07210031347962383, 0.5282258064516129, 0.09318894271872329))
