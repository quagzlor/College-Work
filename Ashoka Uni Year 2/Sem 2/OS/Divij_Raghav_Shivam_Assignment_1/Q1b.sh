R=$(shuf -i 0-10000000 -n 100000) #constant N
for file in $R
do
	echo $file>>random.txt
done
split -l 100000/$P random.txt rand-  #varying value of P
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
