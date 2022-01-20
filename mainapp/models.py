from django.db import models

from django.db import models


class UserAnswers(models.Model):
    question_uuid = models.CharField(max_length=50, unique=True)
    answer = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.answer


class UserQuiz(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Квиз"
        verbose_name_plural = "Квизы"

    def __str__(self):
        return self.title


class UserQuestion(models.Model):
    quiz = models.ForeignKey(
        UserQuiz, on_delete=models.CASCADE, related_name='question')
    text = models.TextField()

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text


class UserChoice(models.Model):
    question = models.ForeignKey(
        UserQuestion, on_delete=models.CASCADE, related_name='choice')
    text = models.CharField(verbose_name="Вариант ответа", max_length=200)
    is_correct = models.BooleanField(
        default=False, verbose_name="Правильный ответ")

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"

    def __str__(self):
        return self.text
