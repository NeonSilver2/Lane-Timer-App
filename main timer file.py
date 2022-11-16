import tkinter as tk

root = tk.Tk()
root.title("Lane Timer")
icon = tk.PhotoImage(file=r"Python\PROJECTS\Lane Timer App\lane_timer_icon.gif")
root.iconphoto(True, icon)

background = tk.Frame(root, bg="#444444")
background.grid(row=0, column=0, rowspan=4, columnspan=2)


lbf1 = tk.LabelFrame(background, width=30, text="Lane 1", labelanchor="n", bg="#757575", fg="black", font=20)
lbf2 = tk.LabelFrame(background, width=30, text="Lane 2", labelanchor="n", bg="#757575", fg="black", font=20)
lbf3 = tk.LabelFrame(background, width=30, text="Lane 3", labelanchor="n", bg="#757575", fg="black", font=20)
lbf4 = tk.LabelFrame(background, width=30, text="Lane 4", labelanchor="n", bg="#757575", fg="black", font=20)
lbf5 = tk.LabelFrame(background, width=30, text="Lane 5", labelanchor="n", bg="#757575", fg="black", font=20)
lbf6 = tk.LabelFrame(background, width=30, text="Lane 6", labelanchor="n", bg="#757575", fg="black", font=20)
lbf1.grid(row=0, column=0, columnspan=2, rowspan=4, padx=4, pady=4)
lbf2.grid(row=0, column=2, columnspan=2, rowspan=4, padx=4, pady=4)
lbf3.grid(row=0, column=4, columnspan=2, rowspan=4, padx=4, pady=4)
lbf4.grid(row=0, column=6, columnspan=2, rowspan=4, padx=4, pady=4)
lbf5.grid(row=0, column=8, columnspan=2, rowspan=4, padx=4, pady=4)
lbf6.grid(row=0, column=10, columnspan=2, rowspan=4, padx=4, pady=4)

timer1 = tk.Label(lbf1, text="00:00", bg="#000000", fg="#ff0000", font=("arial", 36))
timer2 = tk.Label(lbf2, text="00:00", bg="#000000", fg="#ff0000", font=("arial", 36))
timer3 = tk.Label(lbf3, text="00:00", bg="#000000", fg="#ff0000", font=("arial", 36))
timer4 = tk.Label(lbf4, text="00:00", bg="#000000", fg="#ff0000", font=("arial", 36))
timer5 = tk.Label(lbf5, text="00:00", bg="#000000", fg="#ff0000", font=("arial", 36))
timer6 = tk.Label(lbf6, text="00:00", bg="#000000", fg="#ff0000", font=("arial", 36))
timer1.grid(row=3, column=0, columnspan=2, sticky="ewns", padx=5, pady=5)
timer2.grid(row=3, column=2, columnspan=2, sticky="ewns", padx=5, pady=5)
timer3.grid(row=3, column=4, columnspan=2, sticky="ewns", padx=5, pady=5)
timer4.grid(row=3, column=6, columnspan=2, sticky="ewns", padx=5, pady=5)
timer5.grid(row=3, column=8, columnspan=2, sticky="ewns", padx=5, pady=5)
timer6.grid(row=3, column=10, columnspan=2, sticky="ewns", padx=5, pady=5)


ent1 = tk.Entry(lbf1, bg="#cccccc", fg="#000000", justify="center", width=8, font=("arial", 26), border=2, relief="sunken")
ent2 = tk.Entry(lbf2, bg="#cccccc", fg="#000000", justify="center", width=8, font=("arial", 26), border=2, relief="sunken")
ent3 = tk.Entry(lbf3, bg="#cccccc", fg="#000000", justify="center", width=8, font=("arial", 26), border=2, relief="sunken")
ent4 = tk.Entry(lbf4, bg="#cccccc", fg="#000000", justify="center", width=8, font=("arial", 26), border=2, relief="sunken")
ent5 = tk.Entry(lbf5, bg="#cccccc", fg="#000000", justify="center", width=8, font=("arial", 26), border=2, relief="sunken")
ent6 = tk.Entry(lbf6, bg="#cccccc", fg="#000000", justify="center", width=8, font=("arial", 26), border=2, relief="sunken")
ent1.grid(row=0, column=0, columnspan=2, sticky="ewn", padx=5, pady=5)
ent2.grid(row=0, column=2, columnspan=2, sticky="ewn", padx=5, pady=5)
ent3.grid(row=0, column=4, columnspan=2, sticky="ewn", padx=5, pady=5)
ent4.grid(row=0, column=6, columnspan=2, sticky="ewn", padx=5, pady=5)
ent5.grid(row=0, column=8, columnspan=2, sticky="ewn", padx=5, pady=5)
ent6.grid(row=0, column=10, columnspan=2, sticky="ewn", padx=5, pady=5)

