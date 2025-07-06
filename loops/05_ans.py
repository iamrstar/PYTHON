input_str = "you are amazing"

for char in input_str:
    if input_str.count(char) == 1:  # Count occurrences of 'char' in 'input_str'
        print('Count is 1:', char)
        break
