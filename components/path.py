import tkinter as tk


# get the path of a selected file
def get_path():
    root = tk.Tk()
    root.withdraw()
    file_path = tk.filedialog.askopenfilename()
    return file_path


# define the id of the file
def get_id(file_path="/contracts"):
    id = file_path.split("/")[-1]
    return id
