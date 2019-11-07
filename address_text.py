import re
edit = 'edit'
f_source = open('Datos_address.txt', 'r')
a_source = f_source.read() 
f_source.close()
text_address1 = a_source.split('\n') 
file_pruebas = open('Datos_addr.txt','w')
for line in text_address1:
    if line.rfind(edit) >= 0:
    #busqueda edit
        name_t = re.search(r"((edit) \".*?\")",line)
        if name_t is None:
            hjl=0
        else:
            start = name_t.start()
            end = name_t.end()
            string_text = line[start : end]
            file_pruebas.write( string_text + "\n") 
                     
           