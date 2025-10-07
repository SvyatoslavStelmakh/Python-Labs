IP_adress = input("Введите IP адрес: ")

if len(IP_adress)!=15:
    print("IP адрес введён неверно!")
elif int(IP_adress[0:3]) < 0 or int(IP_adress[0:3]) > 255:
    print("IP адрес введён неверно!")
elif IP_adress[3]!=".":
    print("IP адрес введён неверно!")
elif int(IP_adress[4:7]) < 0 or int(IP_adress[4:7]) > 255:
    print("IP адрес введён неверно!")
elif IP_adress[7]!=".":
    print("IP адрес введён неверно!")
elif int(IP_adress[8:11]) < 0 or int(IP_adress[8:11]) > 255:
    print("IP адрес введён неверно!")
elif IP_adress[11]!=".":
    print("IP адрес введён неверно!")
elif int(IP_adress[12:]) < 0 or int(IP_adress[12:]) > 255:
    print("IP адрес введён неверно!")
else:
    print("IP адрес введён верно!")
    
       
