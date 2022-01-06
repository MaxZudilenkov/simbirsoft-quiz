from quiz.dto import QuizDTO, AnswersDTO


class QuizResultService():

    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        user_answers = []
        right_answers = []
        count = 0
        for question in self.quiz_dto.questions:
            right_answers.append([])
            for choice in question.choices:
                if choice.is_correct == True:
                    right_answers[count].append(choice.uuid)
            count = count + 1
        right_user_answers = len(right_answers)
        for user_answer in self.answers_dto.answers:
            user_answers.append(user_answer.choices)
        for count in range(len(user_answers)):
            if str(right_answers[count]) != str(user_answers[count]):
                right_user_answers -= 1
        score = right_user_answers / len(right_answers)
        rounded_score = round(score, 2)
        return rounded_score
