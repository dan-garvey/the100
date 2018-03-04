
def getSelection(selectables):
    for x in range(len(selectables)):
        print(str(x+1)+':',selectables[x])
    print("""Select from the above list by typing the corresponding number,
        then hit enter.""")
    selection=int(input())
    if selection<1 or selection>len(utypes):
        print('error, incorrect input')
        return getSelection(selectables)
    return selectables[selection-1]

#utypes=['temperature','volume','mass','acceleration']
print("Unit types available for conversion:")
#choice=getSelection(utypes)
temps=['farenheit','celsius','kelvin']
volumes=['meters cubed', 'feet cubed']
mass=['kilograms','pounds']
accels=['feet per second squared','meters per second squared']
utypes={'temperature':temps, 'volume':volumes, 'weight':mass, 'acceleration':accels}
farenheits={'celsius': '(x-32)/1.8','kelvin':'(x+459.67)*(5/9)'}
celsius={'farenheit': '(x+32)*1.8', 'kelvin': 'x+273.15'}
kelvin={'celsius':'x-273.15', 'farenheit':'x*9/5 -459.67'}
pounds={'kilograms':'x*.45359237'}
kilograms={'pounds': 'x/.45359237'}
