from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^$', login_required(views.MainView.as_view()), name='main'),
    url(r'^signin/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^main/$', views.main, name="main")
]
