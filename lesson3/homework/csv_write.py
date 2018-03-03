import csv

get_answer = {"answ1": "отлично", "answ2": "норм", "answ3": "хреново"}


with open('out.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f,delimiter=";")
    for key,value in get_answer.items():
        writer.writerow([key,value])
