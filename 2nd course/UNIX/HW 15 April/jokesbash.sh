url="https://bash.im/forweb/?u"
STATUS=$(curl -s -o /dev/null -w '%{http_code}' $url)
if [ $STATUS -eq 200 ]; then
    ID=$(curl -s $url | sed -n "s/.*>#\([0-9]*\)<.*/\1/p")
    url="bash.im/quote/$ID"
    curl -s -L $url > response.txt
    JOKE=$(cat response.txt | sed -n "s/.*meta property=\"og:description\" content=\(.*\)\/>.*/\1/p")
    JOKE=$(echo $JOKE | sed 's/\&#13;&#10;/\ \n /g')
    echo $JOKE
    echo $JOKE >> $1
else
    echo No Internet connection
    if [ -f $1 ]; then
	    ISEMPTY=$(cat $1)
	    if [ "${ISEMPTY:0:1}" == "" ]; then
	    	echo Database is empty
	    else
	    	gshuf -n 1 $1
	    fi
	else
		echo Database does not exist
	fi
fi