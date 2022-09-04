
from tkinter import * 
from PIL import ImageTk, Image
i=0
import os
a=None
battery=os.popen("acpi -b|awk '{print $4}'|sed s/%.*//")
charging=os.popen("acpi -b|awk '{print $3}'|sed s/%.*//")
charging=charging.read()
print(charging)
if charging[0]=="C":
	chargingstatus=True
else:
	chargingstatus=False
batperc= int(battery.read())
def Exitpress():
	root.destroy()


root = Tk() # Create the root (base) window where all widgets go 
exitbutton = Button(root,text="exit",command=Exitpress)

exitbutton.pack()
canvas  = Canvas(root)
canvas.pack()
def makebat(batperc):
	top_y=54+(146-54)*(100-batperc)/100
	if batperc<=15:
		color="red"
	elif batperc<=79:
		color="yellow"
	else:
		color="green"
	canvas.create_rectangle(50, 50, 100, 150,width=3)
	canvas.create_rectangle(54, top_y, 96, 146, fill=color)
	canvas.create_rectangle(70, 40, 80, 50, fill="black")

def make25(color):
	top_y=54+(146-54)*(100-25)/100
	global a
	a=canvas.create_rectangle(54, top_y, 96, 146, fill=color)
	


def make50(color):
	top_y=54+(146-54)*(100-50)/100
	global a
	a=canvas.create_rectangle(54, top_y, 96, 146, fill=color)
	

def make75(color):
	top_y=54+(146-54)*(100-75)/100
	global a
	a=canvas.create_rectangle(54, top_y, 96, 146, fill=color)
	
i=0	
def update():
	global a,i
	global batperc
	i=(i)%3 +1
	if batperc<=15:
		color="red"
	elif batperc<=79:
		color="yellow"
	else:
		color="green"
	
	if i==1:
		make25(color)
	elif i==2:
		make50(color)
	else:
		make75(color)
	def dele():
		#print("now-",a,i)
		canvas.delete(a)
	root.after(1000,dele)
	root.after(1000,update)
if chargingstatus:#if battery is charging then do
	canvas.create_rectangle(50, 50, 100, 150,width=3)
	canvas.create_rectangle(70, 40, 80, 50, fill="black")

	root.after(0,update)
else:
	makebat(batperc)
	#you can uncomment these to test the percentages and colors
	#makebatperc(50)
	#makebatperc(10)
	#makebatperc(90)

root.mainloop() # Start the event loop
