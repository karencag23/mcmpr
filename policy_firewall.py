import re

search_edit = 'edit'

f_source = open('prueba_fort.txt', 'r')
a_source = f_source.read() 
f_source.close()
text_address = a_source.split('\n') 
file_date = open('Datos_fortinet.txt', 'w')
for line in text_address:
    if line.rfind(search_edit) >= 0:
    #busqueda edit
        name = re.search(r"((edit) \".*?\")",line)
        if name is None:
            h=0
        else:
            start_addr = name.start()
            end_addr = name.end()
            string_addr = line[start_addr : end_addr]
            file_date.write( string_addr + "\n" )