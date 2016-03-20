"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa.views import test as qa_test
from qa.views import question_list, question_list_pop, question_detail,\
                     ask_form, answer_add, signup, user_login
from auth.views import test as auth_test


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', question_list),
    url(r'^login/$', user_login),
    url(r'^signup/$', signup),
    url(r'^ask/', ask_form),
    url(r'^popular/$', question_list_pop),
    url(r'^new/$', qa_test),
    url(r'^answer/$', answer_add, name='answer_add'),
    url(r'^question/(?P<question_id>[0-9]+)/$', question_detail, name='question_detail'),

]
