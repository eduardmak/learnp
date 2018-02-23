

uch_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '5a', 'scores': [1,2,4,5,2]}]

avg_per_class = [sum(i.get("scores")) / len(i.get("scores")) for i in uch_list]
avg_per_school = sum(avg_per_class) / len(uch_list)

str_avg_ps = " ".join(str(avg_per_class))
str_avg_sch = " ".join(str(avg_per_school))

print("Средние оценки по ученика:" + str_avg_ps[1:-1])
print("Средние оценки по школе: " + str_avg_sch)
