from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/$', views.uimage, name='uimage'),
    url(r'^dobj/$', views.dobj, name='dobj'),
    url(r'^join/$',views.signup, name='join'),
    url(r'^login/$',views.signin, name='login'),
    url(r'^voca/$',views.voca, name='voca'),
    url(r'^second/$', views.second_view, name='second_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
