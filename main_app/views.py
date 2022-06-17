

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from .filters import *


def homePage(request):
    seminars_count = Seminar.objects.all().count()
    workshops_count = Workshop.objects.all().count()
    skills_count = Skill.objects.all().count()

    context = {
        'seminars_count': seminars_count,
        'workshops_count': workshops_count,
        'skills_count': skills_count,
    }
    return render(request, 'home.html', context)


def addSeminar(request):
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        conducted = request.POST['conducted']
        date_started = request.POST['date_started']
        date_ended = request.POST['date_ended']
        time_duration = request.POST['time_duration']
        seminar_type = request.POST['seminar_type']

        saveSeminar = Seminar(title=title, address=address, conducted=conducted, date_started=date_started,
                              date_ended=date_ended, time_duration=time_duration, seminar_type=seminar_type)
        saveSeminar.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_seminar.html')


def addWorkshop(request):
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        conducted = request.POST['conducted']
        date_started = request.POST['date_started']
        date_ended = request.POST['date_ended']
        time_duration = request.POST['time_duration']
        seminar_type = request.POST['seminar_type']
        saveWorkshop = Workshop(title=title, address=address, conducted=conducted, date_started=date_started,
                                date_ended=date_ended, time_duration=time_duration, seminar_type=seminar_type)
        saveWorkshop.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_workshop.html', )


def addSkill(request):
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        conducted = request.POST['conducted']
        date_started = request.POST['date_started']
        date_ended = request.POST['date_ended']
        time_duration = request.POST['time_duration']
        skill_type = request.POST['skill_type']
        saveSkill = Skill(title=title, address=address, conducted=conducted, date_started=date_started,
                          date_ended=date_ended, time_duration=time_duration, skill_type=skill_type)
        saveSkill.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_skill.html', )


def viewSeminar(request):
    seminars = Seminar.objects.all()
    seminarFilter = SeminarFilter(request.GET, queryset=seminars)
    seminars = seminarFilter.qs

    context = {
        'seminars': seminars,
        'seminarFilter': seminarFilter
    }
    return render(request, 'view_seminar.html', context)


def viewWorkshop(request):
    workshops = Workshop.objects.all()
    workshopFilter = WorkshopFilter(request.GET, queryset=workshops)
    workshops = workshopFilter.qs

    context = {
        'workshops': workshops,
        'workshopFilter': workshopFilter
    }
    return render(request, 'view_workshop.html', context)


def viewSkill(request):
    skills = Skill.objects.all()
    skillFilter = WorkshopFilter(request.GET, queryset=skills)
    skills = skillFilter.qs

    context = {
        'skills': skills,
        'skillFilter': skillFilter
    }
    return render(request, 'view_skill.html', context)


def editSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    return render(request, 'edit_seminar.html', {'seminarItem': seminarItem})


def editWorkshop(request, workshopId):
    workshopItem = Workshop.objects.get(id=workshopId)

    context = {
        'workshopItem': workshopItem,
    }
    return render(request, 'edit_workshop.html', context)


def editSkill(request, skillId):
    skillItem = Skill.objects.get(id=skillId)

    context = {
        'skillItem': skillItem,
    }
    return render(request, 'edit_skill.html', context)


def updateSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    seminarItem.title = request.POST['title']
    seminarItem.address = request.POST['address']
    seminarItem.conducted = request.POST['conducted']
    seminarItem.date_started = request.POST['date_started']
    seminarItem.date_ended = request.POST['date_ended']
    seminarItem.time_duration = request.POST['time_duration']
    seminarItem.seminar_type = request.POST['seminar_type']
    seminarItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewSeminar)


def updateWorkshop(request, workshopId):
    workshopItem = Workshop.objects.get(id=workshopId)
    workshopItem.title = request.POST['title']
    workshopItem.address = request.POST['address']
    workshopItem.conducted = request.POST['conducted']
    workshopItem.date_started = request.POST['date_started']
    workshopItem.date_ended = request.POST['date_ended']
    workshopItem.time_duration = request.POST['time_duration']
    workshopItem.seminar_type = request.POST['seminar_type']
    workshopItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewWorkshop)


def updateSkill(request, skillId):
    skillItem = Skill.objects.get(id=skillId)
    skillItem.title = request.POST['title']
    skillItem.address = request.POST['address']
    skillItem.conducted = request.POST['conducted']
    skillItem.date_started = request.POST['date_started']
    skillItem.date_ended = request.POST['date_ended']
    skillItem.time_duration = request.POST['time_duration']
    skillItem.seminar_type = request.POST['seminar_type']
    skillItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewSkill)


def deleteSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    seminarItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewSeminar)


def deleteWorkshop(request, workshopId):
    workshopItem = Workshop.objects.get(id=workshopId)
    workshopItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewWorkshop)


def deleteSkill(request, skillId):
    skillItem = Skill.objects.get(id=skillId)
    skillItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewSkill)


class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()

                messages.success(request, 'you have successfully created an account')
                return render(request, 'login.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, 'Welcome, ' + user.username + ' you are now logged in')
            return redirect('home')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'login.html')


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')


class updateProfile(View):
    def get(self, request):
        return redirect('update_profile.html')
