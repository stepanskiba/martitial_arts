from django.contrib import admin
from .models import PriceModels, InstructorModels, UserModels, ReviewModels
from .models import TimetableModels, InformationOfInstructorModels
# Register your models here.

admin.site.register(PriceModels)
admin.site.register(InstructorModels)
admin.site.register(UserModels)
admin.site.register(ReviewModels)
admin.site.register(TimetableModels)
admin.site.register(InformationOfInstructorModels)