
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from main_app import views as main_app


urlpatterns = [
                path('', views.homePage, name='home'),

                path('addSeminar/', views.addSeminar, name='add_seminar'),
                path('addWorkshop/', views.addWorkshop, name='add_workshop'),
                path('addSkill/', views.addSkill, name='add_skill'),
                path('Seminars/', views.viewSeminar, name='view_seminar'),
                path('Workshops/', views.viewWorkshop, name='view_workshop'),
                path('Skills/', views.viewSkill, name='view_skill'),
                path('editSeminar/<int:seminarId>/', views.editSeminar, name='edit_seminar'),
                path('editWorkshop/<int:workshopId>/', views.editWorkshop, name='edit_workshop'),
                path('editSkill/<int:skillId>/', views.editSkill, name='edit_skill'),
                path('updateSeminar/<int:seminarId>/', views.updateSeminar, name='update_seminar'),
                path('updateWorkshop/<int:workshopId>/', views.updateWorkshop, name='update_workshop'),
                path('updateSkill/<int:skillId>/', views.updateSkill, name='update_skill'),
                path('deleteSeminar/<int:seminarId>/', views.deleteSeminar, name='delete_seminar'),
                path('deleteWorkshop/<int:workshopId>/', views.deleteWorkshop, name='delete_workshop'),
                path('deleteSkill/<int:skillId>/', views.deleteSkill, name='delete_skill'),

              ]
