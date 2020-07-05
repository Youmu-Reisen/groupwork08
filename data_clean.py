import csv
import re
name = []
date = []
time_zone = []
dic = []


def deleteDuplicate(li):
    temp_list = list(set([str(i) for i in li]))
    li = [eval(i) for i in temp_list]
    return li

with open("date_data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        name.append(row[0])
        date.append(row[1])
        time_zone.append(row[2])

for i in range(len(name)):
    dic_row = {name[i]:(date[i],time_zone[i])}
    dic.append(dic_row)


dic = deleteDuplicate(dic) # 去重


# 统计
d = {}
for i in dic:
    if not list(i.values())[0] in d:
        d[list(i.values())[0]] = 1
    else:
        d[list(i.values())[0]] += 1


keys = list(d.keys())
values = list(d.values())

res = []
for i in range(len(keys)):
    res.append([keys[i][0],keys[i][1],values[i]])

# 数据规范化
pattern = re.compile("\d{4}-\d{2}")

for i in res:
    if pattern.search(i[0]) == None:
        res.remove(i)



with open('clean_data.csv','w',newline="") as csvFile:
    writer = csv.writer(csvFile)
    for i in res:
        writer.writerow(i)
