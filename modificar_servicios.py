#codigo 3
from os import remove 
start_marks = '\"'
end_marks = '\"'
tcp_prot = 'tcp'
udp_prot = 'udp'
#se realiza apertura de archivo
get_service = open('Datos_Servicios.txt', 'r')
read_service = get_service.read()
get_service.close()
#Separamos el texto en una lista cada salto de linea
text_service = read_service.split("\n")
print(text_service)
file_date = open('Destino_Servicios.txt', 'w')
indice = 1
for line in text_service:
    #busqueda " "
    search_marks = line.find(start_marks)
    search_marks2 = line.rfind(end_marks)+1 # Encontramos por la derecha la otra comilla
    result_marks = line[search_marks:search_marks2]
    name_services = result_marks.replace(" ", "_")
    services_name = name_services.replace("(","")
    services_name1 = services_name.replace(")","")
    
    
    if search_marks >= 0 : # If busqueda de " " , tcp/udp, port
        file_date.write(line + "\n")
        search_marks = -1
    else:
        search_prot = line.rfind("p") # Encontramos por la derecha la letra "p"
        protocol = line[search_prot-2:search_prot+1] #
        if protocol == tcp_prot:
            search_ports = line[search_prot+1:len(line)]
            file_date.write("set " + protocol + "-portrange " + search_ports + "\n" )
           
        elif protocol == udp_prot:
         
            search_ports = line[search_prot+1:len(line)]
        
            file_date.write("set " + protocol + "-portrange " + search_ports + "\n")
        else:
            
            file_date.write(line + "\n")
remove("Datos_servicios.txt")

        





      