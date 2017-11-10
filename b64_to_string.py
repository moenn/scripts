import base64

stringThing = input("b64str to str: ")
res = base64.b64decode(stringThing)
print(res)