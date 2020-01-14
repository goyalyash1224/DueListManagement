from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from customers.models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import NewCustomerForm, DocumentForm


from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    if request.user.is_authenticated:
        data = get_data(request.user)
        return render(request, 'customers/dashboard.html',{'agent':request.user,'data':data})
    else:
        return redirect('Home')


def get_data(user):
    content = []
    info = {}
    for customer in user.customers.all():
        info['fullname'] = customer.name
        info['dob'] = customer.dob
        content.append(info)

    return content


def add_new_customer(request):
    user = request.user

    if request.method == 'POST':
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.agent = user
            customer.save()
            return redirect('dashboard')
    else:
        form = NewCustomerForm()
    return render(request, 'customers/new_customer.html',{'form': form})


def customer_profile(request, id=id):
    agent = request.user
    customer = Customer.objects.get(id=id)
    context = {
        'agent': agent,
        'customer':customer,
    }
    if request.user.is_authenticated:
        return render(request, 'customers/customer_profile.html',context)
    return redirect('Home')



class UploadView(View):
    def get(self, request):
        doc_list = Document.objects.all()
        customer = Customer.objects.get(id =self.kwargs['id'])
        return render(self.request, 'customers/uploads/index.html', {'doc_list': doc_list,'customer':customer})

    def post(self, request):
        form = DocumentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            Document = form.save()
            data = {'is_valid': True, 'name': Document.file.name, 'url': Document.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


