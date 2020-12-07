from collections import defaultdict


class Answers:
    def __init__(self):
        self.counts = defaultdict(int)
        self.respondents = 0

    def add(self, yes_answers):
        self.respondents += 1
        for ans in yes_answers:
            self.counts[ans] += 1

    def affirmative(self):
        return self.counts.keys()

    def all_affirmative(self):
        all_affirmative_qs = [
            k for [k, cnt] in self.counts.items() if cnt == self.respondents
        ]
        return all_affirmative_qs


def get_input(file_path):
    with open(file_path) as infile:
        contents = infile.read().strip()
    form = contents.split('\n\n')
    return form


def answers_from_form(form):
    answers = Answers()
    for line in form.split('\n'):
        answers.add(line)
    return answers


def count_any_affirmative(answer_list):
    return sum(len(a.affirmative()) for a in answer_list)


def count_all_affirmative(answer_list):
    return sum(len(a.all_affirmative()) for a in answer_list)


def main():
    forms = get_input('input.txt')
    answer_list = [answers_from_form(f) for f in forms]
    affirmative_count = count_any_affirmative(answer_list)
    print(f'Part 1: {affirmative_count}')
    all_affirmative_count = count_all_affirmative(answer_list)
    print(f'Part 2: {all_affirmative_count}')


if __name__ == '__main__':
    main()
