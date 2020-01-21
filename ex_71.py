f = open('latex.log', 'r', encoding='utf-8')
t = f.readlines()
f.close()
line_index = []
for i in t:
    if len(i) > 2:
        line_index.append(len(i))
sum = 0
for i in line_index:
    sum += int(i)
print(round(sum/len(line_index))-1)

