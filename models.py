# main/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


# Create a UserProfile model that extends User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linking to the User model
    profilepic = models.ImageField(upload_to='profile_pics/', default='default.jpg', blank=True, null=True)  # Image field for profile picture
    full_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)  # Example additional field
    date_of_birth = models.DateField(null=True, blank=True)  # Example additional field
    city = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    interests = models.CharField(max_length=100, blank=True, null=True)
    goals = models.CharField(max_length=100, blank=True, null=True)

    # Return the username for the profile
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    # You can define a signal to automatically create or update the UserProfile when a User is created or updated.

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='employer_logos/', default='default.jpg', blank=True, null=True)
    managername = models.CharField(max_length=100)
    compname = models.CharField(max_length=100)
    companytype = models.CharField(max_length=50)
    desc = models.TextField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Employer Profile"

# main/models.py

'''@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Creates a UserProfile for a newly created user."""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Saves the UserProfile when the User is saved."""
    instance.profile.save()'''

# main/models.py

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comment {self.id} - {self.content[:20]}"

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user} on {self.comment}"
    
class EmailVerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=5)
    
class HealthResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concern = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

class JobPost(models.Model):
    jobtitle = models.CharField(max_length=100)
    jobcategory = models.CharField(max_length=50)
    jobtype = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    jobdesc = models.TextField()
    deadline = models.CharField(max_length=50)
    compname = models.CharField(max_length=100)
    companytype = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    description = models.TextField()
    city = models.CharField(max_length=50)
    email = models.EmailField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.jobtitle} at {self.compname}"
    
class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=20)
    profilepic = models.ImageField(upload_to='candidate_profiles/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    city = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    applied_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} applied for {self.job.jobtitle}"
    


