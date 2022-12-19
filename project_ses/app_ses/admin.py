from django.contrib import admin
from .models import AppUser, Student, Course

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ("full_name", "email", "password", "usertype", "contact")
    search_fields = ("full_name", "email",)
    list_filter = ("full_name", "email",)

class AdminStudent(admin.ModelAdmin):
    list_display =  ("first_name", "middle_name", "last_name", "email", \
            "contact", "gender", "blood_group", "academic_level", \
            "academic_status", "academic_org", "academic_score",\
            "course", "intake", "shift", "remarks")
    search_fields = ("first_name", "contact", "course",)
    list_filter =  ("first_name", "contact", "course",)



admin.site.register(AppUser)
admin.site.register(Course)
admin.site.register(Student)
