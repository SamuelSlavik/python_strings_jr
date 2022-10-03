# string = input("Stdin: ")
string = "lorem ipsum"

def print_position_and_chars():
    index = string.index(" ") #Metoda nad string, vrati index hladaneho charakteru

    # Printovanie do dvoch riadkov s vysvetlenim
    print(index)
    print(string[(index+1):(index+4)]) #str[x:y] vypise substring od x po y, myslim ze x vratane, y uz nie

    # Printovanie do jedneho riadku ako mas v zadani
    print(f"{index} {string[(index+1):(index+4)]}")


print_position_and_chars()
