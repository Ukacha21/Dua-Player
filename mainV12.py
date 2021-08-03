
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as filedialog
import pygame
#import keyboard
import time
import os
import re


#from PIL import ImageTk, Image
def masterWin():

    root = Tk()

    root.title("Calvin Player")

    root.iconbitmap("Images/dlogo.ico") #"icon.ico"
    root.geometry("480x600") #("480x720")
    root.resizable(False,False)
    root.overrideredirect(1)
    #root["bg"] = "grMay"

    root.attributes("-topmost", True)

    pygame.mixer.init()

    #Buttons

    #def play():



    #borderwidth = 2     to be used in buttons
    #borderwidth, highlightthickness=4, highlightcolor="black", highlightbackground="black" 
    #button modes: relief= "groove", "solid", "ridge", "sunken", "raised", "flat"

    #playB = Button(text="play", borderwidth=0,  bg='#F0FFFF', fg='#FFFFFF', compound=LEFT, anchor="se", command=root.destroy)

    playimg = PhotoImage(file="Images/unpause.png")
    pauseimg = PhotoImage(file="Images/pause.png")
    nextimg = PhotoImage(file="Images/next.png")
    previmg = PhotoImage(file="Images/prev.png")
    

    wallimg = PhotoImage(file="Images/capt.png")
    pathimg = PhotoImage(file="Images/showpath.png")

    biglist = []


    rwidth = root.winfo_screenmmwidth()

    
    

    
    def prevMusic(musicNum):

        nextB.config(command= lambda: nextMusic(musicNum+1))
        prevB.config(command= lambda: prevMusic(musicNum-1))
   
        pygame.mixer.music.load(biglist[0][musicNum])
        pygame.mixer.music.play()

        basename = os.path.basename(biglist[0][musicNum])
        
        musicName.config(text=str(basename))

        musicName.place(y=390, anchor=CENTER, x =rwidth//1.5) #x=170, y=330

        def showpath(*args):

            openlabel.place_forget()
            
            nextlabel.place_forget()
            prevlabel.place_forget()
                
            pathlabel.config(text=biglist[0][musicNum])

            pathlabel.place(y=570, anchor=CENTER, x =rwidth//1.5)
            pathlabel.after(4000, pathlabel.place_forget)

        def popshowpathlabelf(*args):
            popshowpathlabel.place(x=60, y=45)
            popshowpathlabel.after(4000, popshowpathlabel.place_forget)

        #pathButton.place(y=110, x=95)
        pathButton.config(command=showpath)
        pathButton.bind("<Enter>", popshowpathlabelf)

    
    def nextMusic(musicNum):

        nextB.config(command= lambda: nextMusic(musicNum+1))
        prevB.config(command= lambda: prevMusic(musicNum-1))

        pygame.mixer.music.load(biglist[0][musicNum])
        pygame.mixer.music.play()

        basename = os.path.basename(biglist[0][musicNum])
        
        musicName.config(text=str(basename))

        musicName.place(y=390, anchor=CENTER, x =rwidth//1.5) #x=170, y=330

        def showpath(*args):
            openlabel.place_forget()
            
            nextlabel.place_forget()
            prevlabel.place_forget()
            
            pathlabel.config(text=biglist[0][musicNum])
            pathlabel.place(y=570, anchor=CENTER, x =rwidth//1.5)
            pathlabel.after(4000, pathlabel.place_forget)

        def popshowpathlabelf(*args):
            popshowpathlabel.place(x=60, y=45)
            popshowpathlabel.after(4000, popshowpathlabel.place_forget)

        #pathButton.place(y=30, x=100)
        pathButton.config(command=showpath)
        pathButton.bind("<Enter>", popshowpathlabelf)


        
        


    def ask():

        
        filep = filedialog.askopenfilenames(initialdir="%Music%", title="Select audio files to open", filetypes=(("mp3 files", "*.mp3"),("m4a files", "*.m4a")))

        #mlist = os.listdir(filep)
        
        mlist = list(filep)
        #print(mlist)
        biglist.append(mlist)

        print("big list: ", biglist[0])
        pygame.mixer.music.load(biglist[0][0])
        pygame.mixer.music.play()

        basename = os.path.basename(biglist[0][0])

        musicName.config(text=str(basename))
        #musicName.place_forget()
        #musicName.place(y=390, anchor=CENTER, x =rwidth/2) #x=170, y=330

        def showpath(*args):

            openlabel.place_forget()
            
            topmlabel.place_forget()
            

            pathlabel.config(text=biglist[0][0])
            pathlabel.after(4000, pathlabel.place_forget)

            pathlabel.place(y=570, anchor=CENTER, x=rwidth//1.5)
        
        def popshowpathlabelf(*args):
            popshowpathlabel.place(x=60, y=45)
            popshowpathlabel.after(4000, popshowpathlabel.place_forget)

        pathButton.place(x=100, y=30)
        pathButton.config(command=showpath)
        pathButton.bind("<Enter>", popshowpathlabelf)

        
    def play():
        
        pygame.mixer.music.pause()

        def conf():
            pygame.mixer.music.unpause()
            playB.config(image=playimg, command=play)

        playB.config(image=pauseimg, command=conf)

   
    wallLabel = Label(image=wallimg)

    redB = PhotoImage(file="Images/close.png")
    greenB = PhotoImage(file="Images/minim.png")

    closeB = Button(image=redB, borderwidth=0, bg="#9C2D71", command=root.destroy)
    minimB = Button(image=greenB, borderwidth=0, bg="#AB2B6C", command=root.iconify)

    global playB
    playB = Button(image=playimg, borderwidth=0, bg="#BA2667", command=play)
    
    #tryna make the same button play and pause

    nextB = Button(image=nextimg, borderwidth=0, bg="#AB2B6C", command= lambda: nextMusic(2))
    prevB = Button(image=previmg, borderwidth=0, bg="#CB2161", command= lambda: prevMusic())
    

    #keyboard.press()
    '''if keyboard.press(hotkey="Space") == "Space":
        pygame.mixer.music.pause()
    '''

    def move_window(event):
        root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    title_bar = Frame(root, relief='flat',bg="#BA2667", bd=1,height=30, width=385)

    title_text=Label(title_bar, text="Dua Player", font=("Consolas", 13), bg="#BA2667", anchor=CENTER)

    music_icon = PhotoImage(file="images/icon.png")
    music_Label = Label(image=music_icon, bg="#CB2161") #bg="#BA2667"

    musicName = Label(text=" ", font=("consolas", 10), bg="#CB2161", fg="white")

    pathlabel = Label(text=" ", font=("consolas", 10), bg="#CB2161", fg="white")
    

    

    pathButton = Button(root,borderwidth=0, image=pathimg, text="path", font=("consolas", 10), bg="#CB2161", fg="white")
    
    pathlabel.place(y=570, anchor=CENTER, x =rwidth//1.5)
    #pathButton.place(x=100, y=30)


    wallLabel.place(x=-2, y=-2)

    title_bar.place(x=45, y=0)
    title_text.place(x=150, y=2)
    playB.place(x=220, y=425)
    
    nextB.place(x=325, y=430)
    prevB.place(x=95, y=430)
    
    closeB.place(x=445, y=7)
    
    music_Label.place(y=240, anchor=CENTER, x=240)
    
    musicName.place(y=390, anchor=CENTER, x =rwidth//1.5) #x=170, y=330

    #root.geometry('480x600')
    
    def hometop():
        top = Toplevel()
        top.title("Home")
        top.geometry("320x320")
        top.resizable(False, False)
        label = Label(top, text="Home", font=("Arial", 32))
        label.pack()

    title_bar.bind('<B1-Motion>', move_window)
    title_text.bind('<B1-Motion>', move_window)
    wallLabel.bind('<B1-Motion>', move_window)
    music_Label.bind('B1-Motion>', move_window)
    #home.bind('<B1-Motion>', move_window)

    #closeB.place(x=440, y=0)

    global vol
    vol = 0 

    volUpImg = PhotoImage(file="Images/volUp.png")
    volDownImg = PhotoImage(file="Images/volDown.png")


    def soundButtons(*args):
        volLabel = Label(root, text="", bg="#9C2D71", fg="white", font=("consolas", 14))
        volLabel.place(x=437, y=40)

        def clear():
            volLabel.config(text="")
            #volLabel.place_forget()

        def Up():
            #vol += 1 #0.4
            global vol
            vol += 0.100000
            
            pygame.mixer.music.set_volume(vol)
            resultv = pygame.mixer.music.get_volume()
            #print("volume: ", resultv)
            volLabel.config(text=str(float(resultv)))

            #volLabel.place(x=437, y=40)

            volLabel.after(3000, clear)
            volUp.after(5000, volUp.place_forget)
            
            
        def Down():
            global vol
            vol -= 0.100000
            
            pygame.mixer.music.set_volume(vol)
            volres = pygame.mixer.music.get_volume()
            #print("volume: ", volres)
            volLabel.config(text=str(float(volres)))

            #volLabel.place(x=437, y=40)

            volLabel.after(3000, clear)
            volDown.after(5000, volDown.place_forget)
        
        volUp = Button(root, bg="#9C2D71", image=volUpImg, borderwidth=0, command=Up)
        volDown = Button(root, bg="#9C2D71", image=volDownImg, borderwidth=0, command=Down) 

        volUp.place(x=450, y=120)
        volDown.place(x=450, y=150)

        def killvols():
            volUp.place_forget()
            volDown.place_forget()
            soundB.config(command=soundButtons)

        volUp.after(10000, killvols)
        volDown.after(10000, killvols)

        def killFrame():
            volUp.place_forget()
            volDown.place_forget()
            soundB.config(command=soundButtons)

        soundB.config(command=killFrame)


    soundImg = PhotoImage(file="Images/sound.png")

    popUpImg = PhotoImage(file="Images/on.png")
    popDownImg = PhotoImage(file="Images/off.png")
    addImg = PhotoImage(file="Images/add.png")

    openB = Button(root, image=addImg,borderwidth=0, bg="#CB2161", command=ask)     
    soundB = Button(root, image=soundImg, font=("consolas", 13),  relief="flat", bg="#9C2D71", command=soundButtons)
    
    def ChangePop():

        def rechangePop():
            popButton.config(image=popUpImg, command=ChangePop)
            root.attributes("-topmost", True)


        popButton.config(image=popDownImg, command=rechangePop)
        root.attributes("-topmost", False)


    popButton = Button(image=popUpImg, borderwidth=0, bg="#CB2161", command=ChangePop)
    
    global topmlabel
    global openlabel

    topmlabel = Label(text="topmost on-off", font=("consolas", 10), bg="#CB2161", fg="white")
    openlabel = Label(text="open file(s)", font=("consolas", 10), bg="#CB2161", fg="white")
    playlabel = Label(text=" ", font=("consolas", 10), bg="#BA2667", fg="white")
    nextlabel = Label(text=" ", font=("consolas", 10), bg="#AB2B6C", fg="white")
    prevlabel = Label(text=" ", font=("consolas", 10), bg="#CB2161", fg="white")
    popshowpathlabel = Label(text="Show path/directory", font=("consolas", 10), bg="#CB2161", fg="white")
    

    def showtop(*args):

        openlabel.place_forget()
        popshowpathlabel.place_forget()
        
        topmlabel.place(x=70, y=45)
        topmlabel.after(4000, topmlabel.place_forget)

    def showOpen(*args):

        topmlabel.place_forget()
        popshowpathlabel.place_forget()
        
        openlabel.place(x=45, y=45)
        openlabel.after(4000, openlabel.place_forget)
        
    def showplay(*args):
        nextlabel.place_forget()
        prevlabel.place_forget()

        playlabel.config(text="Play/Pause")
        playlabel.place(x=200, y=475)
        playlabel.after(2500, playlabel.place_forget)

    def shownext(*args):
        
        playlabel.place_forget()
        prevlabel.place_forget()


        nextlabel.config(text="Play next track")
        nextlabel.place(x=300, y=480)
        nextlabel.after(2500, nextlabel.place_forget)

    def showprev(*args):
        playlabel.place_forget()
        nextlabel.place_forget()


        prevlabel.config(text="Play previous track")
        prevlabel.place(x=75, y=480)
        prevlabel.after(2500, prevlabel.place_forget)




    popButton.bind("<Enter>", showtop)
    openB.bind("<Enter>", showOpen)
    playB.bind("<Enter>", showplay)
    nextB.bind("<Enter>", shownext)
    prevB.bind("<Enter>", showprev)
    
    popButton.place(x=70, y=30)


    openB.place(x=45, y=30) #(relx=0, rely=0, anchor=NW)
    
    soundB.place(x=445, y=70)
    
    soundB.bind("<Enter>", soundButtons)

    #minimB.place(x=125, y=15)
    mainloop()

#minimize to a litte tray
def startone():

    global start
    start = Tk()
    start.geometry("320x120")
    start['bg'] = 'blue'
    start.overrideredirect(1)

    #orientation and more missing
    start_Label = Label(start, text="Loading", font=("times new roman", 14))
    progress_bar = ttk.Progressbar(start, orient=HORIZONTAL, 
    length=300, mode="determinate")

    value = progress_bar['value']
    

    for x in range(10):
        value += 10
        print(value)
        if value == 100:
            start.destroy()
    start.mainloop()

#startone()

masterWin()