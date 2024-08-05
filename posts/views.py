from django.shortcuts import render
from django.http import HttpResponse


def text_answer(request):
    return HttpResponse('Введение в django, views')


def main_page(request):
    return render(request, template_name='main_page.html')
