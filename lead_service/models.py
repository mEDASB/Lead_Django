from django.db import models

# Create your models here.


class Lead(models.Model):
    class status(models.TextChoices):
        NEW = 'new', 'New'
        CONTACTED = 'contacted', 'Contacted'
        QUALIFIED = 'qualified', 'Qualified'
        UNQUALIFIED = 'unqualified', 'Unqualified'
    Status = models.CharField(
        max_length=20,
        choices=status.choices,
        default=status.NEW,
        verbose_name="Lead Status",
        help_text="Select the status of the lead"
    )
    name = models.CharField(max_length=255, verbose_name="Full Name", help_text="Enter your full name")
    email = models.EmailField(verbose_name="Email Address", help_text="Enter your email address")
    phone = models.CharField(max_length=20, verbose_name="Phone Number", help_text="Enter your phone number")
    Source = models.CharField(max_length=255, verbose_name="Lead Source", help_text="Enter the source of the lead")
    note = models.TextField( null=True, blank=True, verbose_name="Notes", help_text="Enter any additional notes about the lead")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


