"""
i = 0
while i != 1:
    print ('1')
    
try:
    lijst = ["hoi", "doei"]
    print (lijst[2])

    except IndexError:
        print ("Te weining items of tevel items")
"""

def main():
    try:
        items = invoer()
        print ("Dit zijn de items", items)
    except IndexError:
        print ("Te weinig items of te veel")

def invoer():
    lijstje = input("Voer 5 items in: ")

    if len(lijstje.split(",")) != 5:
        raise IndexError

    return lijstje

main()
