def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False

print(sleep_in(False, True))

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False

print(monkey_trouble(False, True))

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b
        
print(sum_double(7,8))

def diff21(n):
    x = abs(n-21)
    if n > 21:
        x = x * 2
    return x

print(diff21(24))

def parrot_trouble(talking, hour):
    if talking == False:
        return False
    if talking == True and (hour < 7 or hour > 20):
        return True

print(parrot_trouble(True, 3.5))

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    if a + b == 10:
        return True
    else:
        return False

print(makes10(10,5))

def near_hundred(n):
    if (abs(n-100) <= 10) or (abs(n-200) <= 10):
        return True
    else: 
        return False

print(near_hundred(105))

def pos_neg(a, b, negative):
    if ((a < 0 and b >= 0) or (a >= 0 and b < 0)) and negative == False:
        return True
    if ((a < 0 and b < 0) and negative == True):
        return True
    else: 
        return False

print(pos_neg(1, -1, False))

def not_string(str):
    if str[0] == "n" and str[1] == "o" and str[2] == "t":
    # alternate way => str[:3] which goes from start of string up to, but not including, index 3
    # alternate would be => if str[:3] == "not"
        return str
    else:
        str = "not " + str
        return str

print(not_string("sa"))

def missing_char(str, n):
    if n >= len(str):
        return str
    front = str[:n]
    back = str[n+1:]
    return front + back

print(missing_char("pupper", 4))

def front_back(str):
    first = str[0]
    last = str[len(str)-1]
    middle = str[1:len(str)-1]
    return last + middle + first

print(front_back("pupper"))

def front3(str):
    if len(str) < 3:
        return str + str + str
    front = str[:3]
    return front + front + front

print(front3("aPple"))