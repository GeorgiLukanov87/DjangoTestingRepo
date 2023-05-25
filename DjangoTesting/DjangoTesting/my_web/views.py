from django.shortcuts import render, redirect

from DjangoTesting.my_web.forms import ProfessorCreateForm, ProfessorDeleteForm, ProfessorEditForm
from DjangoTesting.my_web.models import Student, Professor, Animal


def index(request):
    return render(
        request,
        'welcome.html',
    )


def students(request):
    students_list = Student.objects.all()

    context = {
        'students': students_list,
    }

    return render(
        request,
        'students.html',
        context,
    )


def professors(request):
    profs_list = Professor.objects.all()

    if not profs_list:
        return redirect("show index")

    context = {
        'professors': profs_list,
    }

    return render(
        request,
        "professors.html",
        context,
    )


def animal(request):
    animals = Animal.objects.all()
    context = {
        'animal': animals,
    }

    return render(
        request,
        'animal.html',
        context,
    )


def prof_by_id(request, pk):
    current_prof = Professor.objects.filter(pk=pk).get()
    if not current_prof:
        return redirect("show index")

    context = {
        'pro': current_prof,
    }

    return render(
        request,
        'pro_by_id.html',
        context,
    )


def create_professor(request):
    if request.method == 'GET':
        form = ProfessorCreateForm()
    else:
        form = ProfessorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professors')

    context = {
        'form': form,
    }

    return render(
        request,
        'create-prof.html',
        context,
    )


def delete_professor(request, pk):
    professor = Professor.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = ProfessorDeleteForm(instance=professor)
    else:
        form = ProfessorDeleteForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professors')

    context = {
        'form': form,
        'professor': professor,
    }

    return render(
        request,
        'delete-prof.html',
        context,
    )


def edit_professor(request, pk):
    professor = Professor.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = ProfessorEditForm(instance=professor)
    else:
        form = ProfessorEditForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professors')

    context = {
        'form': form,
        'id': pk,
    }

    return render(
        request,
        'edit-prof.html',
        context,
    )
