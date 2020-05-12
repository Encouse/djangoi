from django.urls import path, re_path, include
from rest_framework import routers
from .views import InterviewView, QuestionView, AnswerView

router = routers.DefaultRouter()

router.register(r'interviews', InterviewView)
router.register(r'questions', QuestionView)
router.register(r'answers', AnswerView)


urlpatterns = [
    re_path(r'^',include(router.urls))
]
urlpatterns += router.urls
