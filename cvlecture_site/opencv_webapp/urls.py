from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/$', views.uimage, name='uimage'),
    url(r'^dobj/$', views.dobj, name='dobj'),
<<<<<<< HEAD
    url(r'^join/$',views.signup, name='join'),
    url(r'^login/$',views.signin, name='login'),
=======
>>>>>>> bcde6757cd3e8f462d9e3530d628140754152c24
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
