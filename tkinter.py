from tkinter import *
import random

myRolls = []
rollTimes = 0
dieType = 0
top = Tk()
playlistList = []

def results():
    print(playlistList)

def addToList():
    newItem = E1.get()
    playlistList.append(newItem)
    E1.delete(0,END)

def exportList():
    with open('test.txt', 'w') as f:
        for item in playlistList:
            f.write("%s\n" % item)
            
def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "light blue", command = week1)
    B1Main.grid(column = 0, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "light blue", command = week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "light blue")
    B3Main.grid(column = 0, row = 4)

def week1():
    clearWindow()
    #This is a Label widget
    L1 = Label(top, text = "Playlist Maker")
    L1.grid(column = 0, row = 1)

    #This is a Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text = "    Print Playlist    ", bg = "#c6edee", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg = "#febee5", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "Export" , bg = "pink", command = exportList)
    B3.grid(column = 0, row = 4)

    BClear = Button(text = "Show Main Menu", bg = "Red", command = mainMenu)
    BClear.grid(column = 0, row = 5)

def week2():
    def rollDice():
        #update variable data
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        #clear window after updating
        clearWindow()
        #calculate dice rolls
        for x in range (0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
        #display dice rolls and present an exit buttn
        L4W2 = Label(top, text ="These are your rolls")
        L4W2.grid(column = 0, row = 1)
        L5W2 = Label(top, text="{}".format(myRolls))
        L5W2.grid(column = 0, row = 2)
        B2W2 =  Button(top, text = "Main Menu", command = mainMenu, bg = "red")
        B2W2.grid(column = 0, row = 3)
        
    clearWindow()
    L1W2 = Label(top, text="Dice Roller Program")
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text="How many sides")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text="How many rolls")
    L3W2.grid(column = 0 , row = 4)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column=0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 0, row = 5)

    B1W2 = Button(top, text="Press your luck",command = rollDice())
    B1W2.grid(column = 0, row = 6)
    
if __name__ == "__main__":
    mainMenu()

top.mainloop()
