from django.db import models

# Create your models here.
class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = "stock"


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = "user"


class AlertUserStocks(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="id_user")
    id_stock = models.ForeignKey(Stock, on_delete=models.CASCADE, db_column="id_stock")
    price_alert = models.IntegerField()
    type = models.CharField(max_length=10)
    class Meta:
        db_table = "alert_user_stocks"

    @classmethod
    def create_alert(cls, id_user, id_stock, price_alert, type):
        user = User.objects.get(id=id_user)
        stock = Stock.objects.get(id=id_stock)
        return AlertUserStocks(
            id_user=user,
            id_stock=stock,
            price_alert=price_alert,
            type=type,
        )

class StockRealtimeVW(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10)
    price = models.IntegerField()
    class Meta:
        db_table = "stock_realtime_vw"