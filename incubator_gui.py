# Incubator software v0.0.1
# Jasen Finch April 2013
# First attemped at incubator_pi software GUI layout

from Tkinter import *
class Application(Frame):
	""" The main GUI menu application for the incubator software. """
	def __init__ (self, master):
		""" Initialize the frame. """
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
	
	def create_widgets(self):
		""" Create widgets for layout. """
		# create instruction label
		self.init_lbl = Label(self,text = "Enter options for incubator settings")
		self.init_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		
		# create label for type
		self.type_lbl = Label(self, text = "Egg Type: ")
		self.type_lbl.grid(row = 1, column = 0, sticky = W)
		
		# create dropdown box of type entry
		optionList = ("Chicken","Duck","Goose")
		self.t = StringVar()
		self.typ_drop = OptionMenu(self, self.t, *optionList)
		self.typ_drop.grid(row = 1, column = 1, sticky = W)
		
		# create label for length
		self.len_lbl = Label(self, text = "Incubation Length (days): ")
		self.len_lbl.grid(row = 2, column = 0, sticky = W)
		
		# create entry widget to accept length
		self.l =StringVar()
		self.len_ent = Entry(self,textvariable=self.l)
		self.len_ent.grid(row = 2, column = 1, sticky = W)
		
		# create label for temp
		self.temp_lbl = Label(self, text = "Temperature: ")
		self.temp_lbl.grid(row = 3, column = 0, sticky = W)
		
		# create entry widget to accept temp
		self.tem =StringVar()
		self.temp_ent = Entry(self,textvariable=self.tem)
		self.temp_ent.grid(row = 3, column = 1, sticky = W)
		
		# create label for temp tolerance
		self.temp_tol_lbl = Label(self, text = "Tolerance (+/-): ")
		self.temp_tol_lbl.grid(row = 3, column = 2, sticky = W)
		
		# create entry widget to accept temp tolerance
		self.tem_tol = StringVar()
		self.temp_tol_ent = Entry(self,textvariable=self.tem_tol)
		self.temp_tol_ent.grid(row = 3, column = 3, sticky = W)
		
		# create label for humidity
		self.hum_lbl = Label(self, text = "Humidity (%): ")
		self.hum_lbl.grid(row = 4, column = 0, sticky = W)
		
		# create entry widget to accept humidity
		self.hum =StringVar()
		self.hum_ent = Entry(self,textvariable=self.hum)
		self.hum_ent.grid(row = 4, column = 1, sticky = W)
		
		# create label for humidity tolerance
		self.hum_tol_lbl = Label(self, text = "Tolerance (+/-): ")
		self.hum_tol_lbl.grid(row = 4, column = 2, sticky = W)
		
		# create entry widget to accept humidity tolerance
		self.hum_tol = StringVar()
		self.hum_tol_ent = Entry(self,textvariable=self.hum_tol)
		self.hum_tol_ent.grid(row = 4, column = 3, sticky = W)
		
		# create submit button
		self.submit_bttn = Button(self, text = "Apply Defaults", command = self.reveal)
		self.submit_bttn.grid(row = 1, column = 3, sticky = W)
		
		# create next button
		self.next_bttn = Button(self, text = "Next")
		self.next_bttn.grid(row = 5, column = 5, sticky = W)
		
		#create text widget to display message
		#self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
		#self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

	def reveal(self):
		""" Display defaults based on egg type. """
		contents = self.t.get()
		if contents== "Chicken":
			leng = "20?"
			Tem = "37.5"
			Hum = "70"
			t_tol = "1"
			h_tol = "10"
		elif contents== "Goose":
			leng = "25"
			Tem = "37.5"
			Hum = "70"
			t_tol = "1"
			h_tol = "10"
		elif contents== "Duck":
			leng = "23"
			Tem = "37.5"
			Hum = "70"
			t_tol = "1"
			h_tol = "10"
		self.l.set(leng)
		self.tem.set(Tem)
		self.hum.set(Hum)
		self.tem_tol.set(t_tol)
		self.hum_tol.set(h_tol)
	
#	def nex (self):
#		self.count += 1
   #     id = "New window #%s" % self.count
  #      window = Toplevel(self)
 #       label = Label(window, text=id)
#        label.pack(side="top", fill="both", padx=10, pady=10)
		

# main
root = Tk()
root.title("Incubator")
root.geometry("600x150")
app = Application(root)

root.mainloop()
