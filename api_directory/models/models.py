from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.functions import Cast
from django.db.models import IntegerField





class Customer(models.Model):
    customer_id = models.CharField(max_length=10, primary_key=True)
    age = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(18)])
    gender = models.IntegerField(max_length=20, blank=False, null=False)
    income = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])


    class Meta:
        """
        note it is very important to modify the default nanme of this database
        because of the already existing db and data in it
        """
        db_table = "customers"

    def save(self, *args, **kwargs):
        """
        overriding the save method to b/c i want to auto increament the customer_id
        """
        if not self.customer_id:
            print(Customer.objects.all().count())
            self.customer_id = str(int(Customer.objects.annotate(customer_id_int=Cast('customer_id', IntegerField())).order_by('customer_id_int').last().customer_id )+ 1)
        super().save(*args, **kwargs)




class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)

    VISIT_FREQUENCY_CHOICES = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Rarely", "Rarely"),
    ]
    visit_frequency = models.CharField(max_length=20, choices=VISIT_FREQUENCY_CHOICES)

    average_spend = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    preferred_cuisine = models.CharField(max_length=50)
    wait_time = models.IntegerField(validators=[MinValueValidator(0)])

    service_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    food_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ambiance_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        db_table = "visits"



class Satisfaction(models.Model):
    satisfaction_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    visit = models.ForeignKey("Visit", on_delete=models.CASCADE)

    satisfaction = models.BooleanField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "satisfaction"