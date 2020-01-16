from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import pymorphy2
import re
import matplotlib.pyplot as plt
import numpy as np
import pylab
from matplotlib import mlab


# Импортируем пакет со вспомогательными функциями
from matplotlib import mlab

morph = pymorphy2.MorphAnalyzer()
tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

tweets = []  # список со всеми не пустыми твиттами
tweets_time = [] # время в минутах
tweets_length = {}  # длина твиттов и количество твиттов с такой длиной
tweets_score = []  # оценка каждого твитта по третьему правилу
words_score = {}  # оценка положительное/нейтральное/отрицательное слово
adj_positive = {}
adj_negative = {}
tweet_score_1st_rule = {}  # оценка каждого твитта по первому правилу
tweet_score_2nd_rule = {}  # оценка каждого твитта по второму правилу
tweet_score_3rd_rule = {}  # оценка каждого твитта по третьему правилу
tweet_score_4th_rule = {}  # оценка каждого твитта по четвертому правилу
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
        time = int(time[0]) * 60 + int(time[1]) #время в секундах
        current_tw_length = len(line.split()) - 2  # счетчик длины твиттов (всех) для twits_length.txt
        if current_tw_length not in tweets_length:
            tweets_length[current_tw_length] = 1
        else:
            temp = tweets_length[current_tw_length] + 1
            tweets_length[current_tw_length] = temp

        line = re.sub(r'# [a-zA-zа-яёА-ЯЁ0-9]*', '', line)  # убираю # и дату
        for junk_char in "%…$«»@*!&,^./+()[]{}|:;”0123“’4‘56789?\"":  # избавляюсь от пунктуации и цифр
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
    # if tweets_amount == 5:
    #     break

# for key, value in words_frequency.items():
#     print(key, value)

# начало 1
# # В файл frequency.txt для каждого слова необходимо вывести количество твитов,
# # в котором слово встречается, и их процент от общего числа твитов
# words_frequency = list(words_frequency.items())
# words_frequency.sort(key=lambda i: i[1], reverse=True)
# freq = open("frequency.txt", 'w')
# for i in words_frequency:
#     new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/tweets_amount, 2)) + '%' + '\n'
#     freq.write(new_string)
# freq.close()
#
# # Аналогичным образом необходимо записать информацию о длине (числе слов) твитов в файл twits_length.txt:
# tweets_length = list(tweets_length.items())
# tweets_length.sort(key=lambda i: i[1], reverse=True)
# length = open("twits_length.txt", 'w')
# for i in tweets_length:
#     new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/tweets_amount, 2)) + '%' + '\n'
#     length.write(new_string)
# length.close()
# конец 1
#
# Далее необходимо создать файл с Вашей личной оценкой по каждому из слов в списке frequency.txt
est = open("estimations.txt", 'w')
results = model.predict(list(words_score.keys()))
for message, sentiment in zip(list(words_score.keys()), results):
    # if words_frequency[message] < 100: #для наиболее встречаемых слов ввожу значение самостоятельно
    score = list(sentiment.keys())[0]
    if score == 'neutral':
        score = 0
        words_score[message] = score
    elif score == 'positive':
        score = 1
        words_score[message] = score
        if words_cr[message] == 'ADJF':
            adj_positive[message] = words_frequency[message]
    else:
        score = -1
        words_score[message] = score
        if words_cr[message] == 'ADJF':
            adj_negative[message] = words_frequency[message]
    # else:
    #     print('Введи оценку для слова', message, ':')
    #     score = str(input())
    new_string = message + ' ' + str(score) + '\n'
    est.write(new_string)
est.close()

