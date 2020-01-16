import main
import task3 as t3
import matplotlib.pyplot as plt
import numpy as np

# 4. Правила классификации. Оценка твитов. Сравнительный анализ.
classif = open("classifications.txt", 'w')
tweets_score = []  # оценка каждого твитта по третьему правилу
tweet_score_1st_rule = {}  # оценка каждого твитта по первому правилу
tweet_score_2nd_rule = {}  # оценка каждого твитта по второму правилу
tweet_score_3rd_rule = {}  # оценка каждого твитта по третьему правилу
tweet_score_4th_rule = {}  # оценка каждого твитта по четвертому правилу
# Сумма оценок

tweet_score_1st_rule['Good'] = 0
tweet_score_1st_rule['Bad'] = 0
tweet_score_1st_rule['Neutral'] = 0
for tweet in main.tweets:
    summa = 0
    for word in tweet:
        if word in t3.current_words_score:
            summa += t3.current_words_score[word]
    if summa > 1:
        tweet_score_1st_rule['Good'] += 1
    elif -1 <= summa <= 1:
        tweet_score_1st_rule['Neutral'] += 1
    else:
        tweet_score_1st_rule['Bad'] += 1
classif.write("Sum of scores where -1=<neutral<=1\n")
for key, value in tweet_score_1st_rule.items():
    new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / main.tweets_amount, 2)) + '%' + '\n'
    classif.write(new_string)
classif.write('\n')

# Тональность текста определяется по типу с наибольшей долей.

tweet_score_2nd_rule['Good'] = 0
tweet_score_2nd_rule['Bad'] = 0
tweet_score_2nd_rule['Neutral'] = 0
for tweet in main.tweets:
    positive = 0
    negative = 0
    neutral = 0
    for word in tweet:
        if word in t3.current_words_score:
            if t3.current_words_score[word] == 1:
                positive += 1
            elif t3.current_words_score[word] == -1:
                negative += 1
            else:
                neutral += 1
        else:
            neutral += 1
    if positive > max(negative, neutral):
        tweet_score_2nd_rule['Good'] += 1
    elif negative > max(neutral, positive):
        tweet_score_2nd_rule['Bad'] += 1
    else:
        tweet_score_2nd_rule['Neutral'] += 1
classif.write("Proportion rule\n")
for key, value in tweet_score_2nd_rule.items():
    new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / main.tweets_amount, 2)) + '%' + '\n'
    classif.write(new_string)
classif.write('\n')

# Мое правило №3

tweet_score_3rd_rule['Good'] = 0
tweet_score_3rd_rule['Bad'] = 0
tweet_score_3rd_rule['Neutral'] = 0
for tweet in main.tweets:
    summa = 0
    for word in tweet:
        if word in t3.current_words_score:
            summa += t3.current_words_score[word]
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
    new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / main.tweets_amount, 2)) + '%' + '\n'
    classif.write(new_string)
classif.write('\n')

# Мое правило №4

tweet_score_4th_rule['Good'] = 0
tweet_score_4th_rule['Bad'] = 0
tweet_score_4th_rule['Neutral'] = 0
for tweet in main.tweets:
    summa = 0
    for word in tweet:
        if word in t3.current_words_score:
            summa += t3.current_words_score[word]
    if summa >= 1:
        tweet_score_4th_rule['Good'] += 1
    elif -2 <= summa < 1:
        tweet_score_4th_rule['Neutral'] += 1
    else:
        tweet_score_4th_rule['Bad'] += 1
classif.write("Sum of scores where -2=<neutral<1\n")
for key, value in tweet_score_4th_rule.items():
    new_string = key + ' - ' + str(value) + ' - ' + str(round(value * 100 / main.tweets_amount, 2)) + '%' + '\n'
    classif.write(new_string)
classif.close()

# строю графики

a, b, c = 0, 0 , "dwdw"
barWidth = 0.25  # ширина графика
bars1 = [tweet_score_1st_rule['Good'], tweet_score_2nd_rule['Good'], tweet_score_3rd_rule['Good'],
         tweet_score_4th_rule['Good']]
bars2 = [tweet_score_1st_rule['Neutral'], tweet_score_2nd_rule['Neutral'],
         tweet_score_3rd_rule['Neutral'], tweet_score_4th_rule['Neutral']]
bars3 = [tweet_score_1st_rule['Bad'], tweet_score_2nd_rule['Bad'], tweet_score_3rd_rule['Bad'],
         tweet_score_4th_rule['Bad']]
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='#7da93e', width=barWidth, edgecolor='white', label='Good')
plt.bar(r2, bars2, color='#d3dd37', width=barWidth, edgecolor='white', label='Neutral')
plt.bar(r3, bars3, color='#cc4928', width=barWidth, edgecolor='white', label='Bad')

# Add xticks on the middle of the group bars
plt.title('Amount of good/neutral/bad tweets by classes', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))],
           ['-1=<neutral<=1', 'Proportion', '0 =<neutral<1', '-2=<neutral<1'])

# Create legend & Show graphic
plt.legend()
plt.show()
