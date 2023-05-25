from django.urls import path

from test_commits.testing_web.views import index, index_plus, index_plus_name, mix_index

urlpatterns = (
    path('', index, name='index'),
    path('<int:pk>/', index_plus, name='index-plus'),
    path('<name>/', index_plus_name, name='index-plus-str'),

)
