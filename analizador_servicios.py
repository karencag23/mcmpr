#codigo 2
from collections import defaultdict
from os import remove 

def get_sections(file):
	""" Divide el texto en grupos por nombre y devuelve una tupla (nombre,contenido)
	"""
	
	splited_text = iter(file.read().split('"')) #se divide el texto usando las "" para identificar el nombre 
	for name in splited_text:
		if name == '': continue #se elimina cualquier cadena vacia que estorbe
		content = next(splited_text) # avanzamos otro elemento dentro de los elementos para conseguir el contenido
		yield name, content

def group(content):
	""" agrupa el contenido de acuerdo al primer campo
	"""
	groups_dict = defaultdict(list) #diccionario que contendra los campos agrupados
	content = iter(content.split())  #iterador a aprtir de la lista de los campos separados
	for field in content:
		groups_dict[field].append(next(content)) 
	return dict(groups_dict) # regresando un diccionario simple

def format_dict(dic):
	""" da formato al diccionario para su posterior impresion
	"""
	out = ""
	for key, value in dic.items():
		out += str(key) 
		for i in value: out += " " + str(i) 
		out += "\n"
	return out	


source_file_path = "Datos_firewall.txt"
new_file_path = "Datos_Servicios.txt"

with open(source_file_path,'r') as source_file,\
open(new_file_path,'w') as new_file:

	for name, content in get_sections(source_file):
		grouped_content = group(content)
		f_content = format_dict(grouped_content)
		f_out = 'edit "{}"\n{}next\n'.format(name,f_content)
		new_file.write(f_out)
		source_file.close()
	
remove("Datos_Firewall.txt")
		
			

