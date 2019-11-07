import re
cont = 0
f_source = open('Datos_address.txt', 'r')
a_source = f_source.read() 
f_source.close()
text_address = a_source.split('\n') 

for line in text_address:
    texto = "edit"
    found = re.findall(texto,line) 
    if found:
        cont+=1
        print(texto +" "+ str(cont)) 

