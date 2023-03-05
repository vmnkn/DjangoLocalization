from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _
from .models import Model, Category

from django.utils import timezone
from django.shortcuts import redirect
import pytz


class Index(View):
    def get(self, request):
        models = Model.objects.all()
        current_time = timezone.now()
        context = {
            'models': models,
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones
        }

        return HttpResponse(render(request, 'index.html', context))

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('http://127.0.0.1:8000/app/')
