from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.user_id[:10]

class GlucoseTableLvels(models.Model):
    device = models.CharField(max_length=40)
    serial_number = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="glucose_history")
    device_time_stamp = models.DateTimeField()
    record_type = models.IntegerField(default=0)
    glucose_history = models.IntegerField(null=True,blank=True)
    glucose_scan = models.IntegerField(null=True,blank=True)
    non_numeric_rapid_acting_insulin = models.TextField(null=True,blank=True)
    rapid_acting_insulin = models.FloatField(null=True,blank=True)
    food_data = models.TextField(null=True,blank=True)
    carbohydrates = models.IntegerField(null=True,blank=True)
    carbohydrates_servings = models.TextField(null=True,blank=True)
    non_numeric_extended_release_insulin = models.TextField(null=True,blank=True)
    extended_release_insulin=models.FloatField(null=True,blank=True)
    notes = models.TextField(blank=True,null=True)
    glucose_test_strip = models.IntegerField(blank=True,null=True)
    ketone = models.FloatField(blank=True,null=True)
    mealtime_insuline = models.FloatField(null=True,blank=True)
    correction_insuline = models.FloatField(null=True,blank=True)
    user_change_insulin = models.FloatField(null=True,blank=True)