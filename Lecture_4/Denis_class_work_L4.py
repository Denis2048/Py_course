## L4
## Stringi
# li = [1, 2, 3]
# li[1] = 88
# print(li)
#
# st = "12365"
# print(st[0])

# st = "31314"
# print(len(st))
# st23 = "31314"
# print(id(st), id(st23))
# print(st*5)
# print(st+st)
#
# ch= "f"
# ch1 = "v"
# print(ord(ch))      # Возвращает int

# li = []
# for i in range(250, 275):         # Convert.
#     li.append(chr(i))
# print(li)
#
# for char in li:
#     print(ord(char), end=" ")

# st = "dfsdfsdf25s"
# for value in st:
#     print(value, end=" ")
# excl = "25"
# for value in st:
#     if value in excl:
#         continue
#     print(value)

# st = "dfsdfsdf25s"
# for i in range(len(st)):
#     print("index", i, "| value:", st[i])
#
# st = "Hello"
# for i in range(len(st)):
#     print("index", i, "| value:", st[i])     # Перебор по индексам.

# msg = "rome: grog, shakira."          # Шифр
# secret = 8
# secretMessahe = ""
# for char in msg:
#     secretMessahe += chr(ord(char) + secret)
# print(secretMessahe)
#
# result = ""
# for char in secretMessahe:
#     result += chr(ord(char) - secret)
# print(result)

# st = "dcsfdsdfdfdddddd"
# print(st[::-1])
# st = "[fix] dfsxfsdfsdf."
# st1 = "[bug] dfdfdfdf."
# st3 = "[hlp] dfdfdfdf."
# print(st[1:4])
# li = [st, st1, st3]
# for s in li:
#     res = s[1:4]
#     if res == "bug":
#         print("baag")
#     elif res == "fix":
#         print("fiiiiix")
#     else:
#         print(123)
#
# print(st[::3])   # Извлечь последовательность start:end:step.

## Методы
# st = "HelLo"
# print(st.upper())
# print(st.lower())
# print(input("->").upper())
#
# print(st.index("e"))
#
# name = "John"
# print(name[:2]+ "K" + name[3:])   # Замена символа.
#
# print(name.count("o"))
#
# print(name.isalpha())
#
# numbers = "12345"
# print(name.isalnum())
# print(name.islower())

# li = ["sdfddfdbug", "dfdfdf"]
# res = "|".join(li)
# res = res.replace("bug", "lol")
# print(res)
# print(res.endswith("."))

# st = "            dfdfd     sdfdf  "
# print(st.strip())
# print(st.title())
# print(st.swapcase())
# print(st.capitalize())

# st = "*dfdfdf*dfdfdf*dfdfd"   # Разбить по "*".
# print(st.split("*"))
