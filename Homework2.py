#تکالیف  من  بخش 2

list = ["1", "2", "3", "4","5"]
for line in list:
    print(line)

print("--" * 30)    

Motherboard = ["Asus","Msi","Gigabyte"]
for m in Motherboard:
    print(Motherboard[0])
    print(Motherboard[-1])


print("--" * 30)        

Motherboard = ["Asus","Msi","Gigabyte"]
print(len(Motherboard))

print("--" * 30)


numbers = ["1","2","3"]
numbers.append("4")
print(numbers)


print("--" * 30)

Motherboard = ["Asus","Msi","Gigabyte"]
del Motherboard [-1]
print(Motherboard)

print("--" * 30)

Numbersu = [1, 2, 3, 4, 5]
print(Numbersu[0] + Numbersu[1])

print("--" * 30)

name = ["Amir", "Hossein","Arian"]
for b in name:
    if "Arman" in name:
        print("Ok")
    else:
        print("Not ok")    

print("--" * 30)

Num= []
Num.append(13)
Num.append(91)
Num.append(21)
print(Num)

print("--" * 30)

Number_list = [10, 200, 600,134]
total = 0
for n in Number_list:
    total += n

print(total)  


print("--" * 30)

numbers = [5, 15, 8, 20, 3]
for n in numbers:
    if n > 10:

     print(n)         


print("--" * 30)    

Gaming_console = ["Playstation", "Xbox", "Nintendo switch"]
handheld_console = ["Steam deck","Asus console"]
for g in Gaming_console:
    if g not in handheld_console:
        handheld_console.append(g)
    
print(handheld_console)
    






      