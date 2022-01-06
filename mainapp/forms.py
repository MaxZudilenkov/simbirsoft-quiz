from django import forms

from mainapp.models import UserQuiz


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = UserQuiz
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'quiz_title', "placeholder": "Введите название квиза..."}), }