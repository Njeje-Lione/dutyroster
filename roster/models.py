from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DEPARTMENT = (
    ('radiology','radiology'),
    ('neurology','neurology'),
    ('emergency','emergency'),
    ('cardiology','cardiology'),
    ('gynaecology','gynaecology'),
)
SHIFTS=(
    ('nightshift','nightshift'),
    ('dayshift','dayshift'),
)

class Duty(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=50, choices=DEPARTMENT)
    hours = models.PositiveBigIntegerField()
    shift = models.CharField(max_length=30, choices=SHIFTS)

    class Meta:
        verbose_name_plural = 'Duty'

    def __str__(self):
        return f'{self.name}-{self.department}'

class Order(models.Model):
    product = models.ForeignKey(Duty, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateField(auto_now_add = True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product}'
