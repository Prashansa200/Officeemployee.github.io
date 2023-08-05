from django.db import models

# class log_In(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     class Meta:
#         db_table = 'Hotel'
#         managed = True
#         verbose_name = 'ModelName'
#         verbose_name_plural = 'ModelNames'

        
# class log_In(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     class Meta:
#         db_table = 'Hotel'
#         managed = True
        
#         verbose_name = 'ModelName'
#         verbose_name_plural = 'ModelNames'


class Bookings(models.Model):
    guest_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    id_proof = models.FileField(upload_to='id_proofs/')
