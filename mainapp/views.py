from django.shortcuts import render, redirect
from mainapp.forms import CreateQuizForm
from mainapp.models import UserAnswers, UserQuestion, UserQuiz


def create_quiz(request):
    """
    Функция для создания экземпляра модели UserQuiz
    """
    if request.method == 'POST':
        form = CreateQuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_question')
    form = CreateQuizForm()
    context = {'form': form}
    return render(request, 'mainapp/create_quiz.html', context)


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
