import main

# В файл frequency.txt для каждого слова необходимо вывести количество твитов,
# в котором слово встречается, и их процент от общего числа твитов
words_frequency = list(main.words_frequency.items())
words_frequency.sort(key=lambda i: i[1], reverse=True)  # сортировка по значению
freq = open("frequency.txt", 'w')
for i in words_frequency:
    new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/main.tweets_amount, 2)) + '%' + '\n'
    freq.write(new_string)
freq.close()

# Аналогичным образом необходимо записать информацию о длине (числе слов) твитов в файл twits_length.txt:
tweets_length = list(main.tweets_length.items())
tweets_length.sort(key=lambda i: i[1], reverse=True)
length = open("twits_length.txt", 'w')
for i in tweets_length:
    new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/main.tweets_amount, 2)) + '%' + '\n'
    length.write(new_string)
length.close()