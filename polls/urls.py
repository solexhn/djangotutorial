from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # The index view for the polls app ex: /polls/
    path('', views.index, name="index"),
    # The detail view for a specific question ex: /polls/1/
    path("<int:question_id>/", views.detail, name="detail"),
    # The results view for a specific question ex: /polls/1/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # The vote view for a specific question ex: /polls/1/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]