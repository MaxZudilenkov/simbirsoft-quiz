from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.views.generic import ListView
from mainapp.forms import CreateQuizForm, CreateQuestionForm
from mainapp.models import UserAnswers, UserQuestion, UserQuiz, UserChoice
from mainapp.my_quiz import Myquiz
from quiz.dto import AnswersDTO, AnswerDTO, QuizDTO, QuestionDTO, ChoiceDTO
from quiz.services import QuizResultService


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


def create_own_quiz(request):
    """
    Функция для создания QuizDTO из базы данных
    """
    path = request.get_full_path().split('/')[3]
    if path.find("?") != -1:
        current_quiz_pk = path[0:path.find("?")]
    else:
        current_quiz_pk = path
    current_quiz = UserQuiz.objects.get(pk=current_quiz_pk)
    own_questions = []
    OwnQuiz = QuizDTO(str(current_quiz.pk), current_quiz.title, own_questions)
    for one_question in current_quiz.question.all():
        own_choices = []
        for one_choice in one_question.choice.all():
            own_choices.append(
                ChoiceDTO(
                    uuid=str(
                        current_quiz.pk) + '-' + str(
                        one_question.pk) + '-' + str(
                        one_choice.pk),
                    text=one_choice.text,
                    is_correct=one_choice.is_correct))
        own_questions.append(
            QuestionDTO(
                uuid=str(
                    current_quiz.pk) + '-' + str(
                    one_question.pk),
                text=one_question.text,
                choices=own_choices))
    return OwnQuiz


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
    choice_formset = modelformset_factory(
        UserChoice, fields=('text', 'is_correct'), extra=4)
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST, initial={
                                  'quiz': UserQuiz.objects.last()})
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


def show_own_quiz(request, type, pk):
    """
    Функция-обработчик страницы прохождения квиза
    """
    if type == 'custom_quiz':
        current_quiz = create_own_quiz(request)
    else:
        current_quiz = Myquiz
    my_questions = current_quiz.questions
    for question in my_questions:
        UserAnswers.objects.update_or_create(question_uuid=question.uuid)
    paginator = Paginator(my_questions, 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    current_question_uuid = ''
    for question in page.object_list:
        current_question_uuid = question.uuid
    current_question = UserAnswers.objects.get(
        question_uuid=current_question_uuid).answer
    context = {"my_questions": page.object_list,
               'page': page, 'current_question': current_question, }
    if request.method == "POST":
        user_answer = request.POST.getlist("question_choice")
        next_question = request.POST.get("next")
        previous_question = request.POST.get("previous")
        question_uuid = request.POST.get("question_uuid")
        UserAnswers.objects.update_or_create(
            question_uuid=question_uuid, defaults={"answer": user_answer})
        if previous_question is not None:
            redirect_page = request.path_info + \
                "?page=" + str(page.previous_page_number())
        elif next_question is not None:
            redirect_page = request.path_info + \
                "?page=" + str(page.next_page_number())
        else:
            redirect_page = '/result/' + type + '/' + pk
        return redirect(redirect_page)
    return render(request, 'mainapp/own_quiz.html', context)


class CreatedQuizesListView(ListView):
    """
    Класс для отображения страницы со списком созданных квизов
    """
    model = UserQuiz
    template_name = 'mainapp/created_quizes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizes'] = UserQuiz.objects.all().order_by('title')
        return context


def delete_quiz(request, pk):
    """
    Функция для удаления квизов
    """
    quiz = UserQuiz.objects.get(pk=pk)
    quiz.delete()
    return redirect('created_quizes')


def show_result(request, type, pk):
    """
    Функция для отображения результата прохождения квиза
    """
    if type == "standard_quiz":
        quiz = Myquiz
    else:
        quiz = create_own_quiz(request)
    MyAnswers = AnswersDTO(
        '1', [
            AnswerDTO(
                i.question_uuid, i.answer) for i in UserAnswers.objects.all()])
    my_result_service = QuizResultService(quiz_dto=quiz, answers_dto=MyAnswers)
    result = my_result_service.get_result()
    percent = int(result * 100)
    context = {'percent': percent}
    return render(request, 'mainapp/show_result.html', context)
