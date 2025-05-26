from django.shortcuts import redirect, render
from .models import Lead
from .forms import *

from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def lead_list(request):
    leads = Lead.objects.all()
    count = leads.count()
    context = {
        'leads': leads,
        'count': count
    }
    return render(request, 'show_all.html', context)


@login_required(login_url='login')
def edit_lead(request,id):
    lead = Lead.objects.get(id=id)
    lead_form = EditLeadForm(instance=lead)
    if request.method == 'POST':
        lead_form = EditLeadForm(request.POST, instance=lead)
        if lead_form.is_valid():
            lead_form.save()
            return redirect('lead_list')
    # if request.method == 'POST':
    #     lead.name = request.POST.get('name')
    #     lead.email = request.POST.get('email')
    #     lead.phone = request.POST.get('phone')
    #     lead.Source = request.POST.get('source')
    #     lead.note = request.POST.get('note')
    #     lead.Status = request.POST.get('status')
    #     lead.save()
    #     return redirect('lead_list')
    context = {
        'lead_form': lead_form,
        'lead': lead,
    }
    return render(request, 'edit_lead.html', context)


@login_required(login_url='login')
def add_lead(request): 
    lead_form = LeadForm()
    if request.method == 'POST':
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead_form.save()
            return redirect('lead_list')
    context = {
        'lead_form': lead_form
    }
    return render(request, 'add_lead.html', context)



def register(request):
    if request.user.is_authenticated:
        return redirect('lead_list')
    else:
        form = registerForm()
        if request.method == 'POST':
            re_form = registerForm(request.POST)
            if re_form.is_valid():
                re_form.save()
                return redirect('lead_list')
        context = { 
            'form': form
        }
        return render(request, 'Auth/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('lead_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lead_list')
            else:
                print("Invalid username or password")

        return render(request, 'Auth/login.html')
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')