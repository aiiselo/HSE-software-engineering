import main
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

adj_positive = {}
adj_negative = {}

# Далее необходимо создать файл с Вашей личной оценкой по каждому из слов в списке frequency.txt
est = open("estimations.txt", 'w')
results = model.predict(list(main.words_score.keys()))
for message, sentiment in zip(list(main.words_score.keys()), results):
    # if main.words_frequency[message] < 100: #для наиболее встречаемых слов ввожу значение самостоятельно
    score = list(sentiment.keys())[0]
    if score == 'neutral':
        score = 0
        main.words_score[message] = score
    elif score == 'positive':
        score = 1
        main.words_score[message] = score
        if main.words_cr[message] == 'ADJF':
            adj_positive[message] = main.words_frequency[message]
    else:
        score = -1
        main.words_score[message] = score
        if main.words_cr[message] == 'ADJF':
            adj_negative[message] = main.words_frequency[message]
    # else:
    #     print('Введи оценку для слова', message, ':')
    #     score = str(input())
    new_string = message + ' ' + str(score) + '\n'
    est.write(new_string)
est.close()

current_words_score = main.words_score
