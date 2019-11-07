from os import remove 
aux=0
file_date = open('nomatch_services.txt', 'w')
for line in open('Datos_tservices.txt', 'r'):
    if line not in open('Datos_fortinet.txt', 'r'):
        file_date.write( line +""+ str(aux) +"\n")
        aux+=1
        print(line + str(aux))

remove('Datos_tservices.txt')
remove('Datos_fortinet.txt')