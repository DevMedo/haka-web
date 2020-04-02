from django.shortcuts import render
from .forms import contactForm
from .models import contactRequest
from django.http import JsonResponse
import json
from django.views.defaults import page_not_found
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.user = request.user
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            cr = contactRequest(name=name, email=email)
            cr.save()
            data = {'name': cr.name,
                    'email': cr.email}
            return render(request, template_name="thankyou.html", context={'data': data})
    else:
        form = contactForm()
        return render(request, "index.html", context={'form': form})


def data(request):
    data = contactRequest.objects.all().order_by('pk')
    return render(request, "data.html", context={'data': data})


def error_404_view(request, exception):
    return page_not_found(request, exception, template_name="404.html")


def error_500_view(request):
    data = {}
    return render(request, '500.html', data)


def error_403_view(request, exception):
    data = {}
    return render(request, '403.html', data)


def error_400_view(request, exception):
    data = {}
    return render(request, '400.html', data)
