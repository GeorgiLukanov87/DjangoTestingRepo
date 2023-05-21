from django.shortcuts import render

from petstagram.pets.models import Pet


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(
        request,
        'pets/pet-details-page.html',
        context,
    )


def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')
