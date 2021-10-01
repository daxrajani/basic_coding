def applyByteStuffing(flag, esc, a):
    x = a.replace (esc, esc*2)
    y = x.replace (flag, esc+flag)
    return flag + y + flag

def applydeByteStuffing(flag, esc, d):
    x = d.replace (esc*2, esc)
    y = x.replace (esc+flag, flag)
    z = y.replace (flag*2, flag)
    z = z[:-1]
    return z
 
print("19012011002 Manthan Bhavsar")
a=input("Input for byte stuffing : ")
flag=input("Enter flag byte : ")
esc=input("enter escape byte : ")

d=applyByteStuffing(flag,esc,a)
print("After Byte Stuffing: ",d)

e=applydeByteStuffing(flag,esc,d)
print("After Byte De-Stuffing: ",e)
