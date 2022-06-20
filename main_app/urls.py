from django.urls import path
from . import views
from .views import LoginView, RegistrationView, ProfileView, ViewProfile, edit_profile


urlpatterns = [
                path('', views.homePage, name='home'),
                path('register', RegistrationView.as_view(), name="register"),
                path('login', LoginView.as_view(), name="login"),

                path('profile', ProfileView.as_view(), name="profile"),

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
                path('viewprofile', ViewProfile.as_view(), name="view_profile"),
                path('edit_profile', views.edit_profile, name="edit_profile"),

              ]
