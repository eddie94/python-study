import pygal

#test_file을 열어서 lines에 모든 문장을 넣음
with open('test_file.txt') as f:
    lines = f.readlines()

#받아온 문장들을 공백을 기준으로 나눔
for i in range(len(lines)):
    lines[i] = lines[i].split()

string = input()        #찾고자 하는 문자열
cnt = 0                 #문자열이 나온 횟수
past_words = []         #예전에 나왔던 문자열을 저장
word_count={}           #문자열 당 나온 횟수를 저장
max_word_list = []      #가장 많이 나온 문자열을 저장

for line in lines:      #모든 문장들에 대해
    for word in line:       #한 문장에 대한 단어들에 대해 반복
        if past_words == []:        #만약 처음으로 나온 단어라면
            past_words.append(word)     #과거 문자열 리스트에 단어를 추가
            word_count[word] = 1        #그 단어의 카운트를 1로 설정
        else:
            if word not in past_words:      #단어가 전에 안나온 경우
                word_count[word] = 1        #단어의 카운트를 1로 두고
                past_words.append(word)     #과거 문자열 리스트에 단어를 추가
            else:       #전에 나온 경우
                word_count[word] += 1       #단어의 카운트를 1 증가

#모든 단어들에 대해 가장 많이 나온 단어들을 max_word_list에 추가
for key in word_count.keys():
    if word_count[key] == max(word_count.values()):
        max_word_list.append(str(key))

print(word_count)
print(max_word_list)

pie_chart = pygal.Pie()
pie_chart.title = 'Browser usage in February 2012 (in %)'
pie_chart.add('IE', 19.5)
pie_chart.add('Firefox', 36.6)
pie_chart.add('Chrome', 36.3)
pie_chart.add('Safari', 4.5)
pie_chart.add('Opera', 2.3)
pie_chart.render_to_file('test.svg')

chart = pygal.Pie()
chart.title = "단어별 나온 횟수"
for key in word_count.keys():
    chart.add(key,word_count[key])
chart.render_to_file('1234.svg')