# from _typeshed import Self
from ast import Str
import random
from tkinter import *
import tkinter
from typing import Sized
from playsound import playsound
from PIL import ImageTk,Image
from tkinter import messagebox
    


class App:

    wordList : dict
    dictionaryKey : list
    randomKey : list
    resultWord : Str
    clueLength : int
    index_set : set
    left_attempt : int
    guessValue : Str
    flag : bool
    slove_word : set
    
    
    
    def set_index_set(self) -> None:
        
        self.index_set  = set()
        self.index_set.clear()
        while self.clueLength != len(self.index_set):
            self.index_set.add(random.randint(0,len(self.resultWord)-1))
        print(self.index_set)
        
    def init(self):
        
        self.left_attempt = 5
        self.flag = True
        self.wordList = {
            
            "Fruits" : ["Banana","Apple","Mango","Orange","Pinepal","Cherry","Grapes","Pomegranate",
                            "Coconut","Papaya","Watermelon","Strawberry","Kiwi","Pear","Melon"],

            "Vehicles" : ["car","Truck","Helicopter","Plane","Motorcycle","Bicycle","Bus","Ambulance",
                            "Tractor","Train","Boat","Submarine"],

            "Animal" : ["Elephent","Lion","Tiger","Horse","Zebra","Camel","Monkey","Fox","Deer",
                            "Cheetah","Kangaroo","Jaguar","Wolf","Gorila","Hippopotamus","Giraffe",
                            "Cow","Goat","Pig","Donkey","Buffalo","Rabbit"],

            "Bird" : ["Eagle","Pigeon","Peacock","Sparrow","Parrot","Swan","Woodpecker","Kingfisher",
                        "Owl","Duck","Hummingbird","Penguin"],

            "Vegetabel" : ["Potato","Tomato","Brinjal","Radish","Onion","Garlic","LadyFinger","Cauliflower",
                            "Carrot","Ginger","Chilli","Capsicum","Cucumber","Mushroom","Broccoli","Pumpkin"],

            "Colour" : ["Red","Green","Blue","Yellow","Black","Violet","Cyan"],

            "Flower" : ["Rose","Lily","Lotus","Sunflower","Marygold","Tulip","Jasmine","Hibiscus","Lavender",
                            "Bluebell","Poppy"]
        }
        
        while True: 
        
            self.dictionaryKey = list(self.wordList.keys())
            self.randomKey = random.choices(self.dictionaryKey)
            self.resultWord = random.choices(self.wordList[self.randomKey[0]])[0]
            if self.resultWord not in self.slove_word:
                self.slove_word.add(self.resultWord)
                break
            
           
        

        print(self.resultWord)

        self.clueLength = int(len(self.resultWord)/2)
        self.set_index_set()

    def create_guess_word(self) -> None:
        
        for i in range(0,len(self.resultWord)):
            if i in self.index_set:
                Label(displayFrame,text=self.resultWord[(i)],font="Timesnewroman 20 bold").pack(side=LEFT,padx=10)
            else:
                Label(displayFrame,text="_",font="Timesnewroman 20 bold").pack(side=LEFT,padx=10)  
        
    def create_image_frame(self) -> None:
        global imageFrame
        imageFrame = Frame(root,borderwidth=10,relief=SUNKEN)
        imageFrame.pack()

    def create_button_frame(self):

        
        global next_btn
        global exit_btn
        global buttonFrame

        buttonFrame = Frame(root)
        buttonFrame.pack()

        next_btn = Button(buttonFrame,text="Next",command=self.check,bg="orange",padx=10,font="Timesnewroman 15 bold",state=DISABLED)
        next_btn.pack(side=LEFT,pady=10)

        exit_btn = Button(buttonFrame,text="Exit",command=root.quit,bg="orange",padx=10,font="Timesnewroman 15 bold")
        exit_btn.pack(side=RIGHT,padx=20)

    def playSound(self) -> None:

        playsound('con_sound.mp3' , block=False)

    def clear_frame(self) -> None:

        for i in displayFrame.winfo_children():
            i.destroy()

    def clear_image_frame(self) -> None:
        for i in imageFrame.winfo_children():
            i.destroy()

    def displayImage(self) -> None:
        global img
        global img_label
        img = ImageTk.PhotoImage(Image.open("images/"+self.resultWord+".jpg").resize((170,170),Image.ANTIALIAS))
        img_label = Label(imageFrame,text="Image Frame",image=img)
        img_label.pack(anchor=CENTER)

    def nextWord(self) -> None:
        
        self.init()
        attempt_label.config(text="Attempt left : 5",fg="black")
        self.clear_frame()
        self.create_guess_word()
        category_label.config(text = str(self.randomKey[0],)+ " Name")
        chk_btn.config(state = NORMAL,bg="green",fg="white")
        inputentry.config(state = NORMAL)
        next_btn.config(state=DISABLED)
        img_label.destroy()
        self.clear_image_frame()
        imageFrame.destroy()
        buttonFrame.destroy()
        self.create_image_frame()
        self.create_button_frame()

    def check(self) -> None:

        playsound('chk_sound.wav' ,block = False)
        self.flag = True

        if(self.left_attempt == 1):

            root.grab_set()
            playsound('game_over.wav',block=False)
            play_again = messagebox.askquestion("Game Over","Play Again?")
            if play_again == 'yes':
                
                self.clear_frame()
                
                self.left_attempt = 5   
                
                self.set_index_set()
                self.create_guess_word()
                attempt_label.config(text="Attemp left : 5",fg="black")
                hint_label.config(text="")

            else:
                root.quit()

            return
            
        
        self.guessValue = inputvalue.get()
        inputentry.delete(0,END)
        if any(map(str.isdigit,self.guessValue)):
            hint_label.config(text="Please enter only character!",fg="red")
            self.left_attempt -= 1
            attempt_label.config(text="Attempt left : "+str(self.left_attempt),fg="red")
            return

        if len(self.guessValue) != len(self.resultWord) and len(self.guessValue) != 1:
            
            hint_label.config(text="Please enter only 1 character or entire word!",fg="red")
            self.left_attempt -= 1
            attempt_label.config(text="Attempt left : "+str(self.left_attempt),fg="red")
            return
        
        
        if len(self.guessValue) == len(self.resultWord):
        
            if self.guessValue.lower() == self.resultWord.lower() :
                for i in range(0,len(self.resultWord)):
                    if i not in self.index_set:
                        self.index_set.add(i)
                        self.flag = False
                        
                
            if(self.flag):
                
                hint_label.config(text=" Guess word not correct! ",fg="red")
                self.left_attempt -=  1
                attempt_label.config(text="Attempt left : "+str(self.left_attempt),fg="red")
                
            else:
                hint_label.config(text="",fg="red")
                
            if len(self.resultWord) == len(self.index_set):
                
                self.clear_frame()
                self.create_guess_word()
                self.create_image_frame()
               
               
                self.displayImage()
                self.playSound()
                buttonFrame.destroy()
                self.create_button_frame()
                
                next_btn.config(state = NORMAL,command=self.nextWord)
                chk_btn.config(state = DISABLED,bg = "grey",fg="white")
                inputentry.config(state = DISABLED)
                
                
                
        else: 

            for i in range(0, len(self.resultWord)):
                
                if i not in self.index_set:
                    if(self.guessValue.lower() == self.resultWord[i].lower()):
                        self.index_set.add(i)
                        self.flag = False
                        self.clear_frame()
                        self.create_guess_word()
            if(self.flag):
                hint_label.config(text="Character "+self.guessValue+" not in the word! ",fg="red")
                self.left_attempt -= 1
                attempt_label.config(text="Attempt left : "+str(self.left_attempt),fg="red")
            else:
                hint_label.config(text="")

            if len(self.resultWord) == len(self.index_set):
                
                self.clear_image_frame()
                
                self.displayImage()
                
                self.playSound()
                next_btn.config(state = NORMAL,command=self.nextWord)
                chk_btn.config(state = DISABLED,bg = "grey",fg="white")
                inputentry.config(state = DISABLED)

    def home(self) -> None:
        
        global header_label
        global inputframe
        global chk_btn
        global attempt_label
        global hint_label
        global category_label
        global displayFrame
        global inputentry
        global inputvalue

        header_label = Label(root,text="Word Guess",borderwidth=15,font="Timesnewroman 23 bold",bg="orange",pady=10,relief=SUNKEN)
        header_label.pack(pady=10,fill=X)

        inputframe  = Frame(root)
        inputframe.pack(side=TOP)

        Label(inputframe,text="Enter Character: ",font="Timesnewroman 20 bold").pack(side=LEFT)

        inputvalue = StringVar()
        inputentry = Entry(inputframe,text=inputvalue,font="Timesnewroman 20 ",width=15)
        inputentry.pack(side=LEFT,padx=10)

        chk_btn = Button(inputframe,text="Check",command=self.check,bg="green",fg="white",padx=10,font="Timesnewroman 15 bold")
        chk_btn.pack(side=LEFT,anchor=SW)

        attempt_label = Label(inputframe,text=" Attempt left : 5")
        attempt_label.pack(side=LEFT,anchor=CENTER,padx=10)

        hint_label = Label(root,text="")
        hint_label.pack(pady=20,padx=20)
        category_label = Label(root,text=str(self.randomKey[0],)+" Name",font="Timesnewroman 10 bold")
        category_label.pack()

        displayFrame  = Frame(root)
        displayFrame.pack(anchor=CENTER,padx=50,pady=40)

        self.create_guess_word()
        self.create_image_frame()
        self.create_button_frame()


root = Tk()
root.geometry("900x900+200+10")
root.minsize(900,900)
root.title("Guess Word")
app = App()
app.slove_word = set()
app.init()
app.home()
root.mainloop()

