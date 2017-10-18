from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import (
login ,logout ,PasswordResetDoneView, PasswordResetView , PasswordResetConfirmView, PasswordResetCompleteView)
app_name= 'music'
urlpatterns = [


    url(r'^$', views.IndexView.as_view() , name="index"),
    #music/login/
    url(r'^login/$',login,{'template_name':'music/login.html'}, name="login" ),
    #music/logout/
    url(r'^logout/$',logout,{'template_name':'music/logout.html'}, name="logout"),
    #music/register/
    url(r'^register/$', views.UserFormView.as_view() , name="register"),
    #music/profile/
    url(r'^profile/$', views.profile, name="profile"),
    #music/profile/edit/
    url(r'^profile/edit/$', views.edit_profile, name="edit-profile"),
    #music/changepassword/
    url(r'^change-password/$', views.change_password, name="change-password"),
    #/music/71/
    url(r'^(?P<pk>[0-9]+)/$' ,views.DetailView.as_view(), name='detail'),
    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    #/music/1/add/
    url(r'^(?P<pk>[0-9]+)/add/$', views.SongCreate.as_view() , name='song-add'),
    #/music/album/2/
    url(r'album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),
    #/music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    #/music/album/2/deletesong/
    url(r'album/(?P<pk>[0-9]+)/deletesong/$', views.SongDelete.as_view(), name='song-delete'),
    #/music/allsongs/
    url(r'^allsongs/$', views.AllSongs.as_view(), name='all-songs'),
    #/music/reset-password/
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='music/reset_password.html',
    success_url=reverse_lazy('music:password_reset_done'),
    email_template_name='music/reset_password_email.html')
    , name='reset-password'),

    #music/reset-password-done/
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(
    template_name='music/reset_password_done.html')
    , name='password_reset_done'),
    #music/reset-password/confirm/
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    PasswordResetConfirmView.as_view(success_url=reverse_lazy('music:password_reset_complete'))
    , name='password_reset_confirm'),

    url(r'^reset-password/complete/$',
     PasswordResetCompleteView.as_view(template_name='music/reset_password_done.html'), name='password_reset_complete'),








]
