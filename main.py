# 1 - misol
numbers = (3, 6, 15,  5, 8)
result = list(filter(lambda x:  x % 3 == 1 and x > 5, numbers))

print(result)



# 2 - misol
numbers = (5, 4, 8, 7, 3)
result = list(filter(lambda x: 'Toq' if x % 3 == 1 else 'Juft', numbers))

print(result)


# 3 - misol
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
natija = list(filter(lambda x: x > 0 and x % 2 != 0, sonlar))

print(natija)



# 4 - misol
sozlar = ["Salom", "dunyo", "Python", "kod", "Funksiya", "sinov"]
katta_harf_sozlar = list(filter(lambda x: x[0].isupper(), sozlar))

print(katta_harf_sozlar)










































