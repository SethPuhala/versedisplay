import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk
from tkinter import font
import time
import random

def shrink(text):
	ps = []
	for v in text:
		ps.append(v)
	text = str(ps[0])
	text = (text.split(">", 1)[1])
	final = (text.split("<", 1)[0])
	return final


def getVerse():
	url = 'https://www.bible.com/verse-of-the-day'


	full = requests.get(url)
	full = full.content
	soup = BeautifulSoup(full, 'html.parser')

	verse = soup.findAll('p', {'class':'yv-gray50 mt0 mb2'})
	loc = soup.findAll('p', {'class':'usfm fw7 mt0 mb0 yv-gray25 f7 ttu'})
	VERSE = (shrink(verse) + '\n ' + shrink(loc))


	return VERSE


window  = Tk()
window.attributes('-fullscreen',True)
words = getVerse()

ims = [tk.PhotoImage(file='1.ppm'), tk.PhotoImage(file='2.ppm'), tk.PhotoImage(file='3.ppm'), tk.PhotoImage(file='4.ppm'), tk.PhotoImage(file='5.ppm'), tk.PhotoImage(file='6.ppm'), tk.PhotoImage(file='7.ppm'), tk.PhotoImage(file='8.ppm'), ]



def redo():


	main.itemconfigure(bgimg, image=random.choice(ims))
	main.itemconfigure(text, text=getVerse())

	window.after(5000, redo)








window.geometry('1080x1920')
window.config(cursor='none')
main = Canvas(window, height=1920, width=1080, bg='black', highlightthickness='0')
main.pack()
bgimg = main.create_image(4, 4, anchor=NW, image=random.choice(ims))
text = main.create_text(540, 960, text=getVerse(), font=('Candara Bold', 55), anchor="center", fill='white', width ='1000')
window.after(430200000, redo)
window.mainloop()


	









	


