#from django.contrib import admin
from django.conf.urls import url,include
import xadmin


urlpatterns = [
    #url('admin/', admin.site.urls),
   url(r'^xadmin/', xadmin.site.urls),
url(r'^Ueditor/', include("DjangoUeditor.urls"))
]
