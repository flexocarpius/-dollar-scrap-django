from django.db import models

# Create your models here.
class Entry(models.Model):
    date = models.DateTimeField()
    buy_price = models.FloatField()
    sell_price = models.FloatField()

    def to_dict(self):
        return {
            'id': self.pk,
            'date': self.date,
            'buy_price': self.buy_price,
            'sell_price': self.sell_price
        }

    def __repr__(self):
        return '[{0}] {1} - buy: {2}, sell {3}'.format(self.pk, self.date, self.buy_price, self.sell_price)
        
    class Meta:
        db_table = 'entries'