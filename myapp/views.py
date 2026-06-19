from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Paper, BlogPost, Scholarship, Subscriber

REGION_META = {
    'asia': {'name': 'Asia', 'color': 'amber', 'description': 'Asian countries'},
    'north-america': {'name': 'North America', 'color': 'sky', 'description': 'the USA and Canada'},
    'south-america': {'name': 'South America', 'color': 'green', 'description': 'South American countries'},
    'europe': {'name': 'Europe', 'color': 'purple', 'description': 'European countries'},
}

def index(request):
    latest_scholarships = Scholarship.objects.filter(is_published=True)[:6]
    latest_papers = Paper.objects.filter(is_published=True)[:4]
    regions = []
    for slug, meta in REGION_META.items():
        count = Scholarship.objects.filter(region=slug, is_published=True).count()
        regions.append({**meta, 'slug': slug, 'count': count})
    papers_count = Paper.objects.filter(is_published=True).count()
    scholarships_count = Scholarship.objects.filter(is_published=True).count()
    countries_count = Scholarship.objects.filter(is_published=True).values('country').distinct().count()
    students_helped = scholarships_count * 100 + papers_count * 50
    return render(request, 'index.html', {
        'nav_active': 'home',
        'latest_scholarships': latest_scholarships,
        'latest_papers': latest_papers,
        'regions': regions,
        'papers_count': papers_count,
        'scholarships_count': scholarships_count,
        'countries_count': countries_count,
        'students_helped': students_helped,
    })


def paper_list(request, category=None):
    if category is None:
        category = request.GET.get('category')
    qs = Paper.objects.filter(is_published=True)
    if category:
        qs = qs.filter(category=category)
    papers = Paginator(qs, 12)
    page_number = request.GET.get('page')
    page_obj = papers.get_page(page_number)
    return render(request, 'edu-papers-list.html', {
        'nav_active': 'papers',
        'page_obj': page_obj,
        'current_category': category,
    })


def paper_detail(request, slug):
    paper = get_object_or_404(Paper, slug=slug, is_published=True)
    return render(request, 'edu-paper-detail.html', {
        'nav_active': 'papers',
        'paper': paper,
    })


def scholarship_list(request, region):
    meta = REGION_META.get(region)
    if not meta:
        raise Http404
    scholarships = Paginator(Scholarship.objects.filter(region=region, is_published=True), 12)
    page_number = request.GET.get('page')
    page_obj = scholarships.get_page(page_number)
    return render(request, 'scholarship-list.html', {
        'nav_active': meta['name'].lower().replace(' ', '-'),
        'region_slug': region,
        'region_name': meta['name'],
        'region_color': meta['color'],
        'region_description': meta['description'],
        'page_obj': page_obj,
    })


def scholarship_country(request, region, country):
    meta = REGION_META.get(region)
    if not meta:
        raise Http404
    country_name = country.replace('-', ' ').title()
    scholarships = Paginator(Scholarship.objects.filter(region=region, country__iexact=country_name, is_published=True), 12)
    page_number = request.GET.get('page')
    page_obj = scholarships.get_page(page_number)
    return render(request, 'scholarship-country.html', {
        'nav_active': country,
        'region_slug': region,
        'region_name': meta['name'],
        'region_color': meta['color'],
        'country_name': country_name,
        'page_obj': page_obj,
    })


def scholarship_detail(request, region, country, slug):
    meta = REGION_META.get(region)
    if not meta:
        raise Http404
    scholarship = get_object_or_404(Scholarship, slug=slug, region=region, is_published=True)
    return render(request, 'scholarship-detail.html', {
        'nav_active': meta['name'].lower().replace(' ', '-'),
        'region_slug': region,
        'region_name': meta['name'],
        'region_color': meta['color'],
        'country_name': scholarship.country,
        'scholarship': scholarship,
    })


def blog(request):
    posts = Paginator(BlogPost.objects.filter(is_published=True), 12)
    page_number = request.GET.get('page')
    page_obj = posts.get_page(page_number)
    return render(request, 'blog.html', {
        'nav_active': 'blog',
        'page_obj': page_obj,
    })


def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related = BlogPost.objects.filter(is_published=True, category=post.category).exclude(id=post.id)[:3]
    return render(request, 'blog-single.html', {
        'nav_active': 'blog',
        'post': post,
        'related': related,
    })


def all_scholarships(request):
    scholarships = Paginator(Scholarship.objects.filter(is_published=True), 12)
    page_number = request.GET.get('page')
    page_obj = scholarships.get_page(page_number)
    return render(request, 'scholarship-all.html', {
        'nav_active': 'scholarship',
        'page_obj': page_obj,
    })


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            _, created = Subscriber.objects.get_or_create(email=email, defaults={'is_active': True})
            if created:
                messages.success(request, 'You have been subscribed successfully!')
            else:
                messages.info(request, 'This email is already subscribed.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect('index')


def about(request):
    return render(request, 'about.html', {'nav_active': 'about'})


def contact(request):
    return render(request, 'contact.html', {'nav_active': 'contact'})


def privacy_policy(request):
    return render(request, 'privacy-policy.html', {'nav_active': 'privacy'})


def terms_conditions(request):
    return render(request, 'terms-conditions.html', {'nav_active': 'terms'})