#define Funtions:

def timer1Set():
	t = str(ent1.get())
	s = "00"
	global time1
	time1 = "{0}:{1}".format(t, s)
	timer1.config(text=time1)
	last = len(ent1.get())
	ent1.delete(0,last)
	startB1.config(state="active")


def timer2Set():
	t = str(ent2.get())
	s = "00"
	global time2
	time2 = "{0}:{1}".format(t, s)
	timer2.config(text=time2)
	last = len(ent2.get())
	ent2.delete(0,last)
	startB2.config(state="active")

def timer3Set():
	t = str(ent3.get())
	s = "00"
	global time3
	time3 = "{0}:{1}".format(t, s)
	timer3.config(text=time3)
	last = len(ent3.get())
	ent3.delete(0,last)
	startB3.config(state="active")

def timer4Set():
	t = str(ent4.get())
	s = "00"
	global time4
	time4 = "{0}:{1}".format(t, s)
	timer4.config(text=time4)
	last = len(ent4.get())
	ent4.delete(0,last)
	startB4.config(state="active")

def timer5Set():
	t = str(ent5.get())
	s = "00"
	global time5
	time5 = "{0}:{1}".format(t, s)
	timer5.config(text=time5)
	last = len(ent5.get())
	ent5.delete(0,last)
	startB5.config(state="active")

def timer6Set():
	t = str(ent6.get())	
	s = "00"
	global time6
	time6 = "{0}:{1}".format(t, s)
	timer6.config(text=time6)
	last = len(ent6.get())
	ent6.delete(0,last)
	startB6.config(state="active")


def timer1Update():
	try:
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
				timer1.after(1000, timer1Update)
			elif (cmins1 == 0) and (csecs1 > 0):
				timer1.config(text=str(cmins1) + ":" + str(csecs1 - 1))
				timer1.after(1000, timer1Update)
			elif (cmins1 > 0) and (csecs1 == 0):
				timer1.config(text=str(cmins1 - 1) + ":59")
				timer1.after(1000, timer1Update)
			elif (cmins1 > 0) and ((csecs1 > 0) and (csecs1 < 11)):
				timer1.config(text=str(cmins1) + ":" + ("0" + str(csecs1 - 1)))
				timer1.after(1000, timer1Update)
			elif (cmins1 > 0) and (csecs1 > 0):
				timer1.config(text=str(cmins1) + ":" + str(csecs1 - 1))
				timer1.after(1000, timer1Update)
			else:
				startB1.config(state="active")
				lane1End = tk.Tk()
				L1EndL = tk.Label(lane1End, text="Lane 1 Time Up!")
				L1EndL.pack()
				L1EndB = tk.Button(lane1End, text="Okay", command=lane1End.destroy)
				L1EndB.pack()
				lane1End.mainloop()
	except ValueError:
		startB1.config(state="active")
		lane1Oops = tk.Tk()
		L1Error = tk.Label(lane1Oops, text="Error: Please enter number of minutes only.")
		L1Error.pack()
		error1EndB = tk.Button(lane1Oops, text="my bad", command=lane1Oops.destroy)
		error1EndB.pack(pady=3)
		z1()
		lane1Oops.mainloop()

