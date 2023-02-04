import customtkinter

# Add custom file for font

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

# Iniitialzing login frame
login_win = customtkinter.CTk()
login_frame = customtkinter.CTkFrame(master = login_win, height = 370, width = 350)
login_frame.place(relx = 0.5, rely = 0.51, anchor = customtkinter.CENTER)

login_win.geometry('400x500')

# All functions 
def change_frame():
    pass

# initialize the widget
login_widget = customtkinter.CTkLabel(master = login_win, text = 'Sign Up')
first_name_label = customtkinter.CTkLabel(master = login_frame, text = 'Enter your First Name')
first_name_entry = customtkinter.CTkEntry(master = login_frame, placeholder_text= 'Firstname', height=20, width=150)
last_name_label = customtkinter.CTkLabel(master = login_frame, text= 'Enter your Last Name')
last_name_entry = customtkinter.CTkEntry(master = login_frame, placeholder_text='Lastname')
username_label = customtkinter.CTkLabel(master = login_frame, text = "Set your Username")
username_entry = customtkinter.CTkEntry(master = login_frame, placeholder_text = 'Username of minimum 8 characters')

# Submit Button 
submit_button = customtkinter.CTkButton(master = login_win, text="Submit")

#Password 
password_label = customtkinter.CTkLabel(master = login_frame, text = 'Password')
password_entry = customtkinter.CTkEntry(master = login_frame, placeholder_text='Password')

# configure font 
login_widget.configure(font = ('Courier', 25))
first_name_entry.configure(font = (9), width = 250)
first_name_label.configure(font = ('Comic Sans Ms',12))
last_name_entry.configure(font = (9), width = 250)
last_name_label.configure(font = ('Comic Sans Ms', 12))
username_label.configure(font = ("Comic Sans Ms", 12))
username_entry.configure(font = (11), width = 250)
password_label.configure(font = ("Comic Sans Ms", 12))
password_entry.configure(font = (11), width = 250)

# place the widget on the window
login_widget.place(relx = 0.5, rely = 0.065, anchor = customtkinter.CENTER)
first_name_label.place(relx = 0.1, rely = 0.07, anchor = customtkinter.W)
first_name_entry.place(relx = 0.1, rely = 0.16, anchor = customtkinter.W)
last_name_label.place(relx = 0.1, rely = 0.26, anchor = customtkinter.W)
last_name_entry.place(relx = 0.1, rely = 0.35, anchor = customtkinter.W)
username_label.place(relx=0.09, rely=0.45, anchor = customtkinter.W)
username_entry.place(relx=0.1, rely=0.54, anchor = customtkinter.W)
password_label.place(relx = 0.01, rely = 0.64, anchor = customtkinter.W)
password_entry.place(relx = 0.1, rely = 0.73, anchor = customtkinter.W)

submit_button.place(relx = 0.6, rely = 0.95, anchor = customtkinter.E)

login_win.mainloop()
