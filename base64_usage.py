import base64

stringThing = str(input("str to b64encode: "))
bytesThing = stringThing.encode(encoding='utf-8')
res = base64.b64encode(bytesThing)
print(res)