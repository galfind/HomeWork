vocab = ['а', 'и', 'е', "ё", 'о', 'у', "ы", "э", "ю", "я"]
text = input("Введите стихотворение ")
print(text)
text = text.split()
print(text)
res = list(map(lambda x: [i for i in x if i in vocab], text))
res = [len(res[i]) for i in range(len(res))]
if res.count(res[0]) == len(res):
    print("Парам пам-пам")
else:
    print('Не врифму!')