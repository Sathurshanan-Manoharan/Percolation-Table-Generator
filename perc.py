#Importing Modules
import random
import sys
from prettytable import PrettyTable
from prettytable import SINGLE_BORDER
from time import gmtime, strftime
from datetime import datetime
date = datetime.now()
table = PrettyTable([])
table.set_style(SINGLE_BORDER)
table.hrules = 1
table.header = 0
row = 5
column = 5

#Checking for percolation and writing OK,NO to the text file and creating HTML file
def percolation( row, column):
    global file , table , Grid ,fileName , date
    output = []
    htmFile = date.strftime('%d-%m-%Y-%H-%M-%S.html')
    file = open("Grid"+ fileName +".txt", "a+")
    for i in range(column):
        space = True
        for j in range(row):
            if Grid[j][i] == "  ":
                no = "NO"
                output.append(no)
                file.write("NO")
                file.write(" ")
                space = False
                break
        if space:
            ok = "OK"
            output.append(ok)
            file.write("OK")
            file.write(" ")
    table.add_row([*output])
    print (table)
    with open(htmFile,"w") as out:
        out.write(table.get_html_string(format=True))
    file.close()
    
#Creating the grid and writing them to the text file
def grid(row, column):
    global file, table , Grid , fileName ,date_time
    fileName = strftime("%Y-%m-%d %H-%M-%S", gmtime())
    file = open("Grid"+ fileName +".txt", "w")
    numbers = list(range(10, 100))
    space = ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]
    numbers.extend(space)
    Grid = []
    for i in range(row):
        outputs = []
        for j in range(column):
            outputs.append(random.choice(numbers))
        table.add_row([*outputs])
        for x in outputs:
            file.write(str(x))
            file.write(" ")
        file.write("\n")
        Grid.append(outputs)
    percolation(row,column)

#Getting user input as argument and checking for errors
def arg(row, column):
        if len(sys.argv) == 1:
                grid(row, column)
        else:
                try:
                        dim = str(sys.argv[1]).split("x")
                        row = int(dim[0])
                        column = int(dim[1])
                        if not (3 <= row <= 9) or not (3 <= column <= 9):
                                print ("Invalid value! value for the dimension must be inbetween 3 to 9 in this format - nxn ")
                                exit()
                        else:
                                grid(row, column)
                except ValueError :
                        print ("Invalid value!")
                        exit()
                except IndexError :
                        print ("Invalid value!")
                        exit()
 
#Starting the program
arg(row,column)