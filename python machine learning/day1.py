with open('test_file.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split()

string = input()
cnt = 0
past_words = []
word_count={}
max_word_list = []

for line in lines:
    for word in line:
        if past_words == []:
            past_words.append(word)
            word_count[word] = 1
        else:
            if word not in past_words:      #단어가 전에 안나온 경우
                word_count[word] = 1
                past_words.append(word)
            else:       #전에 나온 경우
                word_count[word] += 1

for key in word_count.keys():
    if word_count[key] == max(word_count.values()):
        max_word_list.append(str(key))

print(word_count)
print(max_word_list)