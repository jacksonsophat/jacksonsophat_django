from django.urls import path

from . import views

# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

# app_name = "polls"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("<int:question_id>/", views.detail, name="detail"),
#     path("<int:question_id>/results/", views.results, name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

# app_name = "polls"
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('projects/', views.projects, name='projects'),
    path('local-news/', views.local_news, name='local_news'),
    path('testing-page/', views.testing_page, name='testing_page'),
    path('amazon-price-tracking/', views.amazon_price_tracking, name='amazon'),
]