from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import About, AboutPage
from .forms import CollaborateForm, AboutPageForm

def about_me(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
            
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form},
    )

@login_required
def create_about_page(request):
    # Check if the user already has an AboutPage
    if AboutPage.objects.filter(user=request.user).exists():
        return redirect('view_about_page', username=request.user.username)
    
    if request.method == 'POST':
        form = AboutPageForm(request.POST)
        if form.is_valid():
            about_page = form.save(commit=False)
            about_page.user = request.user
            about_page.save()
            return redirect('view_about_page', username=request.user.username)
    else:
        form = AboutPageForm()
    return render(request, 'about/create_about_page.html', {'form': form})

@login_required
def view_about_page(request, username):
    user = get_object_or_404(User, username=username)
    try:
        about_page = AboutPage.objects.get(user=user)
    except AboutPage.DoesNotExist:
        messages.error(request, "No About Page found for this user.")
        return redirect('create_about_page')
    return render(request, 'about/view_about_page.html', {'about_page': about_page})

@login_required
def edit_about_page(request):
    about_page = get_object_or_404(AboutPage, user=request.user)
    if request.method == 'POST':
        form = AboutPageForm(request.POST, instance=about_page)
        if form.is_valid():
            form.save()
            return redirect('view_about_page', username=request.user.username)
    else:
        form = AboutPageForm(instance=about_page)
    return render(request, 'about/edit_about_page.html', {'form': form})
