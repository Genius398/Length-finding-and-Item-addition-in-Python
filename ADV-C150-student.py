 from tkinter import *
 
 root=Tk()
 root.title("Length finding and Item addition in Python")
 root.geometry("400x400")
 
 enter_name = Entry(root)
 enter_name.place(relx=0.5, rely=0.2, anchor=CENTER)
 
 prizeList = Label(root)
 randomNumberGeneratorVariable = Label(root)
 prizeWon = Label(root)
 
 prizeListOne= []
 
 def addPrize():
     prizeName = enter_name.get()
     prizeListOne.append(prizeName)
     prizeList["text"] = "Prize is :" + str(prizeList)
     
     
    
 def randomNumberGenerator():
     length = len(prizeList)
     random_no = random.randit(0,length-1)
     random_number_label["text"] = str(random_no)
     generated_random_number = list1[random_no]
     prizeWonTwo["text"] = "Your prize is " + str(generated_random_number)
 
 root.mainLoop()