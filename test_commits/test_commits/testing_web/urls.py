from django.urls import path

from test_commits.testing_web.views import index

urlpatterns = (
    path('', index, name='index'),
)
