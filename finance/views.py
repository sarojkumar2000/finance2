from django.http import HttpResponse
from django.shortcuts import render,redirect
from finance.models import admin,Users
from decimal import Decimal
from datetime import datetime,timedelta
from .models import Users
from monthdelta import monthdelta
from dateutil.relativedelta import relativedelta

def home(request):
    return render(request,"index.html")
def adminLogin(request):
    return render(request,"admin-login.html")
def userLogin(request):
    return render(request,"user-login.html")
def user(request):
    username = request.POST.get('username')
    try:
        user=Users.objects.get(name=username)
        print(user.amount)
        context={'user':user}
        return render(request,"user.html",context)
    except Exception as e:
        error_message = "Invalid username or password."
        return render(request, "user-login.html", {"error_message": error_message})
def admin1(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        admin.objects.get(name=username, password=password)
        users_with_loan = Users.objects.filter(loan_type__isnull=False)
        context = {'username': 'Admin', 'users_with_loan': users_with_loan}
        return render(request, 'admin.html', context)
    except admin.DoesNotExist:
        error_message = "Invalid username or password."
        return render(request, "admin-login.html", {"error_message": error_message})

def applyloan(request):
    return render(request ,"apply-loan.html")
def save(request):
    if request.method == 'POST':
       
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        amount = Decimal(request.POST.get('amount'))
        interest = Decimal(request.POST.get('interest'))
        proof = request.POST.get('proof')
        address = request.POST.get('address')
        loan_type = request.POST.get('loan_type')
        tenure=Decimal(request.POST.get('tenure'))
        applied_date=datetime.now().date()
        lastpaid=applied_date
        next_due_date=datetime.now().date()
        next_due_amount=0
    
        
        if loan_type == 'monthly':
            
            interest_amount = amount * (interest / 100)
            next_due_date = applied_date + monthdelta(1)

            
        elif loan_type == 'daily':
          
            daily_interest = interest / 30
            interest_amount = amount + (amount * (daily_interest / 100) )
            next_due_date = applied_date + timedelta(days=1)
            

        user = Users(
        name=name,
        age=age,
        phone=phone,
        amount=amount,
        interest=interest,
        proof=proof,
        address=address,
        loan_type=loan_type,
        next_due=next_due_amount,
        next_due_date=next_due_date,
        applied_date=applied_date,
        lastpaid=lastpaid,
        interest_amount=interest_amount,
        tenure=tenure
    )


    user.save()
        

    return render(request,"apply-loan.html")





def pay_due(request, user_id):
    user=Users.objects.get(id=user_id)
    lastpaid=user.lastpaid
    amount_due=0
    next_due_date=user.next_due_date
    loan_type=user.loan_type
    if(lastpaid<next_due_date):
        user.next_due=0
        print("You have already paid")
    else:
        if(loan_type=='monthly'):      
            months_difference = relativedelta(datetime.now().date(), lastpaid).months
            if(months_difference==0):
                user.next_due=0
            else:
                user.next_due=months_difference*user.interest_amount
            
           
        elif(loan_type=='daily'):
            days_difference = (datetime.now().date() - lastpaid).days
            if(days_difference==0):
                user.next_due=0
            else:
                user.next_due=days_difference*user.interest_amount

           
      
    user.save()
  
    print(user.name)
    return render(request, "paydue.html",{'user': user})  

def paydue(request, user_id):
    user=Users.objects.get(id=user_id)

    return HttpResponse("Hello")  