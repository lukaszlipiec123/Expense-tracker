from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MoneyChange
from django.utils import timezone


def home(request):
    return render(request, 'tracker/home.html')

def expenses(request):
    data = MoneyChange.objects.all().filter(person=request.user)
    sum = 0
    for obj in data:
        sum += obj.value
    return render(request, 'tracker/expenses.html', {"objects" : data, "sum" : sum})


@login_required()
def new_expense(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['value']:
            record = MoneyChange()
            record.title = request.POST['title']
            record.value = request.POST['value']
            if int(request.POST['value']) >= 0:
                record.isIncome = True
            else:
                record.isIncome = False
            record.pub_date = timezone.datetime.now()
            record.person = request.user
            record.save()
            #return redirect('/produc/' + str(record.id))
            return render(request, 'tracker/new_expense.html')
        else:
            return render(request, 'tracker/new_expense.html', {'error':'All fields are required.'})
    else:
        return render(request, 'tracker/new_expense.html')
