"""flowmeter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from django.urls import include
from flowmeter.views import index
from flowmeter.views import welcome
from flowmeter.views import login
from flowmeter.views import error
from flowmeter.views import user
from flowmeter.views import logout
from flowmeter.views import file
from flowmeter.views import system_setting

# 视图处理器路由
handler_urlpatterns = [
    path('login/', login.login_handler),
    path('admin/', user.user_handler),
    path('manufacturer/', user.user_handler),
    path('user/', user.user_handler),
    path('file/', file.file_handler),
    path('system/', system_setting.system_setting_handler),
]

# 错误页面路由
error_urlpatterns = [
    path('403/', error.error_403_view)
]

admin_urlpatterns = [
    path('view/', user.admin_view),
    path('add/', user.admin_add),
    path('import/', user.admin_import),
]

manufacturer_urlpatterns = [
    path('view/', user.manufacturer_view),
    path('add/', user.manufacturer_add),
    path('import/', user.manufacturer_import),
]

system_setting_urlpatterns = [
    path('register/', system_setting.control_register_view),
    path('frame/', system_setting.data_field_view),
]

# 视图路由
urlpatterns = [
    path('handler/', include(handler_urlpatterns)),
    path('error/', include(error_urlpatterns)),
    path('index/', index.index_view),
    path('welcome/', welcome.welcome_view),
    path('login/', login.login_view),
    path('admin/', include(admin_urlpatterns)),
    path('manufacturer/', include(manufacturer_urlpatterns)),
    path('system/', include(system_setting_urlpatterns)),
    path('logout/', logout.logout_view),
]
