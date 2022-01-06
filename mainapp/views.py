from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from mainapp.forms import CreateQuizForm, CreateQuestionForm
from mainapp.models import UserAnswers, UserQuestion, UserQuiz, UserChoice


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


def create_questions(request):
    """
    Функция для создания экземпляров моделей UserQuestion, UserChoice
    """
    choice_formset = modelformset_factory(UserChoice, fields=('text', 'is_correct'), extra=4)
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST, initial={'quiz': UserQuiz.objects.last()})
        form_a = choice_formset(request.POST)
        if form.is_valid() and form_a.is_valid():
            form_instance = form.save()
            instances = form_a.save(commit=False)
            for instance in instances:
                instance.question = form_instance
                instance.save()
        if 'create_quiz' in request.POST:
            return redirect('show_first_page')
    form = CreateQuestionForm(initial={'quiz': UserQuiz.objects.last()})
    form_a = choice_formset(queryset=UserChoice.objects.none())
    context = {'form': form, 'form_a': form_a}
    return render(request, 'mainapp/create_questions.html', context)
