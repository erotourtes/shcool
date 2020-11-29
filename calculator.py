from tkinter import *

def opp(op):
    global formula
    if op == "C":
        formula = "0"
    elif op == "DEL":
        formula = formula[0: -1]
    elif op == "X^2":
        formula = str((eval(formula))**2)
    elif op == "+/-":
        data = formula.split()
        if formula[0] != "-":
            data.insert(0, "-")
        else:
            formula.insert(0, "+")
        formula = ''.join(data)
    elif op == "=":
        try:
            formula = str(eval(formula))
        except ArithmeticError:
            out.config(bg = "RED")
        except SyntaxError:
            out.config(bg = "#ff4500")
        else:
            out.config(bg = "#1e90ff")
    else:
        if formula == "0":
                formula = ""
        formula += op
    if formula == "":
        formula = "0"
    out.config(text = formula)

formula = "0"
btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "+/-", "0", "%", "X^2"
        ]
but = []
root = Tk()
root.geometry("210x290")
root.resizable(width=False, height=False)
root.configure(bg="#dadada")

#make buttons
for el in btns:
    o = lambda x = el: opp(x)
    but.append(Button(root, text = el, width = 5, height = 2, command = o))

j = 1
for i in range(20):
    if ((i % 4 == 0) and (i != 0)):
        j += 1
    but[i].place(x = 12 + 46 * round(i % 4), y = 17 + j * 43)

#make label
out = Label (root, text = formula, bg = "#1e90ff", width = 25, height = 3)
out.place(x = 12, y = 5)
