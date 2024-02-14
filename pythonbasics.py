
def make_out_word(out, word):
    brackets = {"((": "))","[[": "]]", "{{": "}}","<<":">>"}
    opening = out[:2]
    closing = brackets[opening]
    return opening + word + closing

def first_two(a):
    return a[:2]

def combo_string(a,b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

def without_end(s):
    return s[1:-1]

def left2(s):
    return s[2:] + s[:2]

def caught_speeding(speed, isbirthday):
    if isbirthday:
        speed = speed - 5
    if speed <= 60:
        return 0
    elif 61 < speed < 80:
        return 1
    else:
        return 2


def main():
    print(make_out_word("<<>>","hi"))
    print(first_two("Hello"))
    print(combo_string("hi","hello"))
    print(without_end("coding"))
    print(left2("Hello"))
    print(caught_speeding(65, True))

if __name__ == "__main__":

    main()