# # 4. Правила классификации. Оценка твитов. Сравнительный анализ.
# classif = open("classifications.txt", 'w')
# # Сумма оценок
# tweet_score_1st_rule['Good'] = 0
# tweet_score_1st_rule['Bad'] = 0
# tweet_score_1st_rule['Neutral'] = 0
# for tweet in tweets:
#     summa = 0
#     for word in tweet:
#         if word in words_score:
#             summa += words_score[word]
#     if summa > 1:
#         tweet_score_1st_rule['Good'] += 1
#     elif -1 <= summa <= 1:
#         tweet_score_1st_rule['Neutral'] += 1
#     else:
#         tweet_score_1st_rule['Bad'] += 1
# classif.write("Sum of scores where -1=<neutral<=1\n")
# for key, value in tweet_score_1st_rule.items():
#     new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / tweets_amount, 2)) + '%' + '\n'
#     classif.write(new_string)
# classif.write('\n')
#
# # Для каждого типа слов (положительные, нейтральные и отрицательные) определить долю слов такого типа в твите.
# # Тональность текста определяется по типу с наибольшей долей.
# tweet_score_2nd_rule['Good'] = 0
# tweet_score_2nd_rule['Bad'] = 0
# tweet_score_2nd_rule['Neutral'] = 0
# for tweet in tweets:
#     positive = 0
#     negative = 0
#     neutral = 0
#     for word in tweet:
#         if word in words_score:
#             if words_score[word] == 1:
#                 positive += 1
#             elif words_score[word] == -1:
#                 negative += 1
#             else:
#                 neutral += 1
#         else:
#             neutral += 1
#     if positive > max(negative, neutral):
#         tweet_score_2nd_rule['Good'] += 1
#     elif negative > max(neutral, positive):
#         tweet_score_2nd_rule['Bad'] += 1
#     else:
#         tweet_score_2nd_rule['Neutral'] += 1
# classif.write("Proportion rule\n")
# for key, value in tweet_score_2nd_rule.items():
#     new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / tweets_amount, 2)) + '%' + '\n'
#     classif.write(new_string)
# classif.write('\n')
#
# Мое правило №3
classif = open("classifications.txt", 'w')
tweet_score_3rd_rule['Good'] = 0
tweet_score_3rd_rule['Bad'] = 0
tweet_score_3rd_rule['Neutral'] = 0
for tweet in tweets:
    summa = 0
    for word in tweet:
        if word in words_score:
            summa += words_score[word]
    if summa >= 1:
        tweet_score_3rd_rule['Good'] += 1
        tweets_score.append(1)
    elif 0 <= summa < 1:
        tweet_score_3rd_rule['Neutral'] += 1
        tweets_score.append(0)
    else:
        tweet_score_3rd_rule['Bad'] += 1
        tweets_score.append(-1)
classif.write("Sum of scores where 0=<neutral<1\n")
for key, value in tweet_score_3rd_rule.items():
    new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / tweets_amount, 2)) + '%' + '\n'
    classif.write(new_string)
classif.write('\n')
#
# # Мое правило №4
#
# tweet_score_4th_rule['Good'] = 0
# tweet_score_4th_rule['Bad'] = 0
# tweet_score_4th_rule['Neutral'] = 0
# for tweet in tweets:
#     summa = 0
#     for word in tweet:
#         if word in words_score:
#             summa += words_score[word]
#     if summa >= 1:
#         tweet_score_4th_rule['Good'] += 1
#     elif -2 <= summa < 1:
#         tweet_score_4th_rule['Neutral'] += 1
#     else:
#         tweet_score_4th_rule['Bad'] += 1
# classif.write("Sum of scores where -2=<neutral<1\n")
# for key, value in tweet_score_4th_rule.items():
#     new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / tweets_amount, 2)) + '%' + '\n'
#     classif.write(new_string)
# classif.close()
#
# #строю графики
# barWidth = 0.25 # ширина графика
# bars1 = [tweet_score_1st_rule['Good'], tweet_score_2nd_rule['Good'], tweet_score_3rd_rule['Good'], tweet_score_4th_rule['Good']]
# bars2 = [tweet_score_1st_rule['Neutral'], tweet_score_2nd_rule['Neutral'], tweet_score_3rd_rule['Neutral'], tweet_score_4th_rule['Neutral']]
# bars3 = [tweet_score_1st_rule['Bad'], tweet_score_2nd_rule['Bad'], tweet_score_3rd_rule['Bad'], tweet_score_4th_rule['Bad']]
# r1 = np.arange(len(bars1))
# r2 = [x + barWidth for x in r1]
# r3 = [x + barWidth for x in r2]
#
# # Make the plot
# plt.bar(r1, bars1, color='#7da93e', width=barWidth, edgecolor='white', label='Good')
# plt.bar(r2, bars2, color='#d3dd37', width=barWidth, edgecolor='white', label='Neutral')
# plt.bar(r3, bars3, color='#cc4928', width=barWidth, edgecolor='white', label='Bad')
#
# # Add xticks on the middle of the group bars
# plt.xlabel('group', fontweight='bold')
# plt.xticks([r + barWidth for r in range(len(bars1))], ['-1=<neutral<=1', 'Proportion', '0 =<neutral<1', '-2=<neutral<1'])
#
# # Create legend & Show graphic
# plt.legend()
# plt.show()


