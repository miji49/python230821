# demoStr.py

print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))
result = strA.upper()
print(result)
print(strA.startswith("py"))
print(strA.endswith("ful"))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())
data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)
result2 = result.replace("spam","spam egg")
print(result2)

lst = result2.split()
print(lst)
print(":)".join(lst))

