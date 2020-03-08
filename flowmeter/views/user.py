# coding=utf-8

import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import user as app_user_api
from flowmeter.applications.api import dtu_region as conf_region_api
from flowmeter.applications.api import file as app_file_api
from flowmeter.settings import TMP_FILE_DIRECTORY_PATH


class UserActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_admin': self.query_admin,
            'query_dtu_user': self.query_dtu_user,
            'query_manufacturer': self.query_manufacturer,
            'check_email_unique': self.check_email_unique,
            'check_phone_unique': self.check_phone_unique,
            'create_admin': self.create_admin,
            'create_dtu_user': self.create_dtu_user,
            'create_manufacturer': self.create_manufacturer,
            "edit_admin": self.edit_admin,
            "edit_manufacturer": self.edit_manufacturer,
            "edit_dtu_user": self.edit_dtu_user,
            "switch_admin_state": self.switch_admin_state,
            "switch_dtu_user_state": self.switch_dtu_user_state,
            "switch_manufacturer_state": self.switch_manufacturer_state,
            "del_batch_admin": self.del_batch_admin,
            "del_batch_dtu_user": self.del_batch_dtu_user,
            "del_batch_manufacturer": self.del_batch_manufacturer,
            "import_admin": self.import_admin,
            "import_dtu_user": self.import_dtu_user,
            "import_manufacturer": self.import_manufacturer,
            "export_admin": self.export_admin,
            "export_dtu_user": self.export_dtu_user,
            "export_manufacturer": self.export_manufacturer,
        }
        super().__init__(action_dict)

    def query_admin(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        admins = app_user_api.find_admins_by_query_terms(param, page)

        return Result.success(data=admins, count=len(admins))

    def query_dtu_user(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        dtu_users = app_user_api.find_dtu_users_by_query_terms(param, page)

        return Result.success(data=dtu_users, count=len(dtu_users))

    def query_manufacturer(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        manufacturers = app_user_api.find_manufacturers_by_query_terms(param, page)

        return Result.success(data=manufacturers, count=len(manufacturers))

    def create_admin(self, request):

        admin_info = request_api.get_param(request)

        app_user_api.create_admin(admin_info)

        return Result.success()

    def create_dtu_user(self, request):

        dtu_user_info = request_api.get_param(request)

        app_user_api.create_dtu_user(dtu_user_info)

        return Result.success()

    def create_manufacturer(self, request):

        manufacturer_info = request_api.get_param(request)

        total_num = int(manufacturer_info.pop('total_num', 0))
        manufacturer = app_user_api.create_manufacturer(manufacturer_info)
        conf_region_api.add_region({'manufacturer_id': manufacturer.id, "total_num": total_num})

        return Result.success()

    def edit_admin(self, request):

        admin_info = request_api.get_param(request)

        app_user_api.edit_admin(admin_info)

        return Result.success()

    def edit_dtu_user(self, request):

        dtu_user_info = request_api.get_param(request)

        app_user_api.edit_dtu_user(dtu_user_info)

        return Result.success()

    def edit_manufacturer(self, request):

        manufacturer_info = request_api.get_param(request)

        app_user_api.edit_manufacturer(manufacturer_info)

        return Result.success()

    def check_email_unique(self, request):

        param = request_api.get_param(request)
        email = param.get('email')
        is_unique = app_user_api.check_email_unique(email)

        return Result.success(data=is_unique)

    def check_phone_unique(self, request):

        param = request_api.get_param(request)
        phone = param.get('phone')

        is_unique = app_user_api.check_phone_unique(phone)

        return Result.success(data=is_unique)

    def switch_admin_state(self, request):

        param = request_api.get_param(request)
        admin_id = param.get('admin_id')

        app_user_api.switch_admin_state_by_id(admin_id)

        return Result.success()

    def switch_dtu_user_state(self, request):

        param = request_api.get_param(request)
        dtu_user_id = param.get('dtu_user_id')

        app_user_api.switch_dtu_user_state_by_id(dtu_user_id)

        return Result.success()

    def switch_manufacturer_state(self, request):

        param = request_api.get_param(request)
        manufacturer_id = param.get('manufacturer_id')

        app_user_api.switch_manufacturer_state_by_id(manufacturer_id)

        return Result.success()

    def del_batch_admin(self, request):

        param = request_api.get_param(request)
        admin_ids = param.get('admin_ids')

        app_user_api.del_batch_admin(admin_ids)

        return Result.success()

    def del_batch_dtu_user(self, request):

        param = request_api.get_param(request)
        dtu_user_ids = param.get('dtu_user_ids')

        app_user_api.del_batch_dtu_user(dtu_user_ids)

        return Result.success()

    def del_batch_manufacturer(self, request):

        param = request_api.get_param(request)
        manufacturer_ids = param.get('manufacturer_ids')

        app_user_api.del_batch_manufacturer(manufacturer_ids)

        return Result.success()

    def import_admin(self, request):

        param = request_api.get_param(request)
        name = param.get('filename')
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_user_api.admin_import(filename)
        app_file_api.del_file(filename)

        return Result.success()

    def import_dtu_user(self, request):

        param = request_api.get_param(request)
        name = param.get('filename')
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_user_api.dtu_user_import(filename)
        app_file_api.del_file(filename)

        return Result.success()

    def import_manufacturer(self, request):

        param = request_api.get_param(request)
        name = param.get('filename')
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_user_api.manufacturer_import(filename)
        app_file_api.del_file(filename)

        return Result.success()

    def export_admin(self, request):

        param = request_api.get_param(request)
        name = app_file_api.generate_excel_file_name()
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_user_api.admin_export(param, filename)

        return Result.success(data=name)

    def export_dtu_user(self, request):

        param = request_api.get_param(request)
        name = app_file_api.generate_excel_file_name()
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_user_api.dtu_user_export(param, filename)

        return Result.success(data=name)

    def export_manufacturer(self, request):

        param = request_api.get_param(request)
        name = app_file_api.generate_excel_file_name()
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_user_api.manufacturer_export(param, filename)

        return Result.success(data=name)


@xframe_options_sameorigin
def admin_view(request):

    return render(request, 'admin/admin-list.html', {})


@xframe_options_sameorigin
def admin_add(request):

    return render(request, 'admin/admin-add.html', {})


@xframe_options_sameorigin
def admin_import(request):

    return render(request, 'admin/admin-import.html', {})


@xframe_options_sameorigin
def dtu_user_view(request):

    return render(request, 'dtu_user/dtu_user-list.html', {})


@xframe_options_sameorigin
def dtu_user_add(request):

    return render(request, 'dtu_user/dtu_user-add.html', {})


@xframe_options_sameorigin
def dtu_user_import(request):

    return render(request, 'dtu_user/dtu_user-import.html', {})


@xframe_options_sameorigin
def manufacturer_view(request):

    return render(request, 'manufacturer/manufacturer-list.html', {})


@xframe_options_sameorigin
def manufacturer_add(request):

    return render(request, 'manufacturer/manufacturer-add.html', {})


@xframe_options_sameorigin
def manufacturer_import(request):

    return render(request, 'manufacturer/manufacturer-import.html', {})


def user_handler(request):

    result = UserActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))