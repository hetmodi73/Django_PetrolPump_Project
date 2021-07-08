from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tank_master.models import tank

# Create your views here.
@login_required
def home(request):
    return render(request,"client/home.html")

def dashboard(request):
    from datetime import datetime
    today=tank.objects.get(date=datetime.utcnow().date());
    petrol_stock=today.petrol_closing
    diesel_stock=today.diesel_closing

    # creditor amount
    from django.db.models import Sum
    from creditors_master.models import creditors
    data = creditors.objects.all().aggregate(Sum('pending_balance'))
    print(data)
    #nozzell trancsations
    from nozzlle_transaction.models import nozzlle_t
    data1=nozzlle_t.objects.filter(date=datetime.utcnow().date())
    total_petorl_price=data1.aggregate(Sum('total_price_petrol'))
    total_diesel_price=data1.aggregate(Sum('total_price_diesel'))
    print(total_petorl_price)
    today_collection=total_petorl_price['total_price_petrol__sum']+total_diesel_price['total_price_diesel__sum']


    return render(request,"client/dashboard.html",{
        "petrol_stock":petrol_stock,
        "diesel_stock":diesel_stock,
        'pending_amount':data['pending_balance__sum'],
        'today_collection':today_collection
    })