def timer2Update():
	try:
		if pauseB2.cget("state") == "disabled":
			startB2.config(state="active")
			return None
		else:
			time2 = str(timer2.cget("text"))
			ctime2 = time2.partition(":")
			cmins2, _, csecs2 = ctime2
			cmins2 = int(cmins2)
			csecs2 = int(csecs2)
			startB2.config(state="disabled")
			
			if (cmins2 == 0) and ((csecs2 > 0) and (csecs2 < 11)):
				timer2.config(text=str(cmins2) + ":" + ("0" + str(csecs2 - 1)))
				timer2.after(1000, timer2Update)
			elif (cmins2 == 0) and (csecs2 > 0):
				timer2.config(text=str(cmins2) + ":" + str(csecs2 - 1))
				timer2.after(1000, timer2Update)
			elif (cmins2 > 0) and (csecs2 == 0):
				timer2.config(text=str(cmins2 - 1) + ":59")
				timer2.after(1000, timer2Update)
			elif (cmins2 > 0) and ((csecs2 > 0) and (csecs2 < 11)):
				timer2.config(text=str(cmins2) + ":" + ("0" + str(csecs2 - 1)))
				timer2.after(1000, timer2Update)
			elif (cmins2 > 0) and (csecs2 > 0):
				timer2.config(text=str(cmins2) + ":" + str(csecs2 - 1))
				timer2.after(1000, timer2Update)
			else:
				startB2.config(state="active")
				lane2End = tk.Tk()
				L2EndL = tk.Label(lane2End, text="Lane 2 Time Up!")
				L2EndL.pack()
				L2EndB = tk.Button(lane2End, text="Okay", command=lane2End.destroy)
				L2EndB.pack()
				lane2End.mainloop()
	except ValueError:
		startB2.config(state="active")
		lane2Oops = tk.Tk()
		L2Error = tk.Label(lane2Oops, text="Error: Please enter number of minutes only.")
		L2Error.pack()
		error2EndB = tk.Button(lane2Oops, text="my bad", command=lane2Oops.destroy)
		error2EndB.pack(pady=3)
		z2()
		lane2Oops.mainloop()

def timer3Update():
	try:
		if pauseB3.cget("state") == "disabled":
			startB3.config(state="active")
			return None
		else:
			time3 = str(timer3.cget("text"))
			ctime3 = time3.partition(":")
			cmins3, _, csecs3 = ctime3
			cmins3 = int(cmins3)
			csecs3 = int(csecs3)
			startB3.config(state="disabled")

			if (cmins3 == 0) and ((csecs3 > 0) and (csecs3 < 11)):
				timer3.config(text=str(cmins3) + ":" + ("0" + str(csecs3 - 1)))
				timer3.after(1000, timer3Update)
			elif (cmins3 == 0) and (csecs3 > 0):
				timer3.config(text=str(cmins3) + ":" + str(csecs3 - 1))
				timer3.after(1000, timer3Update)
			elif (cmins3 > 0) and (csecs3 == 0):
				timer3.config(text=str(cmins3 - 1) + ":59")
				timer3.after(1000, timer3Update)
			elif (cmins3 > 0) and ((csecs3 > 0) and (csecs3 < 11)):
				timer3.config(text=str(cmins3) + ":" + ("0" + str(csecs3 - 1)))
				timer3.after(1000, timer3Update)
			elif (cmins3 > 0) and (csecs3 > 0):
				timer3.config(text=str(cmins3) + ":" + str(csecs3 - 1))
				timer3.after(1000, timer3Update)
			else:
				startB3.config(state="active")
				lane3End = tk.Tk()
				L3EndL = tk.Label(lane3End, text="Lane 3 Time Up!")
				L3EndL.pack()
				L3EndB = tk.Button(lane3End, text="Okay", command=lane3End.destroy)
				L3EndB.pack()
				lane3End.mainloop()
	except ValueError:
		startB3.config(state="active")
		lane3Oops = tk.Tk()
		L3Error = tk.Label(lane3Oops, text="Error: Please enter number of minutes only.")
		L3Error.pack()
		error3EndB = tk.Button(lane3Oops, text="my bad", command=lane3Oops.destroy)
		error3EndB.pack(pady=3)
		z3()
		lane3Oops.mainloop()

