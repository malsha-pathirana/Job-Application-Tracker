from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    ]

    company_name = models.CharField(max_length=200)
    job_position = models.CharField(max_length=200)
    job_url = models.URLField(blank=True,null=True)
    applied_date = models.DateField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Applied')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_position} at {self.company_name}"
