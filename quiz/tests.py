from django.test import TestCase
from typing import List
from .services import QuizResultService
from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


class BaseTestCase(TestCase):
    def setUp(self):
        choices: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-1-1",
                "An elephant",
                True
            ),
            ChoiceDTO(
                "1-1-2",
                "A mouse",
                False
            )
        ]

        questions: List[QuestionDTO] = [
            QuestionDTO(
                "1-1",
                "Who is bigger?",
                choices
            )
        ]

        self.quiz_dto = QuizDTO(
            "1",
            "Animals",
            questions
        )

    def test_success_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-1"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 1.00)

    def test_failure_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-2"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.00)


class UserTestCase(TestCase):
    def setUp(self):
        choices: List[ChoiceDTO] = [
            ChoiceDTO(
                "2-1-1",
                "Орел",
                True
            ),
            ChoiceDTO(
                "2-1-2",
                "Тигр",
                False
            ),
            ChoiceDTO(
                "2-1-3",
                "Ворон",
                True
            ),
            ChoiceDTO(
                "2-1-4",
                "Лиса",
                False
            )
        ]

        questions: List[QuestionDTO] = [
            QuestionDTO(
                "2-1",
                "Кто является птицей?",
                choices
            )
        ]

        self.quiz_dto = QuizDTO(
            "2",
            "Птицы",
            questions
        )

    def test_success_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "2-1",
                ["2-1-1", '2-1-3']
            ),

        ]

        answers_dto = AnswersDTO(
            "2",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 1.00)

    def test_failure_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "2-1",
                ["2-1-1", '2-1-2']
            )
        ]

        answers_dto = AnswersDTO(
            "2",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.00)
