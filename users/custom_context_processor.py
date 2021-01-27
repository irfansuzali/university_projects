from .models import School

def school_renderer(request):
    return {
        'schools': School.objects.all()
    }