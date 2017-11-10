import base64

stringThing = input("str to b64encode: ").encode('utf-8')
res = base64.b64encode(stringThing)
print(res)