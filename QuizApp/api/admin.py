from django.contrib import admin
from .models import Quiz,Question,Option,Answer
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
# Register your models here.

# class OptionAdmin(NestedStackedInline):
#     model = Option
#     extra = 1

# class AnswerAdmin(NestedStackedInline):
#     model = Answer
#     extra = 1

# class QuestionAdmin(NestedStackedInline):
#     model = Question
#     inlines = [
#         OptionAdmin,
#         AnswerAdmin
#     ]
#     extra = 0

# class QuizAdmin(NestedModelAdmin):
#     model = Quiz
#     inlines = [
#         QuestionAdmin,
#     ]

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Option)
# admin.site.register(Question, QuestionAdmin)