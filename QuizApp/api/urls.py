from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('quiz/',views.QuizHome.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('quiz/<int:pk>',views.QuizView.as_view(),name="quiz-detail"),
    path('Option/',views.OptionsView.as_view(),name="quiz-Option"),
]
