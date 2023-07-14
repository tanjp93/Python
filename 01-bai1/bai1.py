year= int(input("Nhap so nam : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"La nam nhuan")
else:print(year,"khong la nam nhuan")