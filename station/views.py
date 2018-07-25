from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee


from .forms import ContactForm


User = get_user_model()
def home_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }

    return render(request, "index.html", context)

    # template_name = 'index.html'
    #
    # def get(self, request):
    #     form = ContactForm()
    #     return render(request, self.template_name, {'form': form})

def add_employee(request):

    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    phone = request.POST["phone"]
    email = request.POST["email"]

    employee = Employee(first_name=first_name, last_name=last_name, phone=phone, email=email)

    employee.save()


    return render(request, "index.html")




