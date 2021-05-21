from tkinter import *
import random
myList = []
unique_list = []
NewSorted = []
myRolls = []
rollTimes = 0
dieType = 0
top = Tk()
playlistList = []

            
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
    
    B3Main = Button(text = "Week 3", bg = "light blue", command = week3)
    B3Main.grid(column = 0, row = 4)

def week1():
    clearWindow()
    #This is a Label widget
    L1 = Label(top, text = "Playlist Maker")
    L1.grid(column = 0, row = 1)

    #This is a Entry widget
    E1W1 = Entry(top, bd = 5)
    E1W1.grid(column = 0, row = 2)
    print("E1W1")

    #This is a Button widget
    B1 = Button(text = "    Print Playlist    ", bg = "#c6edee", command = results)
    B1.grid(column = 0, row = 3)
    
    def addToPlayList():
        newItem = E1W1.get()
        playlistList.append(newItem)
        E1W1.delete(0,END)
        
    B2 = Button(text = " + ", bg = "#febee5", command = addToPlayList)
    B2.grid(column = 1, row = 2)


    B3 = Button(text = "Export" , bg = "pink", command = exportList)
    B3.grid(column = 0, row = 4)

    BClear = Button(text = "Show Main Menu", bg = "Red", command = mainMenu)
    BClear.grid(column = 0, row = 5)
def results():
    print(playlistList)



def exportList():
    with open('test.txt', 'w') as f:
        for item in playlistList:
            f.write("%s\n" % item)

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
        L4W2.grid(column = 0, row = 0)
        L5W2 = Label(top, text="{}".format(str(myRolls)[1:-1]),wraplength = 50, justify = LEFT)
        L5W2.grid(column = 0, row = 1)
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

    B1W2 = Button(top, text="Press your luck",command = rollDice)
    B1W2.grid(column = 0, row = 6)
    
def week3():
    print("Hello, there! Let's work with lists!")
    clearWindow()
    B1W3 = Button(top, text="Add to List", command = addToList)
    B1W3.grid(column = 0, row = 1)
    
    B2W3 = Button(top, text = "Return the value of an index position", command = indexValues)
    B2W3.grid(column = 0, row = 2)
    
    B3W3 = Button(top, text="Random Search",command = randomSearch)
    B3W3.grid(column = 0, row = 3)
     
    B4W3 = Button(top, text="Add a bunch of numbers",command=addABunch)
    B4W3.grid(column = 0, row = 4)
    
    B5W3 = Button(top, text="Sort Your List",command = sortListAsk)
    B5W3.grid(column = 0, row = 5)
    
    B6W3 = Button(top, text="Do a Linear search",command = linearSearch)
    B6W3.grid(column = 0, row = 6)
    
    B7W3 = Button(top, text="Recursive Binary Search",command = recursiveBinarySearch)
    B7W3.grid(column = 0, row = 7)
    
    
    B8W3 = Button(top, text="Iterative Binary Search")
    B8W3.grid(column = 0, row = 8)

    B9W3 = Button(top, text="Print Your List",command = printLists)
    B9W3.grid(column = 0, row = 9)

    B10W3 = Button(top, text="Make a new Sorted List")
    B10W3.grid(column = 0, row = 10)

    B11W3 = Button(top, text="Exit Window")
    B11W3.grid(column = 0, row = 11)

"""
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch()
        elif choice == "4":
            addABunch()
        elif choice == "5":
            sortListAsk(myList)
        elif choice == "6":
            linearSearch()
        elif choice == "7":
            binSearch = input("What number are you looking for?   ")
            sortList(myList)
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
        elif choice == "8":
            startIterative = time.time()
            sortList(myList)
            binSearch = input("What number are you looking for?   ")
            result = iterativeBinarySearch(unique_list, int(binSearch))
            if result != -1 :
                endIterative = time.time()
                lengthIterative = endIterative - startIterative
                print("Your number is at index position {}".format(result))
                print("Your search took {} seconds".format(lengthIterative))
            else:
                endIterative = time.time()
                lengthIterative = endIterative - startIterative
                print("Your number isn't here")
                print("Your search took {} seconds".format(lengthIterative))
        elif choice == "10":
            newSortedList()
        elif choice == "9":
            printLists()
            
        else:
            break

           #print("Hehe hoohoo that wasn't clever Restarting...")
"""
"""
addABunch()
asks you how many integers you would like to add to a list and how high they go
then randomly generates in accordance with those inputs"""
                
