
import random,pyperclip
Mode = str(input('Chose Mode Please (Password Generator, Password Checker): '))
tab = ['a','b','c','d','e',"f","g","h","i","j","k","l","m","n","o",'p','[','#','%','$','1','2','A','B','C','D','E']

def mixTable(ok):
    newTab = []
    for i in range(len(ok)+1):
        newTab.append(ok[random.randint(0,len(ok)-1)])
    return newTab


def gen():
    mixed = mixTable(tab)
    for i in mixed:
        print(i)
    if Mode == "g":
        new = ''
        for i in range(0, int(random.randint(9,16))):
            new += str(mixed[random.randint(1,len(mixed)-1)])
        pyperclip.copy(new)
        paste = pyperclip.paste()
        return new

print(gen(),"Copied to ClipBoard")

