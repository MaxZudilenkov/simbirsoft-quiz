from django.contrib import admin

from mainapp.models import UserAnswers, UserQuiz, UserQuestion, UserChoice


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer',)


class UserQuizAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request, obj=None):
        return False


class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz',)


class UserChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')


admin.site.register(UserAnswers, UserAnswerAdmin)
admin.site.register(UserQuiz, UserQuizAdmin)
admin.site.register(UserQuestion, UserQuestionAdmin)
admin.site.register(UserChoice, UserChoiceAdmin)

