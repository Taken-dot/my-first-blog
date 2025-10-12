from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    #is_deleted = models.BooleanField(default=False) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    #soft delete
    # def delete(self):
    #  self.is_deleted=True #when post is deleted, it just flag as deleted but passing true
    # self .save(

class Profile(models.Model):
    #basic info
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()

    #Contacts
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100)  # You'll type "Preston, UK"
    

    #Socials Links
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name or "Profile"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
                 
class Project(models.Model):

    #Basic info
    title = models.CharField(max_length=200)
    description= models.TextField()

    #Tech Stack (what you built it with)
    technologies = models.CharField(max_length=300, help_text= "e.g., Django, Python, HTML/CSS")

    #Links
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True, help_text = "Live demo link if available")
      
    #Image
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Project screenshot")
    
    # Display options
    is_featured = models.BooleanField(default=False, help_text="Show on homepage?")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers show first)") #  Control which project shows first (order=1), second (order=2), etc.
    
    # Dates
    created_date = models.DateField(help_text="When you built this")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['order', '-created_date']  # Sort by order, then newest first

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework/Library'),
        ('database', 'Database'),
        ('tool', 'Tool'),
        ('soft', 'Soft Skill'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=50, help_text="0-100 skill level")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
    class Meta:
        ordering = ['category', 'order']

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave empty if current job")
    description = models.TextField(help_text="What you did at this job")
    is_current = models.BooleanField(default=False, help_text="Currently working here?")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']  # Newest job first
        verbose_name_plural = "Experiences"

class Education(models.Model):

    DEGREE_CHOICES = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
        ('diploma', 'Diploma'),
        ('highschool', 'High School'),
        ('other', 'Other'),
    ]
    
    degree = models.CharField(max_length=200, help_text="e.g., BSc Computer Science")
    institution = models.CharField(max_length=200, help_text="University/School name")
    location = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave empty if ongoing")
    gpa = models.CharField(max_length=20, blank=True, help_text="e.g., 3.09/4.00")
    description = models.TextField(blank=True, help_text="Key modules, achievements")
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
    class Meta:
        ordering = ['-start_date']  # Most recent first
        verbose_name_plural = "Education"

class Achievement(models.Model):
    ACHIEVEMENT_TYPE_CHOICES = [
        ('award', 'Award'),
        ('certification', 'Certification'),
        ('competition', 'Competition'),
        ('recognition', 'Recognition'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, help_text="Who gave this achievement")
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPE_CHOICES)
    date = models.DateField(help_text="When you received it")
    description = models.TextField(blank=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']  # Most recent first