from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import pymorphy2
import re

# Импортируем пакет со вспомогательными функциями
from matplotlib import mlab

morph = pymorphy2.MorphAnalyzer()
tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

tweets = []  # список со всеми не пустыми твиттами
tweets_time = []  # время в минутах
tweets_length = {}  # длина твиттов и количество твиттов с такой длиной
words_score = {}  # оценка положительное/нейтральное/отрицательное слово
words_cr = {}  # словарь со словом и частью его частью речи
words_frequency = {}  # количество твиттов, в котором встречалось это слово
data = open('data.txt')
tweets_amount = 0

useless_words = ['NUMR', 'NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL']

# Подготовка и обработка данных
for line in data:
    if line != "\n":

        tweets_amount += 1  # считаю количество твиттов
        time = line.split()[1].split(':')
        time = int(time[0]) * 60 + int(time[1])  # время в секундах
        current_tw_length = len(line.split()) - 2  # счетчик длины твиттов (всех) для twits_length.txt
        if current_tw_length not in tweets_length:
            tweets_length[current_tw_length] = 1
        else:
            temp = tweets_length[current_tw_length] + 1
            tweets_length[current_tw_length] = temp

        line = re.sub(r'# [a-zA-zа-яёА-ЯЁ0-9]*', '', line)  # убираю # и дату
        for junk_char in "%…$«»@*!&,^.=/+()[]{}><   :;”0123“’4‘56789?\"":  # избавляюсь от пунктуации и цифр
            line = line.replace(junk_char, '')
        current_line = line.lower().split()  # разрезаю твит на слова
        current_line.pop(0)

        # частотный анализ текста

        for i in current_line:  # убираю ссылки
            index = i.find("com")
            if index != -1:
                current_line.remove(i)
                continue
            index = i.find("http")
            if index != -1:
                current_line.remove(i)
                continue
            index = i.find("www")
            if index != -1:
                current_line.remove(i)

        # Добавляем слова в списки (frequency, score, cr), если они несут смысл
        if current_line != "":
            # print(current_line)
            # Добавляем преобразованные слова из твиттов в словарь
            tweets_time.append(time)
            tweets.append(current_line)
            for word in set(current_line):  # рассматриваем слова по одному разу
                current_word = morph.parse(word)[0].normal_form  # привожу слово в начальную форму
                CR = morph.parse(word)[0].tag.POS  # CR aka Chast' Rechi - получаю часть речи текущего слова
                words_cr[current_word] = CR
                if current_word != "-":
                    if current_word not in words_score:  # если слова нет в глобальном словаре - вставляю
                        if CR not in useless_words:  # рассматриваем слова только нужной части речи
                            words_score[current_word] = "None"  # временное значение
                            words_frequency[current_word] = 1
                    else:  # если есть - увеличиваю количество твиттов где оно повторяется
                        temp = words_frequency[current_word] + 1
                        words_frequency[current_word] = temp
