import customtkinter as ctk
import os

def browse_button():
    filename = ctk.filedialog.askdirectory()
    folder_path.delete(0,ctk.END)
    folder_path.insert(0,filename)

def pack_mcmeta():
    mcmeta_path = os.path.join(folder_path.get() + '\\' + name.get(), 'pack.mcmeta')
    pack_mcmeta = open(mcmeta_path, 'w+')
    mcmeta_content = '{\n    "pack": {\n        "pack_format": ' + pack_format.get() + ',\n        "description": "' + description.get() + '"\n    }\n}'
    pack_mcmeta.write(mcmeta_content)
    pack_mcmeta.close()
    
def function_tags():
    os.makedirs(folder_path.get() + '\\' + name.get() + '\\data\\minecraft\\tags\\function')
    load_path = os.path.join(folder_path.get() + '\\' + name.get() + '\\data\\minecraft\\tags\\function', 'load.json')
    load = open(load_path, 'w+')
    load_contents = '{\n    "replace": false,\n    "values": [\n        "' + namespace.get() + ':load"\n    ]\n}'
    load.write(load_contents)
    load.close()
    
    tick_path = os.path.join(folder_path.get() + '\\' + name.get() + '\\data\\minecraft\\tags\\function', 'tick.json')
    tick = open(tick_path, 'w+')
    tick_contents = '{\n    "replace": false,\n    "values": [\n        "' + namespace.get() + ':tick"\n    ]\n}'
    tick.write(tick_contents)
    tick.close()

def tick_load_functions():
    os.makedirs(folder_path.get() + '\\' + name.get() + '\\data\\' + namespace.get() + '\\function')
    load_function_path = os.path.join(folder_path.get() + '\\' + name.get() + '\\data\\' + namespace.get() + '\\function', 'load.mcfunction')
    load_function = open(load_function_path, 'x')
    load_function_contents = 'tellraw @a "Reloaded!"\n\n'
    load_function.write(load_function_contents)
    load_function.close()
    tick_function_path = os.path.join(folder_path.get() + '\\' + name.get() + '\\data\\' + namespace.get() + '\\function', 'tick.mcfunction')
    tick_function = open(tick_function_path, 'x')
    tick_function.close()

def create_datapack():
    name_exists.destroy()
    fill_fields.destroy()
    pack_mcmeta()
    function_tags()
    tick_load_functions()

def check_name():
    try:
        os.makedirs(folder_path.get() + '\\' + name.get(), exist_ok=False)
    except FileExistsError:
        name_exists.place(relx = 0.55, rely = 0.15)
        return
    create_datapack()

def check_if_fields_filled():
    if len(folder_path.get()) > 0 and len(name.get()) > 0 and len(pack_format.get()) > 0 and len(description.get()) > 0 and len(namespace.get()) > 0:
        check_name()
    else:
        fill_fields.place(relx = 0.19, rely = 0.9)
        return

root = ctk.CTk()

root.geometry("700x400")
root.title("Datapack Creator")

frame = ctk.CTkFrame(root, width = 570, height = 330, fg_color = 'transparent')
frame.pack_propagate(0)
frame.pack(pady = 20)

folder_path_text = ctk.CTkLabel(frame, text = "Folder Path", font = ('consolas', 15, 'bold'), text_color = ('black', 'white'))
folder_path_text.place(relx = 0.02, rely = 0.10)
folder_path = ctk.CTkEntry(frame, width = 400, font = ("consolas", 15))
folder_path.place(relx = 0.19, rely = 0.10)

browse = ctk.CTkButton(frame, command = browse_button, text = "Browse", width = 20, font = ('consolas', 15), text_color = ('black', 'white'))
browse.place(relx = 0.89, rely = 0.10)

name_text = ctk.CTkLabel(frame, text = "Name", font = ('consolas', 15, 'bold'), text_color = ('black', 'white'))
name_text.place(relx = 0.02, rely = 0.20)
name = ctk.CTkEntry(frame, width = 200, font = ("consolas", 15))
name.place(relx = 0.19, rely = 0.20)

name_exists = ctk.CTkLabel(frame, text = "FOLDER ALREADY EXISTS", font = ('consolas', 15, 'bold'), text_color = ('red', 'red'))

namespace_text = ctk.CTkLabel(frame, text = "Namespace", font = ('consolas', 15, 'bold'), text_color = ('black', 'white'))
namespace_text.place(relx = 0.02, rely = 0.30)
namespace = ctk.CTkEntry(frame, font = ("consolas", 15))
namespace.place(relx = 0.19, rely = 0.30)

pack_format_text = ctk.CTkLabel(frame, text = "Pack Format", font = ('consolas', 15, 'bold'), text_color = ('black', 'white'))
pack_format_text.place(relx = 0.02, rely = 0.40)
pack_format = ctk.CTkEntry(frame, width = 40, font = ("consolas", 15))
pack_format.place(relx = 0.19, rely = 0.40)

description_text = ctk.CTkLabel(frame, text = "Description", font = ('consolas', 15, 'bold'), text_color = ('black', 'white'))
description_text.place(relx = 0.02, rely = 0.50)
description = ctk.CTkEntry(frame, width = 460, font = ("consolas", 15))
description.place(relx = 0.19, rely = 0.50)

create_datapack_button = ctk.CTkButton(frame, command = check_if_fields_filled, text = "Create Datapack", font = ('consolas', 15), text_color = ('black', 'white'))
create_datapack_button.place(relx = 0.37, rely = 0.8)
fill_fields = ctk.CTkLabel(frame, text = "Fill all fields before attempting again", font = ('consolas', 15, 'bold'), text_color = ('red', 'red'))

root.mainloop()
