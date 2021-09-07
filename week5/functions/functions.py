def stringCalc(string):
    calc={"upperCase":0, "lowerCase":0}
    for c in string:
        if c.isupper():
           calc["upperCase"]+=1
        elif c.islower():
           calc["lowerCase"]+=1
        else:
           pass
    print ("Printed String:", string)
    print ("Number of Upper case characters: ", calc["upperCase"])
    print ("Number of Lower case characters: ", calc["lowerCase"])

stringCalc('I am KING KONG in my game')