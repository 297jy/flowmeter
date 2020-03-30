# coding=utf-8

import json
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import file as app_file_api
from flowmeter.common import common
from flowmeter.settings import TMP_FILE_DIRECTORY_PATH


class FileActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'file_upload': self.file_upload,
            'download_file': self.download_file,
        }
        super().__init__(action_dict)

    def file_upload(self, request):

        name = app_file_api.generate_file_name()
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)
        file = request_api.get_file(request)

        app_file_api.save_file(file, filename)

        return Result.success(data=name)

    def download_file(self, request):

        param = request_api.get_param(request)
        name = param.get('filename')
        filename = os.path.split(name)[1]
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, filename)

        file = app_file_api.read_binary_file(filename)
        return Result.success(data={"file": file, "filename": name}, data_type=Result.FILE_DATA_TYPE)


def file_handler(request):

    result = FileActionHandler().handle(request)
    if result.data_type == Result.JSON_DATA_TYPE:
        return HttpResponse(json.dumps(dict(result)))
    elif result.data_type == Result.FILE_DATA_TYPE:
        data = result.data
        return request_api.get_file_response(file=data.get('file'), filename=data.get('filename'))
