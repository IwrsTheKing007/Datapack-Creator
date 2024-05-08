import os

path = input('Copy and Paste the path here: ')
name = input('Input the name of the datapack: ')

def create_datapack(path, name):
    try:
        os.makedirs(path + '\\' + name, exist_ok=False)
    except FileExistsError:
        name = input('folder already exists, try something else, or delete the already existing folder\nInput the name of the datapack: ')
        create_datapack(path, name)
    
    pack_format = input('Input your desired pack_format: ')
    description = input('Input your description: ')
    
    mcmeta_path = os.path.join(path+'\\'+name, 'pack.mcmeta')
    pack_mcmeta = open(mcmeta_path, 'w+')
    mcmeta_content = '{\n    "pack": {\n        "pack_format": ' + pack_format + ',\n        "description": "' + description + '"\n    }\n}'
    pack_mcmeta.write(mcmeta_content)
    pack_mcmeta.close()
    
    namespace = input('Input your desired namespace: ')
    
    os.makedirs(path + '\\' + name + '\\data\\minecraft\\tags\\functions')
    
    load_path = os.path.join(path + '\\' + name + '\\data\\minecraft\\tags\\functions', 'load.json')
    load = open(load_path, 'w+')
    load_contents = '{\n    "replace": false,\n    "values": [\n        "' + namespace + ':load"\n    ]\n}'
    load.write(load_contents)
    load.close()
    
    tick_path = os.path.join(path + '\\' + name + '\\data\\minecraft\\tags\\functions', 'tick.json')
    tick = open(tick_path, 'w+')
    tick_contents = '{\n    "replace": false,\n    "values": [\n        "' + namespace + ':tick"\n    ]\n}'
    tick.write(tick_contents)
    tick.close()
    
    os.makedirs(path + '\\' + name + '\\data\\' + namespace + '\\functions')
    
    loadfunc_path = os.path.join(path + '\\' + name + '\\data\\' + namespace + '\\functions', 'load.mcfunction')
    loadfunc = open(loadfunc_path, 'x')
    loadfunc_contents = 'tellraw @a "Reloaded!"\n\n'
    loadfunc.write(loadfunc_contents)
    loadfunc.close()
    tickfunc_path = os.path.join(path + '\\' + name + '\\data\\' + namespace + '\\functions', 'tick.mcfunction')
    tickfunc = open(tickfunc_path, 'x')
    tickfunc.close()

create_datapack(path, name)
