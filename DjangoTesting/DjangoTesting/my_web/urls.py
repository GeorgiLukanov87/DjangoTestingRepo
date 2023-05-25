from django.urls import path, include

from DjangoTesting.my_web.views import index, students, professors, prof_by_id, animal, create_professor, \
    delete_professor, edit_professor

urlpatterns = (
    path('', index, name='show index'),
    path('students/', students, name='students'),
    path('animal/', animal, name='animal'),

    # path('professors/', professors, name='professors'),
    # path('professors/<int:pk>/', prof_by_id, name='prof by id'),

    path('professors/', include([
        path('', professors, name='professors'),
        path('<int:pk>/', prof_by_id, name='prof by id'),
        path('create/', create_professor, name='create professor'),
        path('delete/<int:pk>/', delete_professor, name='delete professor'),
        path('edit/<int:pk>/', edit_professor, name='edit professor'),
    ])),

)
