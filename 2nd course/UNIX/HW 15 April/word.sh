amount[1]=0; amount[2]=0; amount[3]=0; amount[4]=0; amount[5]=0; amount[6]=0; amount[7]=0; amount[8]=0; amount[9]=0; amount[10]=0; counter=0
sed -i "" '/^[[:space:]]*$/d' $1
while read line
do
	for symb in $line; do
		((counter++))
		if [[ "$symb" =~ .*".".* ]] || [[ "$symb" =~ .*"!".* ]] 
		then
			((amount[$counter]++)) 
			counter=0			
		fi
	done
done < $1
for((i=1;$i<11;i++)); do
	echo $i word in sentence: ${amount[$i]}
done