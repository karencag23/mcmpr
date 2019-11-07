import re
search_poli = 'policy'
new_source = ''
new_services = ''
string_service1 =''
S1 = ''
string_ip_group =''
src_res = ''
dest_group =''
destination_group = ''
string_nat = ''
new_p = ''
#apertura del archivo
f_source = open('origen_policies.txt', 'r')
p_source = f_source.read() 
f_source.close()
#Separamos el texto 
text_policy = p_source.split('\n')
#Se crea un nuevo archivo de texto
file_policy = open('Datos_policy.txt','w')
#busqueda en el archivo txt
file_policy.write("config firewall policy"+"\n")
for line in text_policy:
    if line == "exit":
        s=0 
        print (destination_group + dest_group)
        file_policy.write("set srcaddr  " + string_ip_group  + src_res +"\n" )
        file_policy.write("set dstaddr "+ destination_group +' '+ dest_group  + "\n" +"set action  "+  new_p + "\n" )
        file_policy.write("set service  "+ new_services+' '+ S1+  "\n" + "set "+ string_nat + "\n"+ "next"+"\n")   
    if line.rfind(' id ') >= 0:
        #busqueda de numero de politicas 
        search_id= re.search(r"(\b(id) [0-9]{1,3} \b(from|name))",line)
        if search_id is None:
              hj=0
        else:
            start_id  = search_id.start()
            end_id = search_id.end()
            string_id = line[start_id + 3 : end_id - 5] 
            print(string_id)
            S1= ''
            src_res = ''
            dest_group = ''
            old_id=string_id
            file_policy.write("edit " + string_id   + "\n" )
        #busqueda de interfaz de origen
        search_source = re.search(r"(\b(from) \".*?\")",line)
        if search_source is None:
              hj=0
        else:
            start_source  = search_source.start()
            end_source = search_source.end()
            string_source = line[start_source + 5 : end_source]
            old_source = string_source.replace("Trust", "port2")
            new_source =old_source.replace("Untrust","port3")
            file_policy.write("set srcintf "+  new_source  + "\n" ) 
            
            new_source = string_source
        #busqueda de interfaz de destino
        search_destination = re.search(r"(\b(to) \".*?\")",line)
        if search_destination is None:
              hj=0
        else:
            start_destination  = search_destination.start()
            end_destination = search_destination.end()
            string_destination = line[start_destination + 3 : end_destination]
            old_destination = string_destination.replace("Trust", "port2")
            new_destination =old_destination.replace("Untrust","port3")
            file_policy.write("set  dstintf  "+  new_destination  + "\n" )
        #busqueda de ip o grupo origen(srcaddr)
        source_ip_group = re.search(r"(\"  \".*?\" )",line)
        if source_ip_group is None:
              hj=0
        else:
            start_ip_group = source_ip_group.start()
            end_ip_group = source_ip_group.end()
            string_ip_group = line[start_ip_group + 3: end_ip_group]
            string_ip_group = string_ip_group.replace("' '","'_'")
            #print(string_ip_group)
              
        #busqueda de ip o grupo destino(dstaddr)
        destination_ip_group = re.search(r"(\b\" \".*?\")",line)
        if destination_ip_group is None:
              hj=0
        else:
            start_destination_group = destination_ip_group.start()
            end_destination_group = destination_ip_group.end()
            destination_group = line[start_destination_group + 2: end_destination_group] 
            destination_group = destination_group.replace("' '","'_'")
            destination_group = destination_group.replace('<','')
            destination_group = destination_group.replace('>','')
            destination_group = destination_group.replace('(','')
            destination_group = destination_group.replace(')','')

            n=destination_group
            n= len(destination_group)
            
        # permit
        permit = re.search(r"( (permit))",line)
        if permit is None:
              hj=0
        else:
            start_p = permit.start()
            end_p = permit.end()
            string_p = line[start_p:end_p]
            new_p = string_p.replace("permit","accept")
            
        #busqueda servicios(services)
        services = re.search(r"(\b\" \".*?\" \".*?\")",line) 
        if services is None:
              hj=0
        else:
            start_services =services.start()
            end_services = services.end()
            destination_services= line[start_services + n + 3 : end_services]
            new_services = destination_services.replace("ANY", "ALL")
            new_services = new_services.replace("' '","'_'")

            
        #nat
        d_nat = re.search(r"(\b(nat src) | (nat src dip-id [0-9]{0,9}))",line)
        if d_nat is None:
              hj=0
        else:
            start_nat = d_nat.start()
            end_nat = d_nat.end()
            string_nat = line[start_nat : end_nat]
               
    else:
        #busqueda de ip o grupo origen(srcaddr)
        src = re.search(r"(set src-address \".*?\")",line)
        if src is None:
              hj=0
        else:
            start_src = src.start()
            end_src = src.end()
            string_src = line[start_src + 16 : end_src]
            src_res = src_res + " " + string_src
            src_res = src_res.replace("' '","'_'")
            #print(src)
            
        #busqueda de ip o grupo destino(dstaddr) 
        dsr = re.search(r"(set dst-address \".*?\")",line)
        if dsr is None:
              hj=0
        else:
            start_dsr = dsr.start()
            end_dsr = dsr.end()
            string_dsr = line[start_dsr + 16 : end_dsr]
            dest_group = dest_group + " " + string_dsr
            dest_group = dest_group.replace("' '","'_'")
        #busqueda de servicios
        service1 = re.search(r"(set service \".*?\")",line)
        if service1 is None:
              hj=0
        else:
            start_service1 = service1.start()
            end_service1 = service1.end()
            string_service1 = line[start_service1 + 12 : end_service1]
            S1= S1 + " " + string_service1
            S1= S1.replace("' '","'_'")
file_policy.write("end"+"\n")

        
        
            
        
       
        
           
        
        
       
       
        
       
       


    
        

        
       


















file_policy.close()  