def timer4Update():
	try:
		if pauseB4.cget("state") == "disabled":
			startB4.config(state="active")
			return None
		else:
			time4 = str(timer4.cget("text"))
			ctime4 = time4.partition(":")
			cmins4, _, csecs4 = ctime4
			cmins4 = int(cmins4)
			csecs4 = int(csecs4)
			startB4.config(state="disabled")

			if (cmins4 == 0) and ((csecs4 > 0) and (csecs4 < 11)):
				timer4.config(text=str(cmins4) + ":" + ("0" + str(csecs4 - 1)))
				timer4.after(1000, timer4Update)
			elif (cmins4 == 0) and (csecs4 > 0):
				timer4.config(text=str(cmins4) + ":" + str(csecs4 - 1))
				timer4.after(1000, timer4Update)
			elif (cmins4 > 0) and (csecs4 == 0):
				timer4.config(text=str(cmins4 - 1) + ":59")
				timer4.after(1000, timer4Update)
			elif (cmins4 > 0) and ((csecs4 > 0) and (csecs4 < 11)):
				timer4.config(text=str(cmins4) + ":" + ("0" + str(csecs4 - 1)))
				timer4.after(1000, timer4Update)
			elif (cmins4 > 0) and (csecs4 > 0):
				timer4.config(text=str(cmins4) + ":" + str(csecs4 - 1))
				timer4.after(1000, timer4Update)
			else:
				startB4.config(state="active")
				lane4End = tk.Tk()
				L4EndL = tk.Label(lane4End, text="Lane 4 Time Up!")
				L4EndL.pack()
				L4EndB = tk.Button(lane4End, text="Okay", command=lane4End.destroy)
				L4EndB.pack()
				lane4End.mainloop()
	except ValueError:
		startB4.config(state="active")
		lane4Oops = tk.Tk()
		L4Error = tk.Label(lane4Oops, text="Error: Please enter number of minutes only.")
		L4Error.pack()
		error4EndB = tk.Button(lane4Oops, text="my bad", command=lane4Oops.destroy)
		error4EndB.pack(pady=3)
		z4()
		lane4Oops.mainloop()


def timer5Update():
	try:
		if pauseB5.cget("state") == "disabled":
			startB5.config(state="active")
			return None
		else:
			time5 = str(timer5.cget("text"))
			ctime5 = time5.partition(":")
			cmins5, _, csecs5 = ctime5
			cmins5 = int(cmins5)
			csecs5 = int(csecs5)
			startB5.config(state="disabled")

			if (cmins5 == 0) and ((csecs5 > 0) and (csecs5 < 11)):
				timer5.config(text=str(cmins5) + ":" + ("0" + str(csecs5 - 1)))
				timer5.after(1000, timer5Update)
			elif (cmins5 == 0) and (csecs5 > 0):
				timer5.config(text=str(cmins5) + ":" + str(csecs5 - 1))
				timer5.after(1000, timer5Update)
			elif (cmins5 > 0) and (csecs5 == 0):
				timer5.config(text=str(cmins5 - 1) + ":59")
				timer5.after(1000, timer5Update)
			elif (cmins5 > 0) and ((csecs5 > 0) and (csecs5 < 11)):
				timer5.config(text=str(cmins5) + ":" + ("0" + str(csecs5 - 1)))
				timer5.after(1000, timer5Update)
			elif (cmins5 > 0) and (csecs5 > 0):
				timer5.config(text=str(cmins5) + ":" + str(csecs5 - 1))
				timer5.after(1000, timer5Update)
			else:
				startB5.config(state="active")
				lane5End = tk.Tk()
				L5EndL = tk.Label(lane5End, text="Lane 5 Time Up!")
				L5EndL.pack()
				L5EndB = tk.Button(lane5End, text="Okay", command=lane5End.destroy)
				L5EndB.pack()
				lane5End.mainloop()
	except ValueError:
		startB5.config(state="active")
		lane5Oops = tk.Tk()
		L5Error = tk.Label(lane5Oops, text="Error: Please enter number of minutes only.")
		L5Error.pack()
		error5EndB = tk.Button(lane5Oops, text="my bad", command=lane5Oops.destroy)
		error5EndB.pack(pady=3)
		z5()
		lane5Oops.mainloop()

