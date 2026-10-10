from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True, db_index=True)
    name = models.CharField(max_length=255, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    market_cap = models.BigIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.name} ({self.ticker})"

class PriceData(models.Model):
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='price_data'
    )
    date = models.DateField(db_index=True)
    open_price = models.DecimalField(max_digits=12, decimal_places=4)
    high = models.DecimalField(max_digits=12, decimal_places=4)
    low = models.DecimalField(max_digits=12, decimal_places=4)
    close = models.DecimalField(max_digits=12, decimal_places=4)
    volume = models.BigIntegerField()
    adj_close = models.DecimalField(
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('stock', 'date')
        ordering = ['-date']

class MomentumScore(models.Model):
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='momentum_scores'
    )
    calculation_date = models.DateField(db_index=True)
    momentum_score = models.DecimalField(max_digits=10, decimal_places=6)
    rank = models.IntegerField(null=True, blank=True)
    quintile = models.IntegerField(null=True, blank=True)
    is_top_quintile = models.BooleanField(default=False)
    period_start = models.DateField()
    period_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('stock', 'date')
        ordering = ['-date']