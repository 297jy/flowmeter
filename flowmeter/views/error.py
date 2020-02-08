# coding=utf-8

from django.shortcuts import render


def error_403_view(request):

    return render(request, 'error-403.html', {})