def addABunch():
    print("addabunch")
    clearWindow()
    L1W3 = Label(top, text="We're going to add a bunch of numbers")
    L1W3.grid(column = 0, row = 0)
    L2W3 = Label(top, text="How many would you like to add?")
    L2W3.grid(column = 0, row = 2)
    E1W3 = Entry(top,bd = 5)
    E1W3.grid(column = 1,row = 2)
    L3W2 = Label(top, text="How high would you like them to go")
    L3W2.grid(column = 0, row = 3)
    E2W3 = Entry(top,bd = 5)
    E2W3.grid(column=1,row =3)
    B2aW3 = Button(top, text = "Week 3 Menu", command = week3,bg = "RED")
    B2aW3.grid(column = 0,row = 7)
    def addThem():
        numToAdd = E1W3.get()
        numRange = E2W3.get()
        for x in range (0,int(numToAdd)):
            myList.append(random.randint(0, int(numRange)))
        L1aW3 = Label(top, text="Your list is now complete")
        L1aW3.grid(column = 0, row = 5)
    B1aW3 = Button(top,text="Add the values to the list",command = addThem)
    B1aW3.grid(column = 0, row = 6)

"""
addToList()
asks you what value you want to add to your list then appends it in"""
           
def addToList():
    print("addtolist")
    clearWindow()
    L4W3 = Label(top, text="Please type an integer")
    L4W3.grid(column = 0, row = 0)
    E3W3 = Entry(top, bd = 5)
    E3W3.grid(column = 0, row = 1)
    B1bW3 = Button(top, text = "Week 3 Menu", command = week3, bg = "RED")
    B1bW3.grid(column = 0, row = 3)
    def addIt():
        myList.append(int(E3W3.get()))
        L4aW3 = Label(top, text=myList)
        L4aW3.grid
    B2bW3 = Button(top, text="Add your value",command= addIt, bg= "Light Blue")
    B2bW3.grid(column = 0, row= 2)
    
"""
pulls a random value in the length of your list and tells you the integer at that index position"""

def randomSearch():
    print("randomSearch")
    clearWindow()
    L5W3 = Label(top, text = myList[random.randint(0,len(myList)-1)])
    L5W3.grid(column = 0,row = 0)
    B1cW3 = Button(top, text = "Week 3 Menu", command = week3, bg = "RED")
    B1cW3.grid(column = 0, row = 3)
    #print(myList[random.randint(0,len(myList)-1)])
    
"""
indexValues()
asks you which index position you want to look at and then tells you what is at that position"""

def indexValues():
    print("indexvalues")
    clearWindow()
    L1dW3 = Label(top, text="Which index position do you want to look at")
    L1dW3.grid(column = 0,row = 1)
    E1dW3 = Entry(top, bd = 5)
    E1dW3.grid(column = 0,row = 2)
    def indexValue():
        indexPos = E1dW3.get()
        L2dW3 = Label(top, text = myList[int(indexPos)])
        L2dW3.grid(column = 0, row = 4)
    B1dW3 = Button(top, text = "Display value at index position", command = indexValue)
    B1dW3.grid(column = 0,row = 3)
    B1dW3 = Button(top, text = "Week 3 Menu", command = week3, bg = "RED")
    B1dW3.grid(column = 0, row = 5)
    

"""
linearSearch() asks you what value you want to look for in your list then goes throught the list one position at a time and compares the value its on to the value
you're looking for then if you find the value it stops and returns which index position its at"""

def linearSearch():
    print("linearSearch")
    clearWindow()
    L1eW3 = Label(top, text = "What number are you looking for")
    L1eW3.grid(column = 0,row = 1)
    E1eW3 = Entry(top, bd = 5)
    E1eW3.grid(column = 0,row = 2)
    def searchlinearSearch():
        amountOfTimes = 0
        searchItem = E1eW3.get()
        for x in range (len(myList)):
            if myList[x] == int(searchItem):
                amountOfTimes = amountOfTimes + 1
                AtPOS.append(x)
                L2eW3 = Label(top, text = "your item is at index pos {}".format(AtPOS))
                L2eW3.grid(column = 0, row = 5)
        print("Your item is in the list", amountOfTimes,"times")
    B1eW3 = Button(top, text = "Search",command = searchlinearSearch)
    B1eW3.grid(column = 0, row = 3)
    B2eW3 = Button(top, text = "Week 3 Menu", command = week3, bg = "RED")
    B2eW3.grid(column = 0, row = 7)
    
    AtPOS = []


"""
recursiveBinarySearch() asks you what number you're looking for then splits the sorted list in half if the value is less then the middle it looks at the first half of the list
if its greater then it looks in the second half of the list it then does the same proccess working closer and closer to the value """

