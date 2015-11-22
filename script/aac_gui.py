#!/usr/bin/python3

import os
from tkinter import *

version = "1.0_151115"

#ManagingTKinter
aac = Tk()
frame_1 = aac
aac.minsize(width=400, height=440)
aac.maxsize(width=400, height=440)

#InitialisationFrame
def init():
	def create():
		os.system("mkdir -p " + folder_name.get())
		os.chdir(folder_name.get())
		java_init = canvas.create_text(190, 150, text="Succesfully initialized. Now hit Install/Update Java.")

	def dl_java():
		os.system("sudo apt-add-repository ppa:webupd8team/java && sudo apt-get update && sudo apt-get install oracle-java7-installer")
		java_done = canvas.create_text(190, 170, text="Okay, java is ready to work !")

	def dl_prgms():
		os.system("sudo apt-get install git-core gnupg flex bison gperf build-essential \
  		zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
	  	lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
	  	libgl1-mesa-dev libxml2-utils xsltproc unzip lzop")
		prgms_done = canvas.create_text(190, 190, text="All downloads done.")
	frame_1 = aac
	frame_1.title("Android Auto Compiler " + version)
	canvas = Canvas(frame_1)
	welcome = canvas.create_text(190, 70, text="Welcome on AAC GUI " + version, fill="blue")
	tips = canvas.create_text(190, 100, text="  You need to launch this program \nwhere you want to see your sources.")
	btn_create = Button(frame_1, text="Create", command=create)
	btn_update_java = Button(frame_1, text="Install/Update Java", command=dl_java)
	btn_dl_prgms = Button(frame_1, text="Download/Update Useful Programs", command=dl_prgms)
	folder_name = StringVar() 
	text_entry = Entry(frame_1, textvariable=folder_name, width=30)
	text_variable = folder_name.get()
	canvas.pack()
	text_entry.pack()
	btn_create.pack()
	btn_update_java.pack()
	btn_dl_prgms.pack()
	
#DownloadFrame
def dl():
	frame_2 = aac
	frame_2.title("Sources Download Options")
	canvas = Canvas(frame_2)
	tips_2 = canvas.create_text(190, 70, text="	Tell me wich sources you want to build.\n You have CyanogenMod, AOSP, AOKP, Paranoid.")	
	canvas.pack()
	#OptionMenu For Source Choose
	options = StringVar(aac)
	options.set("AOSP")
	w = OptionMenu(aac, options, "CyanogenMod", "AOSP", "AOKP", "Paranoid", "OmniROM")
	w.pack()
	#OptionMenu for Branches
	if options.get() == "CyanogenMod":
		opt_branch = StringVar(aac)
		w = OptionMenu(aac, opt_branch, "cm-12.0", "cm-12.1", "cm-13.0")
		w.pack()
	if options.get() == "AOSP":
		opt_branch = StringVar(aac)
		w = OptionMenu(aac, opt_branch, "android-5.1.1_r29", "android-6.0.0_r26")
		w.pack()
	if options.get() == "AOKP":
		opt_branch = StringVar(aac)
		w = OptionMenu(aac, opt_branch, "Lollipop", "Jelly Bean")
		w.pack()
	if options.get() == "Paranoid":
		opt_branch = StringVar(aac)
		w = OptionMenu(aac, opt_branch, "Marshmallow", "Lollipop")
		w.pack()

def build():
	def build_btn():
		os.system("source build/envsetup.sh && brunch " + device_name.get())
	frame_3 = aac
	frame_3.title("Build Options")
	canvas = Canvas(frame_3)
	tip = canvas.create_text(190, 70, text="Here you can build your ROM.")
	tip_2 = canvas.create_text(190, 90, text="Write down your device name then hit the build button.")
	device_name = StringVar() 
	text_entry = Entry(frame_1, textvariable=device_name, width=30)
	text_variable = device_name.get()
	build_btn = Button(frame_3, text="Build Now", command=build_btn)
	canvas.pack()
	text_entry.pack()
	build_btn.pack()
	frame_3.mainloop()
	frame_1.destroy()
	
#Menu
menubar = Menu(frame_1)
menubar.add_command(label="Initialisation", command=init)
menubar.add_command(label="Download Source", command=dl)
menubar.add_command(label="Build for my device", command=build)
menubar.add_command(label="Quit", command=frame_1.quit)

#Display that menu
frame_1.config(menu=menubar)
frame_1.mainloop()


