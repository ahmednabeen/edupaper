from .models import Scholarship

REGION_META = {
    'asia': 'Asia',
    'north-america': 'North America',
    'south-america': 'South America',
    'europe': 'Europe',
}

def navbar_regions(request):
    regions = []
    for slug, name in REGION_META.items():
        countries = (
            Scholarship.objects
            .filter(region=slug, is_published=True)
            .values_list('country', flat=True)
            .distinct()
            .order_by('country')
        )
        regions.append({
            'slug': slug,
            'name': name,
            'countries': countries,
        })
    return {'navbar_regions': regions}
