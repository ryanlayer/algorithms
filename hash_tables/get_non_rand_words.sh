cat The_Great_Gatsby.txt | fmt -w 1 | sed 's/[^a-zA-Z0-9]//g' | awk '{ print tolower($0) }' | sort -u > non_rand_words.txt
