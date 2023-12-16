#thabang sambo
#28 march 2019
def decimal_to_gumatj (num):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    while currentnum:
        mod = currentnum % 5
        currentnum = currentnum // 5
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string    

def gumatj_to_decimal (num):
    rev=0
    for i in range(len(str(num))):
        conver = str(num)[::-1]
        result = (5**i) * int(conver[i])
        rev = result + rev
    return rev
        
def gumatj_add (num1, num2):
    if num1>0 and num2>0:
        rev1=0
        for i in range(len(str(num1))):
            conver = str(num1)[::-1]
            result = (5**i) * int(conver[i])
            rev1 = result + rev1    
        rev2=0
        for i in range(len(str(num2))):
            conver = str(num2)[::-1]
            result = (5**i) * int(conver[i])
            rev2 = result + rev2
        add = rev2 + rev1   
        converted_string, modstring = "", ""
        currentnum = add
        while currentnum:
            mod = currentnum % 5
            currentnum = currentnum // 5
            converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
        return converted_string            
    else:
        return 0
    
def gumatj_multiply (num1, num2):
    if num1>0 and num2>0:
        rev1=0
        for i in range(len(str(num1))):
            conver = str(num1)[::-1]
            result = (5**i) * int(conver[i])
            rev1 = result + rev1    
        rev2=0
        for i in range(len(str(num2))):
            conver = str(num2)[::-1]
            result = (5**i) * int(conver[i])
            rev2 = result + rev2
        add = rev2*rev1   
        converted_string, modstring = "", ""
        currentnum = add
        while currentnum:
            mod = currentnum % 5
            currentnum = currentnum // 5
            converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
        return converted_string            
    else:
        return 0    
  