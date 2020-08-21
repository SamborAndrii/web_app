from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect, HttpResponse, HttpResponseNotFound

from django.db.models import Q
from django.shortcuts import render

from accounts.forms import ProfileAddForm, ProfileEditForm
from accounts.models import Profile


# Create your views here.
def get_profiles_list(request):
    objects = Profile.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(Q(nickname__icontains=search) | Q(login__icontains=search))

    return render(
        request,
        'profiles.html',
        context={
            'result': objects,
            'search': search
        }
    )


def get_profile(request, slug):
    profile = Profile.objects.get(id=slug)
    return render(
        request,
        'profile.html',
        context={
            'profile': profile
        }
    )


def add_profile(request):
    if request.method == 'POST':
        form = ProfileAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profiles')

    elif request.method == 'GET':
        form = ProfileAddForm()

    return render(
        request,
        template_name='profile_add.html',
        context={
            'form': form
        }
    )


def edit_profile(request, slug):
    try:
        profile = Profile.object.get(id=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Profile id {slug} doesnt exist')
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/profiles/show/{slug}')

    elif request.method == 'GET':
        form = ProfileEditForm(instance=profile)

    return render(
        request,
        template_name='profile_edit.html',
        context={
            'form': form
        }
    )