from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BlogPost, BusinessInquiry, ContactInquiry, Category, Tag
from .forms import BlogPostForm, BusinessInquiryForm, ContactInquiryForm
from .serializers import (
    BlogPostSerializer, BusinessInquirySerializer, ContactInquirySerializer,
    CategorySerializer, TagSerializer
)
import logging

logger = logging.getLogger(__name__)

def home(request):
    latest_posts = BlogPost.objects.filter(status='published').order_by('-publication_date')[:3]
    return render(request, 'core/home.html', {'latest_posts': latest_posts})

def about(request):
    return render(request, 'core/about.html')

def business(request):
    if request.method == 'POST':
        form = BusinessInquiryForm(request.POST, request.FILES)
        if form.is_valid():
            inquiry = form.save()
            try:
                # Attempt to send email
                send_mail(
                    'New Business Inquiry',
                    f'New business inquiry from {inquiry.name} ({inquiry.email})\n\nMessage: {inquiry.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                logger.error(f"Failed to send email notification: {str(e)}")
                # Continue with the success response as the inquiry was saved
            
            return JsonResponse({
                'status': 'success',
                'message': 'Your inquiry has been submitted successfully.'
            })
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })
    else:
        form = BusinessInquiryForm()
    return render(request, 'core/business.html', {'form': form})

def blog(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    posts = BlogPost.objects.filter(status='published').order_by('-publication_date')
    
    category_slug = request.GET.get('category')
    tag_slug = request.GET.get('tag')
    
    if category_slug:
        posts = posts.filter(categories__slug=category_slug)
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)
        
    return render(request, 'core/blog.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags
    })

def contact(request):
    if request.method == 'POST':
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            try:
                # Attempt to send email
                send_mail(
                    'New Contact Form Submission',
                    f'New contact form submission from {inquiry.name} ({inquiry.email})\n\nMessage: {inquiry.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                logger.error(f"Failed to send email notification: {str(e)}")
                # Continue with the success response as the inquiry was saved
            
            return JsonResponse({
                'status': 'success',
                'message': 'Your message has been sent successfully.'
            })
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })
    else:
        form = ContactInquiryForm()
    return render(request, 'core/contact.html', {'form': form})

# API ViewSets
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False)
    def published(self, request):
        published = BlogPost.objects.filter(status='published')
        serializer = self.get_serializer(published, many=True)
        return Response(serializer.data)

class BusinessInquiryViewSet(viewsets.ModelViewSet):
    queryset = BusinessInquiry.objects.all()
    serializer_class = BusinessInquirySerializer
    permission_classes = [permissions.IsAuthenticated]

class ContactInquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)

def custom_500(request):
    return render(request, 'core/500.html', status=500)