# задание №4
#
# counter = 0
# adj_positive_list = list(adj_positive.items())
# adj_positive_list.sort(key=lambda i: i[1], reverse=True)
# adj = open("adjectives.txt", 'w')
# adj.write('Top-5 Positive:\n')
# for i in adj_positive_list:
#     new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/tweets_amount, 2)) + '%' + '\n'
#     adj.write(new_string)
#     counter += 1
#     if counter == 5:
#         break
# counter = 0
# adj_negative_list = list(adj_negative.items())
# adj_negative_list.sort(key=lambda i: i[1], reverse=True)
# adj.write('\nTop-5 Negative:\n')
# for i in adj_negative_list:
#     new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/tweets_amount, 2)) + '%' + '\n'
#     adj.write(new_string)
#     counter += 1
#     if counter == 5:
#         break
# adj.close()
#
# barWidth = 0.25 # ширина графика
# pylab.subplot (1, 2, 1)
# bar_pos = [adj_positive_list[0][1], adj_positive_list[1][1], adj_positive_list[2][1], adj_positive_list[3][1], adj_positive_list[4][1] ]
# bars = ('1st', '2nd', '3rd', '4th', '5th')
# y_pos = np.arange(len(bars))
# plt.bar(y_pos, bar_pos, color='#7da93e', width=barWidth, edgecolor='white', label='Positive')
# plt.legend()
# plt.xticks(y_pos, bars)
#
# pylab.subplot (1, 2, 2)
# bar_neg = [adj_negative_list[0][1], adj_negative_list[1][1], adj_negative_list[2][1], adj_negative_list[3][1], adj_negative_list[4][1] ]
# bars = ('1st', '2nd', '3rd', '4th', '5th')
# y_pos = np.arange(len(bars))
# plt.bar(y_pos, bar_neg, color='#a33960', width=barWidth, edgecolor='white', label='Negative')
# plt.xticks(y_pos, bars)
# plt.legend()
# plt.show()

tweets.reverse()
tweets_time.reverse()
tweets_score.reverse()

current_time = 0
exit = 0
step = 10
window = 30
prev_pos = 0
prev_neut = 0
prev_neg = 0
prev_amount = 0
fraction_pos = []
fraction_neg = []
fraction_neut = []
current_amount = 0
pos_amount = 0
neg_amount = 0
neut_amount = 0
number_of_tweets = []
for i in range(len(tweets)):
    if tweets_time[i] > 180 and exit == 1:
        break
    elif tweets_time[i] <= 180:
        if tweets_time[i] < window:
            current_amount = current_amount + 1
            if tweets_score[i] == 1:
                pos_amount += 1
            elif tweets_score[i] == -1:
                neg_amount += 1
            else:
                neut_amount += 1
        elif tweets_time[i] <= window + step:
            number_of_tweets.append(current_amount + prev_amount)
            prev_amount = prev_amount + current_amount
            current_amount = 0

            fraction_pos.append((pos_amount + prev_pos)*100/prev_amount)
            prev_pos += pos_amount
            pos_amount = 0

            fraction_neg.append((neg_amount + prev_neg)*100/prev_amount)
            prev_neg += neg_amount
            neg_amount = 0


            fraction_neut.append((neut_amount + prev_neut)*100/prev_amount)
            prev_neut += neut_amount
            neut_amount = 0

            window = window + step
            exit = 1

print(number_of_tweets)
print(fraction_pos)
print(fraction_neut)
print(fraction_neg)