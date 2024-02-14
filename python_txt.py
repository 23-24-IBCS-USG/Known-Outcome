def getinfo():
    f = open("pg24117.txt")

    s = f.read()
    
    print(s)

    l = s.split("***")
    
    s = l[2]
#s in the list at position 2
    s = s.split()
  
    print(s)

    chars = {"a":0,
             "b":0,
             "c":0,
             "d":0,
             "e":0,
             "f":0,
             "g":0,
             "h":0,
             "i":0,
             "j":0,
             "k":0,
             "l":0,
             "m":0,
             "n":0,
             "o":0,
             "p":0,
             "q":0,
             "r":0,
             "s":0,
             "t":0,
             "u":0,
             "v":0,
             "w":0,
             "x":0,
             "y":0,
             "z":0}

    listOfChars = chars.keys()

    for word in s:
        word = word.replace(",", "")
        word = word.replace("!", "")
        word = word.replace("?", "")
        word = word.replace("-", "")
        word = word.replace("_", "")
        word = word.replace(".", "")
        
  
        for c in word:
                c = c.lower()
                if c in listOfChars:
                     chars.update({c:chars.get(c) + 1})

    print(chars) 
            
    minC = ""
    maxC = ""
    minAmount = 99999
    maxAmount = 0

    for c in listOfChars:
        c = c.lower()
        v = chars.get(c)
        if v > maxAmount:
            maxAmount = v
            maxC = c
        if v < minAmount:
            minAmount = v
            minC = c

    return [minC, minAmount, maxC, maxAmount]

def avg():
    f = open("pg24117.txt")

    s = f.read()
    
    print(s)

    l = s.split("***")
    
    s = l[2]

    words = s.split()

    total_length = 0
    
    num_words = len(words)
  
    print(s)

    chars = {"a":0,
             "b":0,
             "c":0,
             "d":0,
             "e":0,
             "f":0,
             "g":0,
             "h":0,
             "i":0,
             "j":0,
             "k":0,
             "l":0,
             "m":0,
             "n":0,
             "o":0,
             "p":0,
             "q":0,
             "r":0,
             "s":0,
             "t":0,
             "u":0,
             "v":0,
             "w":0,
             "x":0,
             "y":0,
             "z":0}

    listOfChars = chars.keys()

    for word in words:
        for c in word:
            c = c.lower()
            if c not in listOfChars:
                if c not in chars:
                    chars[c] = 1
                else:
                    chars[c] = chars + 1
                    

        total_length = total_length + len(word)

    average_length = total_length / num_words

    return average_length

def main():

     
    results = getinfo()
    print(" ---------- calculating ----------- ")
    print("The minimum character used is " + results[0] + "," + str(results[1]) + " times")
    print("The maximum character used is " + results[2] + "," + str(results[3]) + " times")
    print("The average length of the words is", avg())

if __name__ == "__main__":
        main()
