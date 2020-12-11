from tkinter import *

master = Tk()

def zavrit():   
    exit()

def baf():
    print("baf")

text = Label(master, text = "Nejlepší Program na světě")
popisek1 = Label(master, text = "Printne 'baf' do Outputu ->")
popisek2 = Label(master, text = "Ukončí Program ->")
mezera = Label(master, text = "")

cudlik2 = Button(master, text = "Print 'baf' ", command = baf)
cudlik = Button(master, text = "Konec", command = zavrit)

text.grid(row=1, column = 2)
cudlik2.grid(row = 3, column = 2)
cudlik.grid(row = 4, column = 2)
popisek1.grid(row = 3, column = 1)
popisek2.grid(row = 4, column = 1)
mezera.grid(row = 2, column = 2)


#text.pack()
#cudlik2.pack()
#cudlik.pack()

master.mainloop()