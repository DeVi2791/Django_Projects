from django.conf.urls import include, url
from django.contrib import admin
#para utilizar vistas importando carpeta
from mainapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_denisse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #para utilizar una vista importando carpeta
    #url(r'^$', views.index),
    #para utilizar urls de cada app
    url(r'^',include('mainapp.urls'))
]
