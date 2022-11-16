#This version of the code was posted in a StackOverflow question, and is being kept temporarily until the question is answered.

import tkinter as tk

root = tk.Tk()

background = tk.Frame(root)
background.grid(row=0, column=0, rowspan=3, columnspan=2, padx=10, pady=10)

lbf1 = tk.LabelFrame(background, width=30, text="Lane 1")
lbf1.grid(row=0, column=0, columnspan=2, rowspan=3)

timer1 = tk.Label(lbf1, text="00:00",  bg="#000000", fg="#ff0000", font=38)
timer1.grid(row=3, column=0, columnspan=2, sticky="s", padx=5, pady=5)

ent1 = tk.Entry(lbf1, bg="#cccccc", fg="#000000", justify="center", width=15)
ent1.insert(0, "minutes")
ent1.grid(row=0, column=0, columnspan=2, sticky="s", padx=5, pady=5)

def timer1Set():
	t = str(ent1.get())
	s = "00"
	global time1
	time1 = "{0}:{1}".format(t, s)
	timer1.config(text=time1)
	last = len(ent1.get())
	ent1.delete(0,last)
	startB1.config(state="active")

def timer1Update():
	if pauseB1.cget("state") == "disabled":
		startB1.config(state="active")
		return None
	else:
		time1 = str(timer1.cget("text"))
		ctime1 = time1.partition(":")
		cmins1, _, csecs1 = ctime1
		cmins1 = int(cmins1)
		csecs1 = int(csecs1)
		startB1.config(state="disabled")
		
		if (cmins1 == 0) and ((csecs1 > 0) and (csecs1 < 11)):
			timer1.config(text=str(cmins1) + ":" + ("0" + str(csecs1 - 1)))
			timer1.after(1000, lambda:(timer1Update()))
		elif (cmins1 == 0) and (csecs1 > 0):
			timer1.config(text=str(cmins1) + ":" + str(csecs1 - 1))
			timer1.after(1000, lambda:(timer1Update()))
		elif (cmins1 > 0) and (csecs1 == 0):
			timer1.config(text=str(cmins1 - 1) + ":59")
			timer1.after(1000, lambda:(timer1Update()))
		elif (cmins1 > 0) and ((csecs1 > 0) and (csecs1 < 11)):
			timer1.config(text=str(cmins1) + ":" + ("0" + str(csecs1 - 1)))
			timer1.after(1000, lambda:(timer1Update()))
		elif (cmins1 > 0) and (csecs1 > 0):
			timer1.config(text=str(cmins1) + ":" + str(csecs1 - 1))
			timer1.after(1000, lambda:(timer1Update()))
		else:
			startB1.config(state="active")
			lane1End = tk.Tk()
			L1EndL = tk.Label(lane1End, text="Lane 1 Time Up!")
			L1EndL.pack()
			L1EndB = tk.Button(lane1End, text="Okay", command=lane1End.destroy)
			L1EndB.pack()
			lane1End.mainloop()


def z1():
	timer1.config(text="00:00")

setB1 = tk.Button(lbf1, text="Set Timer", justify="left", command=timer1Set)
setB1.grid(row=1, column=0, sticky="we", padx=5, pady=5)

def setB1state():
	if ent1.get() == "":
		setB1.config(state="disabled")
		setB1.after(1000, setB1state)
	else:
		setB1.config(state="active")
		setB1.after(1000, setB1state)

pauseB1 = tk.Button(lbf1, width=5, text="Pause", command=lambda:((pauseB1.config(state="disabled")),(pauseB1.after(1000, lambda:(pauseB1.config(state="active"))))))
pauseB1.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

startB1 = tk.Button(lbf1, text="Start", justify="center", command=lambda:(timer1Update()))
startB1.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

clearB1 = tk.Button(lbf1, width=5, text="Clear", justify="right", command=z1)
clearB1.grid(row=2, column=0, sticky="we", padx=5, pady=5)

setB1state()

print(startB1.cget("width"))

root.mainloop()
