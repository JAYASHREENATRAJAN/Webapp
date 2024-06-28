from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class CustomUser(AbstractUser):
    
    USER_TYPE_CHOICES = (
        ('intern', 'Intern'),
        ('employer', 'Employer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES,default='intern')
    
    

    def __str__(self):
        return self.username

class InternProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.DateField(null=True)
    additional_email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15,null=True)
    street_address = models.CharField(max_length=255,null=True)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    zip_code = models.CharField(max_length=10,null=True)
    marital_status = models.CharField(max_length=10,default='single')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(null=True)
    experience = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    # Add fields for intern profile
class EducationalBackground(models.Model):
    profile = models.ForeignKey(InternProfile, related_name='educational_background', on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    year_passout = models.CharField(max_length=4)
    course = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.institution} - {self.profile.user.username}"
    
class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255,blank=True)
    company_description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)  # Optional location
    website = models.URLField(blank=True)  # Optional website
    # Add fields for employer profile
    additional_email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255, blank=True,)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s Profile"

from datetime import date
class Internship(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.CharField(max_length=255)
    role_required = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    start_date = models.DateField(default=date.today, null=True)
    end_date = models.DateField(default=date.today, null=True)
    skills_preferred = models.CharField(max_length=255)
    apply_before = models.DateField(default=date.today, null=True)
    internship_country = models.CharField(max_length=255,default='INDIA')
    internship_state = models.CharField(max_length=255, null=True)
    internship_area = models.CharField(max_length=255, null=True)
    stipend = models.CharField(max_length=255,)
    date_posted = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)
    internship_opportunity = models.ForeignKey(Internship, on_delete=models.CASCADE,default=None,)
    resume = models.FileField(upload_to='resumes/',null=True)
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.internship_opportunity.title} - {self.status}"
    


from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid

class EmailVerificationToken(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(hours=24)  # Token expires in 24 hours
        super().save(*args, **kwargs)

    def __str__(self):
        return f"EmailVerificationToken(user={self.user}, token={self.token})"

        