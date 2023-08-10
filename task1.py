def find_count(word):
    alphabet = 'аеёиоуыэюя'
    count = 0
    for i in word:
        if i in alphabet:
            count += 1
    return count

rythm = input("Введите стихотворение: ")
lines = rythm.split()
res = list()

for i in lines:
    count = find_count(i)
    res.append(count)

result = all(x == res[0] for x in res)

if result:
    print("Парам пам-пам")
else:
    print("Пам парам")