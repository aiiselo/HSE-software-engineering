#!/bin/bash
function no_ctrlc() {
    echo "===:: До свидания! Возвращайтесь ещё поиграть :) "
    exit
}

answer=""
read -p "===:: Привет! Это игровой автомат. Чтобы сыграть, нажмите Enter / Return. Чтобы  выйти, нажмите Ctrl+C >> " answer
while [ "$answer" != "" ]
    do
        echo $answer
        read -p "===:: Неверная кнопка!. Чтобы сыграть, нажмите Enter / Return. Чтобы  выйти, нажмите Ctrl+C >> " answer
    done
echo  "===:: Игра начинается!"

trap no_ctrlc SIGINT
victory=0

while true; do #начало игры
    a=""; b=""; c=""
    WIN=$(expr $RANDOM % 10 ) #если рандомное число 9 или 10, то выпадают одинаковые числа
    if [ $WIN -le 7 ]
    then
        a=$(expr $RANDOM % 10)
        b=$(expr $RANDOM % 10)
        c=$(expr $RANDOM % 10)
    else
        a=$(expr $RANDOM % 10)
        b=$a
        c=$a
    fi
    echo -ne "$a $b $c \r" #вывод чисел с последующим обновлением на той же строке
    read -t 1 -n 1 #ожидание ввода от пользователя в течение 1 секунды
    if [ "$?" -eq 0 ] #если ввел enter/return
    then
        if [ "$a" -eq "$b" ] && [ "$a" -eq "$c" ] #если все числа равны
        then
            ((victory++)) #увеличивается число побед
            if [ "$victory" -eq 4 ] #если больше 3х
                then
                    while [ "$a" -eq "$b" ] && [ "$a" -eq "$c" ] #подтасовываем числа, чтобы они были не равны
                    do
                        a=$(expr $RANDOM % 10)
                        b=$(expr $RANDOM % 10)
                        c=$(expr $RANDOM % 10)
                    done
                    echo -ne "$a $b $c \r" #сообщаем о проигрыше
                    echo " ===:: Ваши цифры: $a $b $c"
                    echo "Вы проиграли! :( "
                    victory=0
                    curl -s https://koteiki.com/wp-content/uploads/2018/02/cat-1-8.jpeg > result.png
            else #если число побед 3 или меньше
                echo " ===:: Ваши цифры: $a $b $c" #поздравляем с победой
                echo "Вы победили! :) "
                curl -s  https://avatars.mds.yandex.net/get-zen_doc/164147/pub_5c9ca1ce7dbfa800b562e8e7_5c9ca225b6557700b33cab1e/scale_1200 > result.png
            fi
        else
            victory=0 #если пользователь сам проиграл
            echo " ===:: Ваши цифры: $a $b $c"
            echo "Вы проиграли! :( "
            curl -s https://koteiki.com/wp-content/uploads/2018/02/cat-1-8.jpeg > result.png
        fi
        open result.png # открываем скачанный файл
    fi
done
echo
