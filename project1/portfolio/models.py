from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    market_cap = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.symbol})"