from django.shortcuts import render
from .forms import contactForm
from .models import contactRequest
from django.http import JsonResponse
import json
from django.core import serializers
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            r=form.save(commit=False)
            r.user = request.user
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            plan = form.cleaned_data.get('plan')
            
            cr= contactRequest(name=name,email=email,plan=plan)
            cr.save()
            print("name:"+cr.name)
            print("email :",cr.email)
            print("plan:",cr.plan)
            data = {'name':cr.name,
            'email':cr.email,
            'plan':cr.plan}
            return render(request, template_name="thankyou.html",context={'data':data})
    else:
        form = contactForm()
        return render(request,"index.html",context={'form':form})

def data(request):
    #data = serializers.serialize("json",contactRequest.objects.all().order_by('pk'), fields=('name','email','plan'))
    data = contactRequest.objects.all().order_by('pk')
    return render(request,"data.html",context={'data':data})