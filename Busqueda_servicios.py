#codigo 1
#asignacion de variables 
enable_t = 'service'
start_marks = '\"'
end_marks = '\"'
tcp_prot = 'tcp'
udp_prot = 'udp'
p_address = 'dst-port'
search_protocol = 'protocol'
result_protocol = ''
#apetrtura del archivo
f_source = open('origen_firewall.txt', 'r')
r_source = f_source.read() 
f_source.close()
#Separamos el texto en una lista cada salto de linea
text = r_source.split('\n') 
#Busqueda de servicios
file_date = open('Datos_Firewall.txt', 'w')
for line in text:
    if line.find(search_protocol) >= 0 :  # If busqueda de set service, name, protocolos y puertos
        word = line.rfind(enable_t) # encuentra la palabra
        services = line[word:len(enable_t)] # se hace definicion de un inicio y un fin
        #busqueda " "
        search_marks = line.find(start_marks)
        search_marks2 = line.rfind(end_marks) +1 # Encontramos por la derecha la otra comilla
        result_marks = line[search_marks:search_marks2]
        name_services = result_marks.replace(" ", "_")
        services_name = name_services.replace("(","")
        services_name1 = services_name.replace(")","")
        
        # busqueda de protocolo(udp/tcp)
        result = line.find(search_protocol)
        result_protocol = line[result+(len(search_protocol)+1):result+12]
        if result_protocol == tcp_prot : 
            identify_str = services_name1 + "\n" + result_protocol
            file_date.write(identify_str)
            #Busqueda de puertos del protocolo  (udp/tcp)    
            search_address = line.rfind(p_address)
            search_port = line[search_address + 9 :len(line)] 
            file_date.write(" " + search_port + "\n ")

        elif result_protocol == udp_prot:
            print(result_protocol)
            file_date.write(services_name1 + "\n" + result_protocol)
            #Busqueda de puertos del protocolo  (udp/tcp)    
            search_address = line.rfind(p_address)
            search_port = line[search_address + 9 :len(line)] 
            file_date.write(" " + search_port + "\n")
        else:                        
            file_date.write(services_name1 + "\n")
    else: # else de busqueda de  protocolos y puerto
        protocol_TCP = line.find(tcp_prot)
        aditional_tcp = line[protocol_TCP:protocol_TCP+3] # variable recurrencia
        protocol_UDP = line.find(udp_prot)
        aditional_udp = line[protocol_UDP:protocol_UDP+3] # variable recurrencia
        if aditional_tcp == result_protocol:
            aditional_udp = ' '           
            file_date.write(" " + aditional_tcp)
            #Busqueda de puertos del protocolo  (udp/tcp)    
            search_address = line.rfind(p_address)
            search_port = line[search_address + 9 :len(line)] 
            file_date.write(" " + search_port + "\n")
            if aditional_udp == result_protocol:
                file_date.write( " " +  aditional_udp)
                #Busqueda de puertos del protocolo  (udp/tcp)    
                search_address = line.rfind(p_address)
                search_port = line[search_address + 9 :len(line)] 
                file_date.write(" " + search_port + "\n")
            else:
                file_date.write("")
            aditional_tcp = ' '

        elif aditional_udp == result_protocol:
            aditional_tcp = ' '
            file_date.write(" " + aditional_udp)
            
            #Busqueda de puertos del protocolo  (udp/tcp)    
            search_address = line.rfind(p_address)
            search_port = line[search_address + 9 :len(line)] 
            file_date.write(" " + search_port + "\n")

            if aditional_tcp == result_protocol:
                file_date.write(" " + aditional_tcp)
                #Busqueda de puertos del protocolo  (udp/tcp)    
                search_address = line.rfind(p_address)
                search_port = line[search_address + 9 :len(line)] 
                file_date.write(" " + search_port + "\n")
            else:
                file_date.write("")
               
            aditional_udp = ' '

        else:
            #print("No entro a ninguno de los ciclos")
            protocol_TCP = line.find(tcp_prot)
            aditional_tcp = line[protocol_TCP:protocol_TCP+3] # variable recurrencia
            protocol_UDP = line.find(udp_prot)
            aditional_udp = line[protocol_UDP:protocol_UDP+3] # variable recurrencia

            if aditional_tcp == tcp_prot:
                file_date.write( " " + aditional_tcp )
                result_protocol = aditional_tcp
                #Busqueda de puertos del protocolo  (udp/tcp)    
                search_address = line.rfind(p_address)
                search_port = line[search_address + 9 :len(line)] 
                file_date.write(" " + search_port + "\n")

            elif aditional_udp == udp_prot:
                file_date.write(" " + aditional_udp )
                result_protocol = aditional_udp
                    
                #Busqueda de puertos del protocolo  (udp/tcp)    
                search_address = line.rfind(p_address)
                search_port = line[search_address + 9 :len(line)] 
               
                file_date.write(" " + search_port + "\n")
            else:
                result_protocol = ' '              
file_date.close()