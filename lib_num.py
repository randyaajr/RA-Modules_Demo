def conversion(): 
    input_num = input('Enter the a numeric value: ')
    con_from = input('Which unit of measurement do you wish to converted from:  ')
    con_to = input('Which unit of measurement do you want it converted to: ')

    if con_from == "cm" and con_to == "m":
        ans = float(input_num)/100
        print(ans)
    elif con_from == "m" and con_to == "cm":
        ans = float(input_num)*100
        print(ans)
    elif con_from == "mm" and con_to == "cm":
        ans = float(input_num)/10
        print(ans)
    elif con_from == "cm" and con_to == "mm":
        ans = float(input_num)*10
        print(ans)
    elif con_from == "mm" and con_to == "m":
        ans = float(input_num)/1000
        print(ans)
    elif con_from == "m" and con_to == "mm":
        ans = float(input_num)*1000
        print(ans)
    elif con_from == "ft" and con_to == "cm":
        ans = float(input_num)*30.48
        print(ans)
    elif con_from == "ft" and con_to == "inch":
        ans = float(input_num)*12
        print(ans)
    elif con_from == "inch" and con_to == "cm":
        ans = float(input_num)*2.54
        print(ans)
    elif con_from == "inch" and con_to == "mm":
        ans = float(input_num)*25.4
        print(ans)
    
conversion()
