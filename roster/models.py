from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DEPARTMENT = (
    ('radiology','radiology'),
    ('neurology','neurology'),
    ('emergency','emergency'),
    ('cardiology','cardiology'),
    ('gynecology','gynecology'),
    ('Endocrinology and metabolic Medicine','Endocrinology and metabolic Medicine'),
    ('Outpatient department','Outpatient department'),
    ('Inpatient department','Inpatient department'),
    ('Critical Care','Critical Care'),
    ('Gastroenterology','Gastroenterology'),
    ('Psychiatry','Psychiatry'),
    ('Haematology','Haematology'),
    ('Cardiology','Cardiology'),
)
SHIFTS=(
    ('nightshift','nightshift'),
    ('dayshift','dayshift'),
)
ACTIVITY=(
    ('checkin','checkin'),
    ('checkout','checkout'),
)
COMPLAIN_TYPE=(
    ('sexual harassment','sexual harassment'),
    ('Unfair treatment','Unfair treatment'),
    ('Bullying','Bullying'),
    ('Toxic work relationships','Toxic work relationships'),
    ('Taken advantage of','Taken advantage of'),
    ('other','other')

)

class Ward(models.Model):
    name = models.CharField(max_length=40)
    floor = models.PositiveBigIntegerField()
    department = models.CharField(max_length=40, choices=DEPARTMENT)
    building = models.CharField(max_length=30, null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Ward'

    def __str__(self):
        return f'{self.name} {self.department}'

class Duty(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=50, choices=DEPARTMENT)
    hours = models.PositiveBigIntegerField()
    shift = models.CharField(max_length=30, choices=SHIFTS)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Duty'

    def __str__(self):
        return f'{self.name}-{self.department}'

class Order(models.Model):
    product = models.ForeignKey(Duty, on_delete=models.CASCADE)
    activity = models.CharField(max_length=30, choices=ACTIVITY, default="checkin", null=True, blank=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateField(auto_now_add = True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product}'
    
class Leave(models.Model):
    name = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT,default="neurology")
    email = models.EmailField(default="Empty") 
    class Meta:
        verbose_name_plural = 'Leave'

    def __str__(self):
         return f'{self.name}-{self.time}'
    
class Complains(models.Model): 
     name = models.CharField(max_length=40)
     time = models.DateTimeField(auto_now=False, auto_now_add=True)
     department = models.CharField(max_length=50, choices=DEPARTMENT,default="neurology")
     email = models.EmailField(default="Empty") 
     type = models.CharField(max_length=40, choices=COMPLAIN_TYPE)
     brief_description = models.CharField(max_length=50, null=True, blank=True)



