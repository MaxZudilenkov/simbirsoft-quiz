from django import forms

from mainapp.models import UserQuiz, UserQuestion, UserChoice


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = UserQuiz
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'quiz_title', "placeholder": "Введите название квиза..."}), }


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = UserQuestion
        fields = ('quiz', 'text')
        widgets = {'quiz': forms.HiddenInput(),
                   'text': forms.TextInput(attrs={'class': 'question_title', "placeholder": "Введите вопрос..."}), }


class CreateChoiceForm(forms.ModelForm):
    class Meta:
        model = UserChoice
        fields = ('question', 'text', 'is_correct')
        widgets = {'question': forms.HiddenInput(), }
        exclude = ('question',)
