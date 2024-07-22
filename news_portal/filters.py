from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post

class PostFilter(FilterSet):
    date = DateFilter(field_name='time_in', lookup_expr='gt', widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Post
        fields = {
            'title': ['iregex'],
            'author__user__username': ['iregex'],
        }

