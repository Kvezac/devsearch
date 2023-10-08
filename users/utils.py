from .models import Profile, Skill
from django.db.models import Q


def search_profiles(request):
    search_query = request.GET.get('search_query') if request.GET.get('search_query') else ''
    skills = Skill.objects.filter(name__iexact=search_query)
    profs = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                              Q(short_info__icontains=search_query) |
                                              Q(skill__in=skills))
    return profs, search_query