def recursiveBinarySearch():
    print("recursive search")
    sortList(myList)
    clearWindow()
    L1fW3 = Label(top, text = "What number are you looking for")
    L1fW3.grid(column = 0,row = 1)
    E1fW3 = Entry(top, bd = 5)
    E1fW3.grid(column = 0,row = 2)

    def recursiveSearch(unique_list, low, high, x):
        print("yeetus")
        if high >= low:
            
            mid = (high + low) // 2
            print("1")

            if unique_list[mid] == x:
                print("2")
                L2fW3 = Label(top, text = "Oh what luck your number is at position {}".format(mid))
                L2fW3.grid(column = 0,row = 4)
                #endRecursive = time.time()
                #print("Your search took {} seconds".format(endRecursive - startRecursive))
                return mid
            elif unique_list[mid] > x:
                return recursiveSearch(unique_list, low , mid -1, x)
            else:
                return recursiveSearch(unique_list, mid + 1, high, x) 
        else:
            L2fW3 = Label(top, text = "YOur number isn't in the your list")
            L2fW3.grid(column = 0,row = 4)
            #endRecursive = time.time()
            #print("Your search took {} seconds".format(endRecursive - startRecursive))
    B1fW3 = Button(top, text = "Search", command = lambda:recursiveSearch(unique_list, 0, len(unique_list)-1, int(E1fW3.get())))
    B1fW3.grid(column = 0, row = 3)
    B2fW3 = Button(top, text = "Week 3 Menu", command = week3, bg = "RED")
    B2fW3.grid(column = 0, row = 7)

"""
sortList() goes through your main list starting from 0 and checks if the value its on is in your list it adds it to your new sorted list this way it will be
sorted starting at 0 then asks you if you want to see your new sorted list if yes it prints it if no it doesnt print it"""
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()

        
def sortListAsk():
    clearWindow()
    def sortedList():
        sortList(myList)
        L1gW3 = Label(top, text = unique_list, wraplength = 40)
        L1gW3.grid(column = 0, row = 2)
    B1gW3 = Button(top, text = "Sort and display your List", command = sortedList)
    B1gW3.grid(column = 0, row = 1)
    B2gW3 = Button(top, text = "Week 3 Menu", command = week3, bg = "RED")
    B2gW3.grid(column = 0, row = 7)
    
        
"""
printLists() checks if you have created a sorted list if yes it asks you which list you would like to see if no it will just print your regular list, doesnt actually
check to see if you replied with un-sorted just checks if you said sorted and anything other then sorted"""
def printLists():
    clearWindow()
    L1hW3 = Label(top, text = "Which list would you like to print?")
    L1hW3.grid(column = 2, row = 1)
    def Sorted():
        sortList(myList)
        L2hW3 = Label(top, text = unique_list, wraplength = 50)
        L2hW3.grid(column = 1, row = 3)
    B1hW3 = Button(top, text= "Sorted",command = Sorted)
    B1hW3.grid(column = 1, row = 2)
    def UnSorted():
        L3hW3 = Label(top, text = myList, wraplength = 50)
        L3hW3.grid(column = 3,row = 3)
    B2hW3 = Button(top, text ="Un-Sorted",command = UnSorted)
    B2hW3.grid(column = 3, row = 2)
    B3hW3 = Button(top, text = "Week 3 Menu", command = week3, bg = "RED")
    B3hW3.grid(column = 0, row = 7)
"""
iterativeBinarySearch() the iterative search will split your list into two pieces then determine which half the value youre looking for is in it will keep on doing this till it finds your value"""
def iterativeBinarySearch(unique_list, x):
    startIterative =  time.time()
    
    low = 0
    high = len(unique_list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) //2

        if unique_list[mid] < x:
            low = mid + 1
            lengthIterative = endIterative - startIterative

        elif unique_list[mid] > x:
            high = mid -1
            lengthIterative = endIterative - startIterative

        else:
            return mid
            lengthIterative = endIterative - startIterative
    return -1
    endIterative = time.time()
    lengthIterative = endIterative - startIterative
""" makes a new list very similiar to the addABunch() function but then sorts the new list"""
def newSortedList():
    newToAdd = input("how many numbers do you want to add?")
    newRange = input("how high do you want them to go?")
    for x  in range (0,int(newToAdd)):
        NewSorted.append(random.randint(0, int(newRange)))
    NewSorted.sort()
    
    print(NewSorted)


if __name__ == "__main__":
    mainMenu()
    print("dunder")

top.mainloop()
