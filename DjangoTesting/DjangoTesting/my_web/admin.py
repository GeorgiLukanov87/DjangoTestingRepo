from django.contrib import admin

from DjangoTesting.my_web.models import Student, Professor, Animal


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'level')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
