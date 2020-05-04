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
from flowmeter.views import statistic
from flowmeter.views import login
from flowmeter.views import error
from flowmeter.views import user
from flowmeter.views import logout
from flowmeter.views import file
from flowmeter.views import system_setting
from flowmeter.views import dtu_region
from flowmeter.views import dtu
from flowmeter.views import meter
from flowmeter.views import auth
from flowmeter.views import log
from flowmeter.views import websocket


# 视图处理器路由
handler_urlpatterns = [
    path('login/', login.login_handler),
    path('admin/', user.user_handler),
    path('dtu_user/', user.user_handler),
    path('manufacturer/', user.user_handler),
    path('user/', user.user_handler),
    path('file/', file.file_handler),
    path('system/', system_setting.system_setting_handler),
    path('dtu_region/', dtu_region.region_handler),
    path('dtu/', dtu.dtu_handler),
    path('meter/', meter.meter_handler),
    path('auth/', auth.auth_handler),
    path('log/', log.log_handler),
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

dtu_user_urlpatterns = [
    path('view/', user.dtu_user_view),
    path('add/', user.dtu_user_add),
    path('import/', user.dtu_user_import),
]

manufacturer_urlpatterns = [
    path('view/', user.manufacturer_view),
    path('add/', user.manufacturer_add),
    path('import/', user.manufacturer_import),
]

system_setting_urlpatterns = [
    path('register/', system_setting.control_register_view),
    path('frame/', system_setting.data_field_view),
    path('configure/', system_setting.configure_view),
]

dtu_region_urlpatterns = [
    path('view/', dtu_region.region_view),
    path('add/', dtu_region.region_add),
]

dtu_urlpatterns = [
    path('view/', dtu.dtu_view),
    path('add/', dtu.dtu_add),
]

meter_urlpatterns = [
    path('view/', meter.meter_view),
    path('add/', meter.meter_add),
    path('state/', meter.meter_state_view),
]

role_urlpatterns = [
    path('view/', auth.role_view),
    path('auth/view/', auth.auth_view),
]

log_urlpatterns = [
    path('opr/view/', log.opr_log_view),
    path('system/view/', log.system_log_view),
    path('alarm/view/', log.alarm_log_view),
]

statistic_urlpatterns = [
    path('admin/', statistic.admin_statistic_view),
    path('manufacturer/', statistic.manufacturer_statistic_view),
    path('dtu_user/', statistic.dtu_user_statistic_view),
]

# 视图路由
urlpatterns = [
    path('handler/', include(handler_urlpatterns)),
    path('error/', include(error_urlpatterns)),
    path('index/', index.index_view),
    path('statistic/', include(statistic_urlpatterns)),
    # path('websocket/', websocket.link_view),
    path('login/', login.login_view),
    path('admin/', include(admin_urlpatterns)),
    path('dtu_user/', include(dtu_user_urlpatterns)),
    path('manufacturer/', include(manufacturer_urlpatterns)),
    path('dtu_region/', include(dtu_region_urlpatterns)),
    path('dtu/', include(dtu_urlpatterns)),
    path('role/', include(role_urlpatterns)),
    path('meter/', include(meter_urlpatterns)),
    path('log/', include(log_urlpatterns)),
    path('system/', include(system_setting_urlpatterns)),
    path('logout/', logout.logout_view),
    path('', login.login_view),
]
