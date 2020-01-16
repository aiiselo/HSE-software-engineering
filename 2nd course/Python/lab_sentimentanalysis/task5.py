import main
import task3 as t3
import pylab
import matplotlib.pyplot as plt
import numpy as np

# Задание №4. 5. Части речи.

counter = 0
adj_positive_list = list(t3.adj_positive.items())
adj_positive_list.sort(key=lambda i: i[1], reverse=True)
adj = open("adjectives.txt", 'w')
adj.write('Top-5 Positive:\n')
for i in adj_positive_list:
    new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/main.tweets_amount, 2)) + '%' + '\n'
    adj.write(new_string)
    counter += 1
    if counter == 5:
        break
counter = 0
adj_negative_list = list(t3.adj_negative.items())
adj_negative_list.sort(key=lambda i: i[1], reverse=True)
adj.write('\nTop-5 Negative:\n')
for i in adj_negative_list:
    new_string = str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(round(i[1]*100/main.tweets_amount, 2)) + '%' + '\n'
    adj.write(new_string)
    counter += 1
    if counter == 5:
        break
adj.close()

barWidth = 0.25 # ширина графика
pylab.subplot(1, 2, 1)
bar_pos = [adj_positive_list[0][1], adj_positive_list[1][1], adj_positive_list[2][1], adj_positive_list[3][1], adj_positive_list[4][1] ]
bars = ('1st', '2nd', '3rd', '4th', '5th')
y_pos = np.arange(len(bars))
plt.title('“Top-5 Positive”', fontweight='bold')
plt.bar(y_pos, bar_pos, color='#7da93e', width=barWidth, edgecolor='white', label='Positive')
plt.legend()
plt.xticks(y_pos, bars)

pylab.subplot(1, 2, 2)
bar_neg = [adj_negative_list[0][1], adj_negative_list[1][1], adj_negative_list[2][1], adj_negative_list[3][1], adj_negative_list[4][1] ]
bars = ('1st', '2nd', '3rd', '4th', '5th')
y_pos = np.arange(len(bars))
plt.bar(y_pos, bar_neg, color='#a33960', width=barWidth, edgecolor='white', label='Negative')
plt.title('“Top-5 Negative”', fontweight='bold')
plt.xticks(y_pos, bars)
plt.legend()
plt.show()
