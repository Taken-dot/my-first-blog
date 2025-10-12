from django.contrib import admin
from.models import Post, Profile, Project, Skill, Experience, Education, Achievement

# Register your models here.
admin.site.register(Post)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order', 'created_date')
    list_filter = ('is_featured',)
    list_editable = ('is_featured', 'order')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category',)
    list_editable = ('order',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'is_current')
    list_filter = ('is_current',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'is_current')
    list_filter = ('degree_type', 'is_current')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'achievement_type', 'date')
    list_filter = ('achievement_type',)