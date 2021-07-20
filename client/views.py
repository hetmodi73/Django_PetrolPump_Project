from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tank_master.models import tank
from datetime import datetime
from creditors_master.models import creditors
from django.db.models import Sum
from nozzlle_transaction.models import nozzlle_t
from django.http.response import JsonResponse
from rates.models import rate

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

    if total_petorl_price['total_price_petrol__sum'] is None :
        total_petorl_price['total_price_petrol__sum']=0
    if total_diesel_price['total_price_diesel__sum'] is None:
        total_diesel_price['total_price_diesel__sum']=0
    today_collection=total_petorl_price['total_price_petrol__sum']+total_diesel_price['total_price_diesel__sum']


    return render(request,"client/dashboard.html",{
        "petrol_stock":petrol_stock,
        "diesel_stock":diesel_stock,
        'pending_amount':data['pending_balance__sum'],
        'today_collection':today_collection
    })


def get_petrol_amount_by_month_chart(request):
    from django.db.models import Sum
    from datetime import datetime
    from calculation_master.models import calculation
    result = calculation.objects.annotate(month=TruncMonth('date')).values('month').annotate(
         no_of_ad=Sum('total_lit_petrol'))
    data = {'label': [], 'values': []}
    for ex in result:
        data['label'].append(datetime.strftime(ex['month'], '%B'))
        data['values'].append(ex['no_of_ad'])
        print(data)
    return JsonResponse(data)

