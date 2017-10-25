from random import Random

def random_str(length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    random = Random()
    for i in range(length):	
        str+=chars[random.randint(0, len(chars)-1)]
    return str

res = random_str()
print(res)