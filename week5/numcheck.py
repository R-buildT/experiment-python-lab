def is_phone_number(num):
    if len(num) != 10:
        return False

    for i in range(10):
        if not num[i].isdecimal():
            return False
        
    return True

print(is_phone_number("9967526574"))