from django.http import HttpResponse
from django.shortcuts import render, redirect


def redirect_block(request):
    return redirect('posts_list_url', permanent=True)