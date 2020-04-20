url="https://api.chucknorris.io/jokes/random"
STATUS=$(curl -s -o /dev/null -w '%{http_code}' $url)
if [ $STATUS -eq 200 ]; then
    curl -s $url > response.txt
	JOKE=$(cat response.txt | jq '.value')
	echo $JOKE >> $1
	echo $JOKE
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