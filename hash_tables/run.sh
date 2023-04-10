python hash_functions.py rand_words.txt ascii | python histogram.py     ascii_hash_function_rand.png "Hashed value" "Freq"
python hash_functions.py non_rand_words.txt ascii | python histogram.py ascii_hash_function_nonrand.png "Hashed value" "Freq"

python hash_functions.py rand_words.txt rolling | python histogram.py     rolling_hash_function_rand.png "Hashed value" "Freq"
python hash_functions.py non_rand_words.txt rolling | python histogram.py rolling_hash_function_nonrand.png "Hashed value" "Freq"

python hash_functions.py rand_words.txt python | python histogram.py     python_hash_function_rand.png "Hashed value" "Freq"
python hash_functions.py non_rand_words.txt python | python histogram.py python_hash_function_nonrand.png "Hashed value" "Freq"
