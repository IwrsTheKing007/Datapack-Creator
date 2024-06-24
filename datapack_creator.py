import customtkinter as ctk
import os
import webbrowser
import json

def pack_format_link():
    webbrowser.open_new("https://minecraft.wiki/w/Pack_format#List_of_data_pack_formats")

def browse_button():
    filename = ctk.filedialog.askdirectory()
    folder_path.delete(0,ctk.END)
    folder_path.insert(0,filename)

def create_datapack():
    name_exists.destroy()
    fill_fields.destroy()
    pack_format_value_error.destroy()
    pack_mcmeta()
    namespace_path = folder_path.get() + '\\' + name.get() + '\\data\\' + namespace.get()
    namespace_folder(namespace_path)
    if load_json_checkbox.get() == 1 or tick_json_checkbox.get() == 1:
        load_tick_functions(namespace_path)
        function_tags()
    if advancement_checkbox.get() == 1:
        advancement(namespace_path)
    if loot_table_checkbox.get() == 1:
        loot_table(namespace_path)
    if recipe_checkbox.get() == 1:
        recipe(namespace_path)
    if tags_checkbox.get() == 1:
        tags(namespace_path)

def pack_mcmeta():
    mcmeta_path = os.path.join(folder_path.get() + '\\' + name.get(), 'pack.mcmeta')
    pack_mcmeta = open(mcmeta_path, 'w+')
    mcmeta_json = {
        "pack": {
            "pack_format": int(pack_format.get()),
            "description": description.get()
        }
    }
    mcmeta_content = json.dumps(mcmeta_json, indent = 4)
    pack_mcmeta.write(mcmeta_content)
    pack_mcmeta.close()
    
def namespace_folder(namespace_path):
    os.makedirs(namespace_path)
    
def load_tick_functions(namespace_path):
    os.makedirs(namespace_path + '\\functions')
    if load_json_checkbox.get() == 1:
        load_function_path = os.path.join(namespace_path + '\\functions', 'load.mcfunction')
        load_function = open(load_function_path, 'x')
        load_function_contents = 'tellraw @a "Reloaded!"\n\n'
        load_function.write(load_function_contents)
        load_function.close()
    
    if tick_json_checkbox.get() == 1:
        tick_function_path = os.path.join(namespace_path + '\\functions', 'tick.mcfunction')
        tick_function = open(tick_function_path, 'x')
        tick_function.close()
        
def function_tags():
    os.makedirs(folder_path.get() + '\\' + name.get() + '\\data\\minecraft\\tags\\functions')
    if load_json_checkbox.get() == 1:
        load_path = os.path.join(folder_path.get() + '\\' + name.get() + '\\data\\minecraft\\tags\\functions', 'load.json')
        load = open(load_path, 'w+')
        namespace_load = namespace.get() + ":load"
        load_json = {
            "replace": False,
            "values": [
                namespace_load
            ]
        }
        load_content = json.dumps(load_json, indent = 4)
        load.write(load_content)
        load.close()
    
    if tick_json_checkbox.get() == 1:
        tick_path = os.path.join(folder_path.get() + '\\' + name.get() + '\\data\\minecraft\\tags\\functions', 'tick.json')
        tick = open(tick_path, 'w+')
        namespace_tick = namespace.get() + ":tick"
        tick_json = {
            "replace": False,
            "values": [
                namespace_tick
            ]
        }
        tick_content = json.dumps(tick_json, indent = 4)
        tick.write(tick_content)
        tick.close()
        
def advancement(namespace_path):
    os.makedirs(namespace_path + '\\advancements')

def loot_table(namespace_path):
    os.makedirs(namespace_path + '\\loot_tables')

def recipe(namespace_path):
    os.makedirs(namespace_path + '\\recipes')
    
def tags(namespace_path):
    os.makedirs(namespace_path + '\\tags')

def check_name():
    try:
        os.makedirs(folder_path.get() + '\\' + name.get(), exist_ok=False)
    except FileExistsError:
        name_exists.place(relx = 0.55, rely = 0.20)
        return
    create_datapack()

def check_if_fields_filled():
    if len(folder_path.get()) > 0 and len(name.get()) > 0 and len(namespace.get()) > 0 and len(pack_format.get()) > 0 and len(description.get()) > 0:
        try:
            int_test = int(pack_format.get())
        except ValueError:
            pack_format_value_error.place(relx = 0.63, rely = 0.40)
            return
        check_name()
    else:
        fill_fields.place(relx = 0.1, rely = 0.9)
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

pack_format_value_error = ctk.CTkLabel(frame, text = "needs to be a number!", font = ('consolas', 15, 'bold'), text_color = ('red', 'red'))

pack_format_button = ctk.CTkButton(frame, command = pack_format_link, text = "Check Pack Format(link)", font = ('consolas', 15), text_color = ('black', 'white'))
pack_format_button.place(relx = 0.27, rely = 0.40)

description_text = ctk.CTkLabel(frame, text = "Description", font = ('consolas', 15, 'bold'), text_color = ('black', 'white'))
description_text.place(relx = 0.02, rely = 0.50)
description = ctk.CTkEntry(frame, width = 460, font = ("consolas", 15))
description.place(relx = 0.19, rely = 0.50)

create_datapack_button = ctk.CTkButton(frame, command = check_if_fields_filled, text = "Create Datapack", font = ('consolas', 15), text_color = ('black', 'white'))
create_datapack_button.place(relx = 0.37, rely = 0.8)
fill_fields = ctk.CTkLabel(frame, text = "Fill all fields before attempting again", font = ('consolas', 15, 'bold'), text_color = ('red', 'red'))

checkbox_frame = ctk.CTkScrollableFrame(root, width = 150, height = 135, fg_color = 'gray20', border_width = 3, border_color = 'gray30')
checkbox_frame._scrollbar.configure(height = 0)
checkbox_frame.place(relx = 0.655, rely = 0.57)

load_json_checkbox = ctk.CTkCheckBox(checkbox_frame, text = "load.json", font = ('consolas', 15, 'bold'))
load_json_checkbox.select()
load_json_checkbox.pack(pady = 3, anchor = 'nw')

tick_json_checkbox = ctk.CTkCheckBox(checkbox_frame, text = "tick.json", font = ('consolas', 15, 'bold'))
tick_json_checkbox.select()
tick_json_checkbox.pack(pady = 3, anchor = 'nw')

advancement_checkbox = ctk.CTkCheckBox(checkbox_frame, text = "advancements", font = ('consolas', 15, 'bold'))
advancement_checkbox.pack(pady = 3, anchor = 'nw')

loot_table_checkbox = ctk.CTkCheckBox(checkbox_frame, text = "loot_tables", font = ('consolas', 15, 'bold'))
loot_table_checkbox.pack(pady = 3, anchor = 'nw')

recipe_checkbox = ctk.CTkCheckBox(checkbox_frame, text = "recipes", font = ('consolas', 15, 'bold'))
recipe_checkbox.pack(pady = 3, anchor = 'nw')

tags_checkbox = ctk.CTkCheckBox(checkbox_frame, text = "tags", font = ('consolas', 15, 'bold'))
tags_checkbox.pack(pady = 3, anchor = 'nw')

root.mainloop()
