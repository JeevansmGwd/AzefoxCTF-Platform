from django.shortcuts import render

def index_view(request):
    # Logic for the home page
    return render(request, 'dashboard/index.html')

def about_us_view(request):
    # Logic for the about us page
    return render(request, 'dashboard/about.html')

def contact_us_view(request):
    # Logic for the contact us page
    return render(request, 'dashboard/contact.html')

def challenge_view(request):
    # Logic for the challenges page
    return render(request, 'challenges/challenges.html')

def search_results_view(request):
    # Logic for handling search results can be removed or simplified
    return render(request, 'search_results.html')  # Adjust as necessary

def sign_up_view(request):
    # Logic for user sign-up
    return render(request, 'sign-up/sign-up.html')

def sign_in_view(request):
    # Logic for user sign-in
    return render(request, 'sign-in/sign-in.html')
