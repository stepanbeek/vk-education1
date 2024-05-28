#Задание 3
low = int(input())
high = int(input())
between = True
while True:
    line = input()
    if not line:
        break
    if between:
        between = low < int(line) <= high
print(between)

#Задание 4
s= input()
print(('a' in s or 'o' in s) and 'i' not in s and 'e' not in s)

#Задание 5
integ = int(input())
flot = float(input())
intg_pos = int(input())
print(f"{integ:0=+10}")
print(f"{flot:#>10.2f}")
res_current = (f"{(intg_pos):0>16b}")
res_current = str(res_current)
result = str(res_current)
result = (result[::-1])
print('_'.join(result[i:i+4] for i in range(0, len(result),4))[::-1])

#Задача 6 
s = input()
c1 = len(s)
s = s.replace('!','')
s = s.replace('@','')
s = s.replace('#','')
s = s.replace('%','')
print(c1 - len(s))
print(s.lower())

#Задача 7
s = input()
n = s.split()
c1 = len(n)
c2 = 0
for _ in n:
    c2 += len(_)
print(c2/c1)

#Задание 8 
n = int(input())
max_values = []
for _ in range(n):
    record = input()
    values = record.split()
    values = [int(value) for value in values]
    max_value = max(values)
    max_values.append(max_value)
max_values.sort(reverse=True)
output = ';'.join(map(str, max_values))
print(output)

#Задание 9
input_string = input().lower()
unique_chars = set(input_string) - {' '}
print(' '.join(sorted(list(unique_chars))))

#Задание 10
line = input()
words = []
current_word = ""
for char in line:
    if char.isalnum():
        current_word += char
    elif current_word:
        words.append(current_word)
        current_word = ""
if current_word:
    words.append(current_word)
word_counts = {}
for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
most_common_word = ""
most_common_count = 0
for word, count in word_counts.items():
    if count > most_common_count:
        most_common_word = word
        most_common_count = count
print(most_common_word, most_common_count)