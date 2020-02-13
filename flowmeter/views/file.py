# coding=utf-8

import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import file as app_file_api
from flowmeter.common import common


class FileActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'file_upload': self.file_upload,
        }
        super().__init__(action_dict)

    def file_upload(self, request):

        path = app_file_api.generate_file_path()
        file = request_api.get_file(request)
        app_file_api.save_file(file, path)

        return Result.success(data=path)


def file_handler(request):

    result = FileActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))