def timer6Update():
	try:
		if pauseB6.cget("state") == "disabled":
			startB6.config(state="active")
			return None
		else:
			time6 = str(timer6.cget("text"))
			ctime6 = time6.partition(":")
			cmins6, _, csecs6 = ctime6
			cmins6 = int(cmins6)
			csecs6 = int(csecs6)
			startB6.config(state="disabled")

			if (cmins6 == 0) and ((csecs6 > 0) and (csecs6 < 11)):
				timer6.config(text=str(cmins6) + ":" + ("0" + str(csecs6 - 1)))
				timer6.after(1000, timer6Update)
			elif (cmins6 == 0) and (csecs6 > 0):
				timer6.config(text=str(cmins6) + ":" + str(csecs6 - 1))
				timer6.after(1000, timer6Update)
			elif (cmins6 > 0) and (csecs6 == 0):
				timer6.config(text=str(cmins6 - 1) + ":59")
				timer6.after(1000, timer6Update)
			elif (cmins6 > 0) and ((csecs6 > 0) and (csecs6 < 11)):
				timer6.config(text=str(cmins6) + ":" + ("0" + str(csecs6 - 1)))
				timer6.after(1000, timer6Update)
			elif (cmins6 > 0) and (csecs6 > 0):
				timer6.config(text=str(cmins6) + ":" + str(csecs6 - 1))
				timer6.after(1000, timer6Update)
			else:
				startB6.config(state="active")
				lane6End = tk.Tk()
				L6EndL = tk.Label(lane6End, text="Lane 6 Time Up!")
				L6EndL.pack()
				L6EndB = tk.Button(lane6End, text="Okay", command=lane6End.destroy)
				L6EndB.pack()
				lane6End.mainloop()
	except ValueError:
		startB6.config(state="active")
		lane6Oops = tk.Tk()
		L6Error = tk.Label(lane6Oops, text="Error: Please enter number of minutes only.")
		L6Error.pack()
		error6EndB = tk.Button(lane6Oops, text="my bad", command=lane6Oops.destroy)
		error6EndB.pack(pady=3)
		z6()
		lane6Oops.mainloop()


def z1():
	timer1.config(text="00:00")

def z2():
	timer2.config(text="00:00")

def z3():
	timer3.config(text="00:00")

def z4():
	timer4.config(text="00:00")

def z5():
	timer5.config(text="00:00")

def z6():
	timer6.config(text="00:00")


setB1 = tk.Button(lbf1, text="Set Time", justify="left", command=timer1Set)
setB2 = tk.Button(lbf2, text="Set Time", justify="left", command=timer2Set)
setB3 = tk.Button(lbf3, text="Set Time", justify="left", command=timer3Set)
setB4 = tk.Button(lbf4, text="Set Time", justify="left", command=timer4Set)
setB5 = tk.Button(lbf5, text="Set Time", justify="left", command=timer5Set)
setB6 = tk.Button(lbf6, text="Set Time", justify="left", command=timer6Set)
setB1.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
setB2.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
setB3.grid(row=1, column=4, sticky="ew", padx=5, pady=5)
setB4.grid(row=1, column=6, sticky="ew", padx=5, pady=5)
setB5.grid(row=1, column=8, sticky="ew", padx=5, pady=5)
setB6.grid(row=1, column=10, sticky="ew", padx=5, pady=5)

def setB1state():
	if ent1.get() == "":
		setB1.config(state="disabled")
		setB1.after(1000, setB1state)
	else:
		setB1.config(state="active")
		setB1.after(1000, setB1state)

def setB2state():
	if ent2.get() == "":
		setB2.config(state="disabled")
		setB2.after(1000, setB2state)
	else:
		setB2.config(state="active")
		setB2.after(1000, setB2state)

def setB3state():
	if ent3.get() == "":
		setB3.config(state="disabled")
		setB3.after(1000, setB3state)
	else:
		setB3.config(state="active")
		setB3.after(1000, setB3state)

def setB4state():
	if ent4.get() == "":
		setB4.config(state="disabled")
		setB4.after(1000, setB4state)
	else:
		setB4.config(state="active")
		setB4.after(1000, setB4state)

