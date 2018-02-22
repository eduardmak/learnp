def get_answer(question,answers):
    ans = answers.get(question).lower()
    return ans


answers_inp = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
question_inp = "привет"
print(get_answer(question_inp,answers_inp))