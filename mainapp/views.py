from django.shortcuts import render
from mainapp.models import UserAnswers, UserQuestion, UserQuiz


def show_first_page(request):
    """
    Функция-обработчик стартовой страницы
    """
    all_quizes = UserQuiz.objects.all()
    if UserAnswers.objects.last() is not None:
        UserAnswers.objects.all().delete()
    existing_quiz = False
    if UserQuestion.objects.last() is not None:
        existing_quiz = True
    context = {'existing_quiz': existing_quiz, 'all_quizes': all_quizes}
    return render(request, 'mainapp/first_page.html', context)
