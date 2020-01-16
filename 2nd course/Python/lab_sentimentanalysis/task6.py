import datetime
import main
import task4 as t4
import matplotlib.pyplot as plt
import pylab

main.tweets.reverse()
main.tweets_time.reverse()
t4.tweets_score.reverse()

current_time = 0
exit = 0
step = 0
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

for i in range(len(main.tweets)):
    if main.tweets_time[i] > 180 and exit == 1:
        break
    elif main.tweets_time[i] <= 180:
        if main.tweets_time[i] < window:
            current_amount = current_amount + 1
            if t4.tweets_score[i] == 1:
                pos_amount += 1
            elif t4.tweets_score[i] == -1:
                neg_amount += 1
            else:
                neut_amount += 1
        elif main.tweets_time[i] <= window + step:
            number_of_tweets.append(current_amount + prev_amount)
            prev_amount = prev_amount + current_amount
            current_amount = 0

            fraction_pos.append((pos_amount + prev_pos) * 100 / prev_amount)
            prev_pos += pos_amount
            pos_amount = 0

            fraction_neg.append((neg_amount + prev_neg) * 100 / prev_amount)
            prev_neg += neg_amount
            neg_amount = 0

            fraction_neut.append((neut_amount + prev_neut) * 100 / prev_amount)
            prev_neut += neut_amount
            neut_amount = 0
            step = 5
            window = window + step
            exit = 1
            #
#

# print(number_of_tweets)
# print(fraction_pos)
# print(fraction_neut)
# print(fraction_neg)
window = 30 * 60
step = 5
hr = open("hours.txt", 'w')
timeaxis = []
timeaxis.append(datetime.datetime.utcfromtimestamp(0).strftime('%H:%M'))
for i in range(len(number_of_tweets)):
    time = datetime.datetime.utcfromtimestamp(window).strftime('%H:%M')
    timeaxis.append(time)
    new_string = "00:00 - " + time + " : " + str(number_of_tweets[i]) + " " + str(
        round(fraction_pos[i] / 100, 2)) + "/" + str(round(fraction_neut[i] / 100, 2)) + "/" + str(
        round(fraction_neg[i] / 100, 2)) + "\n"
    window += step * 60
    hr.write(new_string)
hr.close()

plt.subplot(2, 1, 1)
plt.grid()
plt.plot(fraction_pos, linestyle="--", marker="o", color="g", label='N_pos')
plt.plot(fraction_neut, linestyle="--", marker="o", color="y", label='N_0')
plt.plot(fraction_neg, linestyle="-", marker="o", color="r", label='N_neg')
plt.xticks(range(len(timeaxis)), timeaxis, color='black', fontsize=5, rotation=90)
plt.title('Distribution of tweets classes in time')
plt.legend()
plt.ylabel('Fraction in percentage')

plt.subplot(2, 1, 2)
plt.grid()
pylab.stem(number_of_tweets, use_line_collection=True)
plt.ylim(0, 6000)
plt.xticks(range(len(timeaxis)), timeaxis, color='black', fontsize=5, rotation=90)
plt.ylabel('Number of tweets')
plt.show()
