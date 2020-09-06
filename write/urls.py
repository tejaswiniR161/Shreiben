from django.conf.urls import url,include
from django.conf import settings
from django.views.static import serve
from . import views
urlpatterns = [
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^AddLetter/', views.AddLetter, name="addl"),
    url(r'^addImg/', views.addImgr, name="addimg"),
    url(r'^SignUpSave/', views.SignUpSave, name="signupsave"),
    url(r'^SignUp/', views.SignUp, name="signup"),
    url(r'^LogIn/', views.LogIn, name="login"),
    url(r'^LogOut/', views.LogOut, name="logout"),
    url(r'^AddHandWriting/', views.AddHandWriting, name="addh"),
    url(r'^Convert/', views.Convert, name="conv"),
    url(r'^Output/', views.Output, name="output"),
    url(r'^ConvertToText/',views.ConvertToText,name="convtotext"),
    url(r'^$', views.Home, name="home"),
]