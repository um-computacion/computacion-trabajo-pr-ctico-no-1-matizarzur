def decimal_to_roman(num):
    miles = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    if num<10:
        return unidades[num]
    elif num<100:
        d= decenas[num//10]
        u= unidades[num%10]
        return d + u
    elif num<1000:
        c= centenas[num//100]
        d= decenas[(num%100)//10]
        u= unidades[num%10]
        return c+d+u
    else:
        m= miles[num//1000]
        c= centenas[(num%1000)//100]
        d= decenas[(num%100)//10]
        u= unidades[num%10]
        return m+c+d+u


def main():
    while True:
        num=int(input("Ingrese un numero (menor a 4000): "))
        if num>3999:
            print("Porfavor ingrese un numero valido")
            continue
        romano=decimal_to_roman(num)
        print(f"El numero {num} en romanos es: {romano}")
        op=(input("Desea contuniar? Ingrese 1 para seguir, si desea salir del programa oprima cualquier otra tecla. "))
        if op!="1":
            break
        
        

if __name__== "__main__" :
    main()