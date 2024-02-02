
myList = [7,7,8,9,55,3,2]

def p1(S):

    for i in range(len(S)-1):
        if S[i]== 7:
            if S[i+1]== 7:
                return True
    return False

def p2(S):

    primes = [2, 3, 5, 7, 11]
    total = 0
    
    for num in S:
        if num in primes and primes.index(num) <= 4:
            break
        total = total + num
    print(total)

def p3(S):

    total = 0
    ex = False

    for num in S:
        if num == 2:
            ex = True
        elif num == 3:
            ex = False
        elif not ex:
            total = total + num

    return total
    


def main():
    
    print(p1([7,7,8,9,55,3,2]))
    p2([1,4,2,3,6])
    print(p3([1,4,4]))
    

if __name__ == "__main__":

    main()