def setB5state():
	if ent5.get() == "":
		setB5.config(state="disabled")
		setB5.after(1000, setB5state)
	else:
		setB5.config(state="active")
		setB5.after(1000, setB5state)

def setB6state():
	if ent6.get() == "":
		setB6.config(state="disabled")
		setB6.after(1000, setB6state)
	else:
		setB6.config(state="active")
		setB6.after(1000, setB6state)

pauseB1 = tk.Button(lbf1,  width=5, text="Pause", command=lambda:((pauseB1.config(state="disabled")),(pauseB1.after(1000, lambda:(pauseB1.config(state="active"))))))
pauseB2 = tk.Button(lbf2, width=5, text="Pause", command=lambda:((pauseB2.config(state="disabled")),(pauseB2.after(1000, lambda:(pauseB2.config(state="active"))))))
pauseB3 = tk.Button(lbf3, width=5, text="Pause", command=lambda:((pauseB3.config(state="disabled")),(pauseB3.after(1000, lambda:(pauseB3.config(state="active"))))))
pauseB4 = tk.Button(lbf4, width=5, text="Pause", command=lambda:((pauseB4.config(state="disabled")),(pauseB4.after(1000, lambda:(pauseB4.config(state="active"))))))
pauseB5 = tk.Button(lbf5, width=5, text="Pause", command=lambda:((pauseB5.config(state="disabled")),(pauseB5.after(1000, lambda:(pauseB5.config(state="active"))))))
pauseB6 = tk.Button(lbf6, width=5, text="Pause", command=lambda:((pauseB6.config(state="disabled")),(pauseB6.after(1000, lambda:(pauseB6.config(state="active"))))))
pauseB1.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
pauseB2.grid(row=2, column=3, sticky="ew", padx=5, pady=5)
pauseB3.grid(row=2, column=5, sticky="ew", padx=5, pady=5)
pauseB4.grid(row=2, column=7, sticky="ew", padx=5, pady=5)
pauseB5.grid(row=2, column=9, sticky="ew", padx=5, pady=5)
pauseB6.grid(row=2, column=11, sticky="ew", padx=5, pady=5)

startB1 = tk.Button(lbf1, text="Start", justify="center", command=timer1Update)
startB2 = tk.Button(lbf2, text="Start", justify="center", command=timer2Update)
startB3 = tk.Button(lbf3, text="Start", justify="center", command=timer3Update)
startB4 = tk.Button(lbf4, text="Start", justify="center", command=timer4Update)
startB5 = tk.Button(lbf5, text="Start", justify="center", command=timer5Update)
startB6 = tk.Button(lbf6, text="Start", justify="center", command=timer6Update)
startB1.grid(row=1, column=1, sticky="we", padx=5, pady=5)
startB2.grid(row=1, column=3, sticky="we", padx=5, pady=5)
startB3.grid(row=1, column=5, sticky="we", padx=5, pady=5)
startB4.grid(row=1, column=7, sticky="we", padx=5, pady=5)
startB5.grid(row=1, column=9, sticky="we", padx=5, pady=5)
startB6.grid(row=1, column=11, sticky="we", padx=5, pady=5)

clearB1 = tk.Button(lbf1, text="Clear", justify="right", command=z1)
clearB2 = tk.Button(lbf2, text="Clear", justify="right", command=z2)
clearB3 = tk.Button(lbf3, text="Clear", justify="right", command=z3)
clearB4 = tk.Button(lbf4, text="Clear", justify="right", command=z4)
clearB5 = tk.Button(lbf5, text="Clear", justify="right", command=z5)
clearB6 = tk.Button(lbf6, text="Clear", justify="right", command=z6)
clearB1.grid(row=2, column=0, sticky="we", padx=5, pady=5)
clearB2.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
clearB3.grid(row=2, column=4, sticky="ew", padx=5, pady=5)
clearB4.grid(row=2, column=6, sticky="ew", padx=5, pady=5)
clearB5.grid(row=2, column=8, sticky="ew", padx=5, pady=5)
clearB6.grid(row=2, column=10, sticky="ew", padx=5, pady=5)

setB1state()
setB2state()
setB3state()
setB4state()
setB5state()
setB6state()

root.mainloop()
