
from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import include

urlpatterns = [
    path('', redirect_block),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]