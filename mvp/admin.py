from django.contrib import admin
from .models import User, Student, Teacher, Clase, Disponible, Payment


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Clase)
admin.site.register(Disponible)
admin.site.register(Payment)