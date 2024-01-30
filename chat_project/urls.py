"""
URL configuration for chat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import create_account, login_user, home, logout_user, delete_users, get_users
from chat_project import settings
from django.conf.urls.static import static
from chat_app.views import create_message, get_my_message, answer_message, answer_message_from_a_list, delete_all_my_messages, answer_an_answer_from_a_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_account/', create_account, name='create_account'),
    path('', login_user, name='login_user'),
    path('home/', home, name='home'),
    path('logout_user/', logout_user, name='logout_user'),
    path('delete_users/', delete_users, name="delete_users"),
    path('get_users/', get_users, name="get_users"),
    path('create_message/', create_message, name="create_message"),
    path('get_my_message/', get_my_message, name="get_my_message"),
    path('answer_message/', answer_message, name="answer_message"),
    path('answer_message_from_a_list/<int:id>/answer', answer_message_from_a_list, name="answer_choosed_message"),
    path('delete_all_my_messages/', delete_all_my_messages, name="delete_all_my_messages"),
    path('answer_an_answer_from_a_list/<int:id>/answer',answer_an_answer_from_a_list,name="answer_an_answer_from_a_list"),
] 




if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )