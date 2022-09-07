from django.contrib import admin

from enroll.models import Student

# Register your models here.

#Model Class

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stid', 'stname', 'stemail')

admin.site.register(Student, StudentAdmin)