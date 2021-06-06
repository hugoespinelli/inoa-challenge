import json

from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import View

from .models import StockRealtimeVW, AlertUserStocks


def index(request):
    stocks_queryset = StockRealtimeVW.objects.all()
    stocks = [model_to_dict(stock) for stock in stocks_queryset]
    return JsonResponse(stocks, safe=False)


class AlertStockView(View):

    def get(self, request, *args, **kwargs):
        alerts_queryset = AlertUserStocks\
        .objects\
        .select_related('id_stock')\
        .filter(id_user=1)
        alerts = []
        for alert_queryset in alerts_queryset:
            alert_stock = model_to_dict(alert_queryset, fields=["price_alert", "type"])
            alert_stock['code'] = model_to_dict(alert_queryset.id_stock, fields=['code'])['code']
            alerts.append(alert_stock)
        return JsonResponse(alerts, safe=False)

    def post(self, request, *args, **kwargs):
        print(json.loads(request.body))
        print('done')
        alert = AlertUserStocks.create_alert(**json.loads(request.body))
        alert.save()
        return JsonResponse(model_to_dict(alert), safe=False)
