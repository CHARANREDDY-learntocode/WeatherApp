import tkinter as tk
from PIL import Image,ImageTk

import weather

def heading():

	head_frame=tk.Frame(root)
	head_frame.place(relwidth=1,relheight=0.2)

	heading_label=tk.Label(head_frame,text="Live Weather Report",font="Times 32 bold",bg="#5ca19e")
	heading_label.place(relwidth=1,relheight=1)

def entry_box():
	global city_name
	entry_frame=tk.Frame(root,bg="#7797b8")
	entry_frame.place(rely=0.2,relwidth=1,relheight=0.1)

	label=tk.Label(entry_frame,text="Enter City Name",bg="#7797b8",font="Arial 14")
	label.place(relheight=1,relwidth=0.25)

	city_name=tk.StringVar()

	city=tk.Entry(entry_frame,font="Arial 14",textvariable=city_name)
	city.place(relx=0.25,rely=0.05,relwidth=0.45,relheight=0.9)

	submit=tk.Button(entry_frame,text="Get Weather",font="Arial 14",command=lambda: show_weather(city_name.get()))
	submit.place(relx=0.71,rely=0.05,relwidth=0.28,relheight=0.9)

def show_weather(city):

	global image_frame

	try:
		info_frame.destroy()
		
	except:
		pass

	try:

		image_frame.destroy()

	except:
		pass
	
	info_frame=tk.Frame(root,bg="#ffffff")
	info_frame.place(rely=0.3,relwidth=0.55,relheight=0.7)

	if len(city)<2:
		return

	info=weather.call_api(city)
	print(info)
	if info!=None:

		try:
			if len(info)==5:

				for row in range(4):
					info_frame.rowconfigure(row,weight=1)
				
				info_label=tk.Label(info_frame,text="City-Country:",font="Helvectica 14",anchor="w",bg="#ffffff")
				info_label.grid(row=0,column=0,padx=2,pady=2,sticky="ew")

				info_label=tk.Label(info_frame,text="Temparature:",font="Helvectica 14",bg="#ffffff",anchor="w")
				info_label.grid(row=1,column=0,padx=2,pady=2,sticky="ew")

				info_label=tk.Label(info_frame,text="Weather:",font="Helvectica 14",anchor="w",bg="#ffffff")
				info_label.grid(row=2,column=0,padx=2,pady=2,sticky="ew")

				info_label=tk.Label(info_frame,text="Description:",font="Helvectica 14",anchor="w",bg="#ffffff")
				info_label.grid(row=3,column=0,padx=2,pady=2,sticky="ew")

				info_label=tk.Label(info_frame,text=str(info[0]+"  "+info[1]),font="Helvectica 14",anchor="w",bg="#ffffff")
				info_label.grid(row=0,column=1,sticky="ew")
				
				info_label=tk.Label(info_frame,text=info[2],font="Helvectica 14",anchor="w",bg="#ffffff")
				info_label.grid(row=1,column=1,sticky="ew")
				
				info_label=tk.Label(info_frame,text=info[3],font="Helvectica 14",anchor="w",bg="#ffffff")
				info_label.grid(row=2,column=1,sticky="ew")

				info_label=tk.Label(info_frame,text=info[4],font="Helvectica 11",anchor="w",bg="#ffffff")
				info_label.grid(row=3,column=1,sticky="ew")

				#Display picture
				image_frame=tk.Frame(root,bg="#ffffff")
				image_frame.place(relx=0.55,relwidth=0.45,relheight=0.7,rely=0.3)

				image_list=["drizzle.png",'thunderstorm.png','cloud.png','clear.png', 'fog.png','haze.png','scatterd.png', 'sunny.jpg','mist.png','rain.png']
				
				for image in image_list:
					if image[:3]==(info[3].lower())[:3]:
						print(image)
						try:
							img=ImageTk.PhotoImage(Image.open(image))

							img_lbl=tk.Label(image_frame,image=img)
							img_lbl.image=img
							img_lbl.pack(side="top")
							break
						except:
							break


		except:

			if info==-1:

				info_label=tk.Label(info_frame,text="Something goes wrong",font="Helvectica 14",bg="#ffffff",anchor="w")
				info_label.grid(row=0,column=0,padx=2,pady=2,sticky="ew")

			elif info==401:

				info_label=tk.Label(info_frame,text="Invalid API key",bg="#ffffff",font="Helvectica 14",anchor="w")
				info_label.grid(row=0,column=0,padx=2,pady=2,sticky="ew")

			elif info==404:

				info_label=tk.Label(info_frame,text="No city found",bg="#ffffff",font="Helvectica 14",anchor="w")
				info_label.grid(row=0,column=0,padx=2,pady=2,sticky="ew")


	else:

		info_label=tk.Label(info_frame,text="No internet connection",bg="#ffffff",font="Helvectica 14",anchor="w")
		info_label.grid(row=0,column=0,padx=2,pady=2,sticky="ew")

def enter(event):
	show_weather(city_name.get())


def decorate():

	global root,canvas

	root=tk.Tk()
	root.title("Weather App")
	root.configure(bg="#ffffff")
	root.iconbitmap("icon.ico")
	screen_width,screen_height=root.winfo_screenwidth(),root.winfo_screenheight()
	root.geometry("600x350"+"+"+str(int(0.2*screen_width))+"+"+str(int(0.07*screen_height)))
	root.resizable(0,0)


	heading()
	entry_box()
	show_weather
	root.bind('<Return>',enter)
	root.mainloop()

decorate()
