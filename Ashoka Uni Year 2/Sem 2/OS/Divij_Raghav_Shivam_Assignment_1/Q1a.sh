R=$(shuf -i 0-10000000 -n $N) #Changing value of N (10^3, 10^4, 10^5)
for file in $R
do
	echo $file>>random.txt
done
split -l $N/5 random.txt rand-  #Number of processes will be N/5
variable=($(ls rand*))
for filename in $variable
do
	max=$(cut -f1 -d"," $filename | sort -n | head -1 &)
	min=$(cut -f1 -d"," $filename | sort -n | tail -1 &)
	echo $max >> maxmin.txt
	echo $min >> maxmin.txt
done
wait

max=$(cut -f1 -d"," maxmin.txt | sort -n | head -1 )
min=$(cut -f1 -d"," maxmin.txt | sort -n | tail -1 )
echo $max
echo $min
