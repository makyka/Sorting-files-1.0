from tkinter import *
from tkinter import filedialog, Tk, Label, Entry, Button
import shutil
import os

def move_files():
    directory = filedialog.askdirectory(title='Open a folder')
    if directory:
        # Get a list of files in the selected directory
        files = os.listdir(directory)
        # Convert the list of files to a string
        files_str = '\n'.join(files)
        # Pass the files string to the Entry widget
        field_2.delete(1.0, END)
        field_2.insert(END, files_str)
        # Get the list of files in the directory
        files = os.listdir(directory)
        destination_folder = filedialog.askdirectory(title='Select a folder')
        # Prompt the user to enter a step and index value
        step = int(entry_1.get())
        index = int(entry_2.get())
        if destination_folder:
            for index in range(1, len(destination_folder), step):
                # Get the full path of the file
                
                file_path = os.path.join(directory, files[index])

                # Move the file to the destination folder
                shutil.move(file_path, destination_folder)

            # Display a notification
            field_3.insert("1.0", "Files were successfully moved to the new folder!")
            

Window = Tk()
Window.title("Sorting files 1.0")
Window.geometry("700x700+500+200")
Window.configure(bg="#7B68EE")
Window.resizable(False, False)
# Frame for two buttons.
frame_1 = Frame(Window, width=500, height=100, bg="#6495ED")
frame_1.place(x=100, y=20) # 1 фрейм
# Frame for widget text. Field text.
frame_2 = Frame(Window, width=300, height=350, bg="#6495ED")
frame_2.place(x=100, y=120)
label = Label(frame_2, text="Info")
label.pack(padx=20, pady=10)
field_2 = Text(frame_2, width=65, height=20, wrap=WORD, bg="blue", font=('Arial', 10), fg="white")
field_2.pack(padx=20, pady=6)
# Frame for the text widget with the notification "files have been successfully moved to a new folder"
frame_3 = Frame(Window, width=500, height=70, bg="#6495ED")
frame_3.place(x=100, y=550)
field_3 = Text(frame_3, width=65, height=5, wrap=WORD, bg="blue", font=('Arial', 10), fg="white")
field_3.pack(padx=20, pady=6)
# Two buttons for frame_1. Entry widget for frame_1

btn_2 = Button(frame_1, text="Select", bg="#BC8F8F", fg="#4B0082", command=move_files)
btn_2.pack(side=LEFT, padx=50, pady=1)

label_1 = Label(frame_1, text="Step")
label_1.pack(side=LEFT, padx=1, pady=1)
entry_1 = Entry(frame_1, width=5, borderwidth=3, bg="yellow")
entry_1.pack(side=LEFT, padx=10, pady=1)

label_2 = Label(frame_1, text="Index")
label_2.pack(side=LEFT, padx=3, pady=1)
entry_2 = Entry(frame_1, width=5, borderwidth=3)
entry_2.pack(side=LEFT, padx=3, pady=1)


Window.mainloop()