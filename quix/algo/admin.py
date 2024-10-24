# register the models to the admin site

from django.contrib import admin

from .models import Algorithm
from .models import AlgorithmStep
from .models import PracticeExample

admin.site.register(Algorithm)
admin.site.register(AlgorithmStep)
admin.site.register(PracticeExample)
