##importing tkinter and a custom library
import tkinter
import customtkinter as ct
#importing my BoneManager library
import BoneManager
#see what files are in the 'drop mods folder'
BoneManager.findFiles()

#activate tkinter
app = ct.CTk()
#tkinter window size
app.geometry("400x600")
#the title of the tkinter window
app.title("BLI renderer window")
#setting the color theme to green
ct.set_default_color_theme("green")
#put the BLI image as the window icon
img = tkinter.PhotoImage(file='BLinstallericon.png')
app.iconphoto(False, img)

#attach files to the bonelab mods folder
attach_button = ct.CTkButton( text = "Attach to bonelab", command=BoneManager.extractall)
#render the attach to bonelab button
attach_button.pack(pady=10)
#open the dropmods folder button
drop_button = ct.CTkButton( text = "open dropmods folder", command=BoneManager.openmodsfolder)
#render the dropmods folder button
drop_button.pack()
#tutoiral text
tutorial_text = ct.CTkLabel( text="put .zip files in the 'dropmods' folder",justify=tkinter.LEFT)
#render the tutoiral text
tutorial_text.pack()
#make a frame for the detector
frame = ct.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill="both", expand=True)



#draw text for every .zip file in dropmods folder
for mod in BoneManager.mods_list:
    modtext = ct.CTkLabel( text=mod,master=frame, justify=tkinter.LEFT)
    modtext.pack()

#detect if the are more files in the drop mods folder
detect_button = ct.CTkButton(text = "detect files" ,command=BoneManager.update)
detect_button.pack(pady=10)
#leave button to leave the app
leave_button = ct.CTkButton(text = "leave program" ,command=app.destroy)
#render leave button
leave_button.pack()



app.mainloop()