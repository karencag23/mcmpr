import re
enable_t = 'set service'
start_marks = '\"'
end_marks = '\"'
search_address = 'address'
n = ''
string_ip1 = ''
#apetrtura del archivo
f_source = open('origen_address.txt', 'r')
a_source = f_source.read() 
f_source.close()

#Separamos el texto en una lista cada salto de linea
text_address = a_source.split('\n') 
#Creacion de archivo txt
file_date = open('Datos_address.txt', 'w')
#busqueda y escritura en archivo de texto 
file_date.write("config firewall address"+ "\n") 
for line in text_address:
    if line.rfind(search_address) >= 0:
        word_service = line.rfind(enable_t) 
        services = line[word_service:len(enable_t)] 
       

        #busqueda de comillas
        name = re.search(r"(\" \".*?\")",line)
        name_addr= name.group(0).replace('" ','')
        name_addr= name_addr.replace('" ','')
        name_addr =name_addr.replace(" ", "_")
        names = name_addr.replace('<','')
        names1 = names.replace('>','')
        names2 = names1.replace('(','')
        names3 = names2.replace(')','')
        file_date.write("edit " + names3 + "\n" )  
        
        #busqueda de ip
        ip = re.search(r"(\" \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})",line) 
        search_url = re.search(r"([\w.%+-]+[\w.-]+\.[a-zA-Z]{2,6})",line)
        if ip is None:
            start_url = search_url.start()
            end_url = search_url.end()
            url_find = line[start_url:end_url]
          
            file_date.write("set type fqdn"  + "\n" ) 
            file_date.write("set fqdn" + ' ' + url_find + "\n" ) 
            #file_date.write("\tset comment" + ' ' + result_remark + "\n" )  
        else:
            start_ip = ip.start()
            end_ip = ip.end()
            string_ip = line[start_ip:end_ip]
            string_ip1 = string_ip.replace('" ','')
            n = string_ip1
            n = len(string_ip1)

            #file_date.write("IP:" + string_ip + "\n")  

        #busqueda de mascara de red 
        #mask = re.search(r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})",line) 
        mask = re.search(r"(\" \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})",line) 
      
        if mask is None:
            jr=0
        else:
            start_mask = mask.start()
            end_mask = mask.end()
            string_mask = line[start_mask +2 +n :end_mask]
            print(string_mask)
            #print(string_mask)
            file_date.write("set subnet" +' ' + string_ip1 + string_mask + "\n" )

    #busqueda de cometarios        
    remark = re.search(r"([0-9] \".*?\")",line)
    if remark is None:
       jr=0
    else:
        start_coment = remark.start()
        end_coment = remark.end()
        string_remark = line[start_coment:end_coment]
        result_remark = string_remark.replace('5','')
        file_date.write("set comment" + ' ' + result_remark + "\n" ) 
    file_date.write("next"  + "\n" ) 
file_date.write("end"+ "\n")