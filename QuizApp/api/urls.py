from django.urls import path
from . import views


urlpatterns = [
    path('quiz/',views.QuizHome.as_view()),
    path('quiz/<int:pk>',views.QuizView.as_view(),name="quiz-detail"),
    path('Option/',views.OptionsView.as_view(),name="quiz-Option"),
    path('Current_answer/',views.AllCurrentAnswerView.as_view(),name="All-Current-Answer"),
    path('Current_answer/<int:pk>',views.CurrentAnswerView.as_view(),name="Current-Answer"),
]
