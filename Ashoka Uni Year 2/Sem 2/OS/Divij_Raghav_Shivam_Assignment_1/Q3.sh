value=$(<words.txt)
grep $value q3.txt -o | wc -l
