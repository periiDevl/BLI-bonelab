##importing tkinter library
import tkinter
#importing my BoneManager library
import BoneManager
#see what files are in the 'drop mods folder'
BoneManager.findFiles()

#activate tkinter
app = tkinter.Tk()
#tkinter window size
app.geometry("400x600")
#the title of the tkinter window
app.title("detector inspector")

#put the BLI image as the window icon
img = tkinter.PhotoImage(file='BLinstallericon.png')
app.iconphoto(False, img)

#attach files to the bonelab mods folder
attach_button = tkinter.Button( text = "Attach to bonelab", command=BoneManager.extractall)
#render the attach to bonelab button
attach_button.pack(pady=10)
#open the dropmods folder button
drop_button = tkinter.Button( text = "open dropmods folder", command=BoneManager.openmodsfolder)
#render the dropmods folder button
drop_button.pack()
#tutoiral text
tutorial_text = tkinter.Label( text="put .zip files in the 'dropmods' folder",justify=tkinter.LEFT)
#render the tutoiral text
tutorial_text.pack()
#make a frame for the detector
frame = tkinter.Frame(master=app)
frame.pack(pady=20, padx=40, fill="both", expand=True)

#draw text for every .zip file in dropmods folder
for mod in BoneManager.mods_list:
    modtext = tkinter.Label( text=mod,master=frame, justify=tkinter.LEFT)
    modtext.pack()

#detect if the are more files in the drop mods folder
detect_button = tkinter.Button(text = "detect files" ,command=BoneManager.update)
detect_button.pack(pady=10)
#leave button to leave the app
leave_button = tkinter.Button(text = "leave program" ,command=app.destroy)
#render leave button
leave_button.pack()



app.mainloop()