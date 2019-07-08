# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


# Create your views here.

def index(request):
    return HttpResponse("Hello, you are at the root / index.")



class IndexView(generic.ListView):
    template_name = 'gdash_root/index.html'
    context_object_name = 'index_list'

    # Override queryset.
    def get_queryset(self):
        return
