
"""
Created on Wed Apr  4 18:48:37 2018
@author: JuanCarlos
"""

import xlwt
import pandas as pd 
import requests

# from pandas import DataFrame

import os
path = '../../_data_tmp/W3SVC2/'
fgeo = False

def old(): 
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    #if __name__ == '__main__':
    #    print("Cleaning program! ")
    #
    #    #Read names.txt
    #    data_real = [] 
    #    list1 = []
    #    f = open("./u_ex091024.log","r", newline='\r\n') 
    #    newopen = open('newfile.txt', 'w')
    #    bad_words = ['#Software','#Version','#Date' ]
    #    for line in f: 
    #        data_real.append(line)
    #    
    #    cadena = " ".join(data_real)
    #    for line in cadena: 
    #        # print(line.split())
    #        cline = cleanLine(line)
    #        data.append(cline.upper().split())
    #     fclose()
    #         
    #        
    #if not any(bad_word in cadena for bad_word in bad_words)
    pass

def create_excel( file ):
    print(str(file))
    bad_words = ['#Software','#Version','#Date','#Fields']
    data_real = []
    data = []
    with open( path + file) as oldfile, open(path + 'newfile.txt', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)

    f = open(path + "/newfile.txt","r") 
    for line in f: 
            data_real.append(line)
            cadena = " ".join(data_real)
            cadena1 = cadena.split()
    if cadena1[0] == cadena1[14]:
        print("14 columns")
        n=1
    else:
        print("18 columns")
        n=0
            #data.append(cadena1)
    #Writing to excel

    #import xlwt
    #from tempfile import TemporaryFile
    #book = xlwt.Workbook()
    #sheet1 = book.add_sheet('sheet1')
    #
    ##supersecretdata = [34,123,4,1234,12,34,12,41,234,123,4,123,1,45123,5,43,61,3,56]
    #
    #for e,i in enumerate(cadena1):
    #    sheet1.write(e,0,i)
    #
    #name = "random.xls"
    #book.save(name)
    #book.save(TemporaryFile())

    #probar otra cosa mediante pandas
        
    if n == 1:
    ######column Date###########
        a = range(len(cadena1))
        b = a[0:len(cadena1):14]
        count = 0
        date = []
        while (count < len(b)):
            date.append(cadena1[b[count]])
            count = count + 1
    ######column Time###########
        b = a[1:len(cadena1):14]
        count = 0
        time = []
        while (count < len(b)):
            time.append(cadena1[b[count]])
            count = count + 1  
    ######column S-ip##########
        b = a[2:len(cadena1):14]
        count = 0
        s_ip = []
        while (count < len(b)):
            s_ip.append(cadena1[b[count]])
            count = count + 1
    ######colum cs_method#######
        b = a[3:len(cadena1):14]
        count = 0
        cs_method = []
        while (count < len(b)):
            cs_method.append(cadena1[b[count]])
            count = count + 1
    ####cs_uri_stem##########
        b = a[4:len(cadena1):14]
        count = 0
        cs_uri_stem = []
        while (count < len(b)):
            cs_uri_stem.append(cadena1[b[count]])
            count = count + 1
    ######cs_uri_query########
        b = a[5:len(cadena1):14]
        count = 0
        cs_uri_query = []
        while (count < len(b)):
            cs_uri_query.append(cadena1[b[count]])
            count = count + 1   
    ######s_port###########
        b = a[6:len(cadena1):14]
        count = 0
        s_port = []
        while (count < len(b)):
            s_port.append(cadena1[b[count]])
            count = count + 1   
    #####cs_username######
        b = a[7:len(cadena1):14]
        count = 0
        cs_username = []
        while (count < len(b)):
            cs_username.append(cadena1[b[count]])
            count = count + 1   
    #######c_ip##### 
        b = a[8:len(cadena1):14]
        count = 0
        c_ip = []
        while (count < len(b)):
            c_ip.append(cadena1[b[count]])
            count = count + 1    
    #####cs_User_Agent#######
        b = a[9:len(cadena1):14]
        count = 0
        cs_User_Agent = []
        while (count < len(b)):
            cs_User_Agent.append(cadena1[b[count]])
            count = count + 1  
    #####sc_status########
        b = a[10:len(cadena1):14]
        count = 0
        sc_status = []
        while (count < len(b)):
            sc_status.append(cadena1[b[count]])
            count = count + 1
    ######sc_substatus#######
        b = a[11:len(cadena1):14]
        count = 0
        sc_substatus = []
        while (count < len(b)):
            sc_substatus.append(cadena1[b[count]])
            count = count + 1

    #####sc_win32########
        b = a[12:len(cadena1):14]
        count = 0
        sc_win32 = []
        while (count < len(b)):
            sc_win32.append(cadena1[b[count]])
            count = count + 1 
    #####time_taken######
        b = a[13:len(cadena1):14]
        count = 0
        time_taken = []
        while (count < len(b)):
            time_taken.append(cadena1[b[count]])
            count = count + 1    
        

    #date = [cadena1[0],cadena1[14],cadena1[28],cadena1[42],cadena1[56],cadena1[70],cadena1[84],cadena1[98],cadena1[112],cadena1[126],cadena1[140]]
    #time = [cadena1[1],cadena1[15],cadena1[29],cadena1[43],cadena1[57],cadena1[71],cadena1[85],cadena1[99],cadena1[113],cadena1[127],cadena1[141]]
    #s_ip = [cadena1[2],cadena1[16],cadena1[30],cadena1[44],cadena1[58],cadena1[72],cadena1[86],cadena1[100],cadena1[114],cadena1[128],cadena1[142]]
    #cs_method = [cadena1[3],cadena1[17],cadena1[31],cadena1[45],cadena1[59],cadena1[73],cadena1[87],cadena1[101],cadena1[115],cadena1[129],cadena1[143]]
    #cs_uri_stem = [cadena1[4],cadena1[18],cadena1[32],cadena1[46],cadena1[60],cadena1[74],cadena1[88],cadena1[102],cadena1[116],cadena1[130],cadena1[144]]
    #cs_uri_query =[cadena1[5],cadena1[19],cadena1[33],cadena1[47],cadena1[61],cadena1[75],cadena1[89],cadena1[103],cadena1[117],cadena1[131],cadena1[145]]
    #s_port = [cadena1[6],cadena1[20],cadena1[34],cadena1[48],cadena1[62],cadena1[76],cadena1[90],cadena1[104],cadena1[118],cadena1[132],cadena1[146]]
    #cs_username = [cadena1[7],cadena1[21],cadena1[35],cadena1[49],cadena1[63],cadena1[77],cadena1[91],cadena1[105],cadena1[119],cadena1[133],cadena1[147]]
    #c_ip = [cadena1[8],cadena1[22],cadena1[36],cadena1[50],cadena1[64],cadena1[78],cadena1[92],cadena1[106],cadena1[120],cadena1[134],cadena1[148]]
    #cs_User_Agent = [cadena1[9],cadena1[23],cadena1[37],cadena1[51],cadena1[65],cadena1[79],cadena1[93],cadena1[107],cadena1[121],cadena1[135],cadena1[149]]
    #sc_status = [cadena1[10],cadena1[24],cadena1[38],cadena1[52],cadena1[66],cadena1[80],cadena1[94],cadena1[108],cadena1[122],cadena1[136],cadena1[150]]
    #sc_substatus = [cadena1[11],cadena1[25],cadena1[39],cadena1[53],cadena1[67],cadena1[81],cadena1[95],cadena1[109],cadena1[123],cadena1[137],cadena1[151]]
    #sc_win32 = [cadena1[12],cadena1[26],cadena1[40],cadena1[54],cadena1[68],cadena1[82],cadena1[96],cadena1[110],cadena1[124],cadena1[138],cadena1[152]]
    #time_taken = [cadena1[13],cadena1[27],cadena1[41],cadena1[55],cadena1[69],cadena1[83],cadena1[97],cadena1[111],cadena1[125],cadena1[139],cadena1[153]]

    #####DATA COLUMN####
    #a = list(range(len(cadena1))
    #b = a[0:len(cadena1):14]
    #date = [cadena1[b]]
       # geolocalizacion
        pc = []; city = []; area = []; country = []
        if fgeo: 
            geo = []
            for i in c_ip:
                ip = i
                url = 'http://freegeoip.net/json/'+ip
                r = requests.get(url)
                js = r.json()   
                
                city.append(js["city"])
                pc.append(js["zip_code"])
                area.append(js["region_name"])
                country.append(js["country_name"])
                
                geo.append(js)
        else: 
            pc = date; city = date; area = date; country = date

        df = pd.DataFrame({'Date': date, 'Time': time, 's_ip': s_ip,'cs_method':cs_method,'cs_uri_stem': cs_uri_stem, 'cs_uri_query': cs_uri_query,'s_port': s_port,'cs_username': cs_username,'c_ip': c_ip,'cs_User_Agent': cs_User_Agent, 'cs_Cookie': '-' , 'cs_Referer': '-', 'sc_status': sc_status,'sc_substatus': sc_substatus,'sc_win32': sc_win32, 'sc_bytes': '-','cs_bytes': '-' ,'time_taken': time_taken ,
                        'pc': pc, 'city' : city, 'state_area' : area, 'country': country
            })
        ##df = DataFrame({'Date': date, 'Time': time, 's_ip': s_ip, 'cs_method': cs_method,'cs_uri_stem': cs_uri_stem, 'cs_uri_query': cs_uri_query, 's_port': s_port ,'cs_username': cs_username, 'c_ip': c_ip,'cs_User_Agent': cs_User_Agent,'sc_status': sc_status, 'sc_substatus': sc_substatus, 'sc_win32': sc_win32, 'time_taken': time_taken})         

        robots = df[ df["cs_uri_stem"] == '/robots.txt' ]
        arob = []
        for robot in robots.values:
            arob.append(robot[2] )

        def check(x): 
            if x in arob: return "X"
            return ""

        df['crowler'] = df['c_ip'].map(lambda x: check( x ))

        if os.path.isfile(path + 'test2.xlsx'):
            dfs = pd.read_excel(path + 'test2.xlsx', sheet_name='sheet1', index=False)      
            frames = [df, dfs]
            result1 = pd.concat(frames)
        else:
            result1 = df

        result1.to_excel( path + 'test2.xlsx', sheet_name='sheet1', index=False)
        
    else:
        a = range(len(cadena1))
        b = a[0:len(cadena1):18]
        count = 0
        date = []
        while (count < len(b)):
            date.append(cadena1[b[count]])
            count = count + 1
    ######column Time###########
        b = a[1:len(cadena1):18]
        count = 0
        time = []
        while (count < len(b)):
            time.append(cadena1[b[count]])
            count = count + 1  
    ######column S-ip##########
        b = a[2:len(cadena1):18]
        count = 0
        s_ip = []
        while (count < len(b)):
            s_ip.append(cadena1[b[count]])
            count = count + 1
    ######colum cs_method#######
        b = a[3:len(cadena1):18]
        count = 0
        cs_method = []
        while (count < len(b)):
            cs_method.append(cadena1[b[count]])
            count = count + 1
    ####cs_uri_stem##########
        b = a[4:len(cadena1):18]
        count = 0
        cs_uri_stem = []
        while (count < len(b)):
            cs_uri_stem.append(cadena1[b[count]])
            count = count + 1
    ######cs_uri_query########
        b = a[5:len(cadena1):18]
        count = 0
        cs_uri_query = []
        while (count < len(b)):
            cs_uri_query.append(cadena1[b[count]])
            count = count + 1   
    ######s_port###########
        b = a[6:len(cadena1):18]
        count = 0
        s_port = []
        while (count < len(b)):
            s_port.append(cadena1[b[count]])
            count = count + 1   
    #####cs_username######
        b = a[7:len(cadena1):18]
        count = 0
        cs_username = []
        while (count < len(b)):
            cs_username.append(cadena1[b[count]])
            count = count + 1   
    #######c_ip##### 
        b = a[8:len(cadena1):18]
        count = 0
        c_ip = []
        while (count < len(b)):
            c_ip.append(cadena1[b[count]])
            count = count + 1    
    #####cs_User_Agent#######
        b = a[9:len(cadena1):18]
        count = 0
        cs_User_Agent = []
        while (count < len(b)):
            cs_User_Agent.append(cadena1[b[count]])
            count = count + 1 
        
    ##cs_cookie######
        b = a[10:len(cadena1):18]
        count = 0
        cs_cookie = []
        while (count < len(b)):
            cs_cookie.append(cadena1[b[count]])
            count = count + 1    
    ###cs_referer#######
        b = a[11:len(cadena1):18]
        count = 0
        cs_referer = []
        while (count < len(b)):
            cs_referer.append(cadena1[b[count]])
            count = count + 1    
        
    #####sc_status########
        b = a[12:len(cadena1):18]
        count = 0
        sc_status = []
        while (count < len(b)):
            sc_status.append(cadena1[b[count]])
            count = count + 1
    ######sc_substatus#######
        b = a[13:len(cadena1):18]
        count = 0
        sc_substatus = []
        while (count < len(b)):
            sc_substatus.append(cadena1[b[count]])
            count = count + 1

    #####sc_win32########
        b = a[14:len(cadena1):18]
        count = 0
        sc_win32 = []
        while (count < len(b)):
            sc_win32.append(cadena1[b[count]])
            count = count + 1 
    #####sc_bytes########
        b = a[15:len(cadena1):18]
        count = 0
        sc_bytes = []
        while (count < len(b)):
            sc_bytes.append(cadena1[b[count]])
            count = count + 1
    ####cs_bytes########
        b = a[16:len(cadena1):18]
        count = 0
        cs_bytes = []
        while (count < len(b)):
            cs_bytes.append(cadena1[b[count]])
            count = count + 1  
        
    #####time_taken######
        b = a[17:len(cadena1):18]
        count = 0
        time_taken = []
        while (count < len(b)):
            time_taken.append(cadena1[b[count]])
            count = count + 1

        # geolocalizacion
        pc = []; city = []; area = []; country = []
        if fgeo: 
            geo = []
            for i in c_ip:
                ip = i
                url = 'http://freegeoip.net/json/'+ip
                r = requests.get(url)
                js = r.json()   
                
                city.append(js["city"])
                pc.append(js["zip_code"])
                area.append(js["region_name"])
                country.append(js["country_name"])
                
                geo.append(js)
        else: 
            pc = date; city = date; area = date; country = date

        # read current excel in pandas. 
        df = pd.DataFrame({'Date': date, 'Time': time, 's_ip': s_ip,'cs_method':cs_method,'cs_uri_stem': cs_uri_stem, 'cs_uri_query': cs_uri_query,'s_port': s_port,'cs_username': cs_username,'c_ip': c_ip,'cs_User_Agent': cs_User_Agent, 'cs_cookie': cs_cookie , 'cs_referer': cs_referer, 'sc_status': sc_status,'sc_substatus': sc_substatus,'sc_win32': sc_win32, 'sc_bytes': sc_bytes,'cs_bytes': cs_bytes ,'time_taken': time_taken,
                            'pc': pc, 'city' : city, 'state_area' : area, 'country': country
         })
        ##df = DataFrame({'Date': date, 'Time': time, 's_ip': s_ip, 'cs_method': cs_method,'cs_uri_stem': cs_uri_stem, 'cs_uri_query': cs_uri_query, 's_port': s_port ,'cs_username': cs_username, 'c_ip': c_ip,'cs_User_Agent': cs_User_Agent,'sc_status': sc_status, 'sc_substatus': sc_substatus, 'sc_win32': sc_win32, 'time_taken': time_taken})     
        robots = df[ df["cs_uri_stem"] == '/robots.txt' ]
        arob = []
        for robot in robots.values:
            arob.append(robot[2] )

        def check(x): 
            if x in arob: return "X"
            return ""

        df['crowler'] = df['c_ip'].map(lambda x: check( x ))

        if os.path.isfile(path + 'test3.xlsx'):
            dfs = pd.read_excel(path + 'test3.xlsx', sheet_name='sheet1', index=False)      
            frames = [df, dfs]
            result2 = pd.concat(frames)
        else:
            result2 = df

        result2 = pd.concat(frames)



        
        result2.to_excel(path + 'test3.xlsx', sheet_name='sheet1', index=False)
        
        #date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Cookie) cs(Referer) sc-status sc-substatus sc-win32-status sc-bytes cs-bytes time-taken
        #date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) sc-status sc-substatus sc-win32-status time-taken  

def geolocalizacion():
	print("geo")
    geo = []
    pc = []; city = []; area = []; country = []
    c_ip = []
    for i in c_ip:
        ip = i
        url = 'http://freegeoip.net/json/'+ip
        r = requests.get(url)
        js = r.json()   
        
        city.append(js["city"])
        pc.append(js["zip_code"])
        area.append(js["region_name"])
        country.append(js["country_name"])
        
        geo.append(js)

def read_files(): 
    files = os.listdir(path)
    for i in range(len(files)): 
        print(files[i])
        if files[i].startswith("u_ex"): 
            create_excel(files[i])
    print("end")
		
# main    
if __name__ == '__main__':
    read_files()
		