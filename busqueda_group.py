import re 
from os import remove 
start_marks = '\"'
end_marks = '\"'
search_group = 'group'
search_add = ' add '
match_group = ''
string_usr = ''
name_group = ''
name_group_old =''
i = 0
j = 0
k = 0

#Apertura de archivo de texto 
get_group = open('origen_group.txt', 'r')
read_group = get_group.read()
get_group.close()
#Separamos el texto 
text_group = read_group.split('\n')
#Se crea un nuevo archivo de texto
file_group = open('Datos_groups.txt','w')

#Busqueda y escritura de archivo de texto
file_group.write("config firewall addrgrp" + "\n")
for line in text_group:
    #busqueda de comillas 
    if (j==1 and match_group != ''):
        i+=1
        file_group.write("edit" + ' ' + name_group_old + "\n" + "set member " + match_group + "\n" + "next" + "\n")
        match_group = ''
        name_group_old = name_group  
        
    if line.rfind(' add ') >= 0:
        #buscar add 
        
        search_add = re.search(r"([a-d]{1,3} \".*?\")",line)
        if search_add is None:
            jr=0
        else:
            j=0
            start_usr = search_add.start()
            end_usr = search_add.end()
            string_usr =line[start_usr + 4: end_usr] 
            string_usr = string_usr.replace(' ','_')
            string_usr = string_usr.replace("(","") 
            string_usr =string_usr.replace(")","")
            match_group = match_group +" "+ string_usr
           
                 
    else:
        name = re.search(r"(\" \".*?\")",line)
        if name is None:
              jr=0
        else:   
            start_name = name.start()
            end_name = name.end()
            string_name = line[start_name : end_name]  
            name_group = string_name.replace('" ','')
            name_group = name_group.replace(" ","_")  
            name_group = name_group.replace("(","") 
            name_group = name_group.replace(")","")
            
            if k==0:
                name_group_old = name_group
            j=1
            k=1
file_group.write("end" + "\n")
file_group.close()       