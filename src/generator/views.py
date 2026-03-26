from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
import google.genai as genai

from .models import GeneratedWebsite

# Configure the Gemini API client safely using the key from settings
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
except AttributeError:
    # Handle the case where the API key is not set
    # In a real app, you might want to log this or show a more specific error page
    pass

@login_required
def generator_view(request):
    """
    View to handle topic submission, AI content generation,
    and displaying the results.
    """
    # Lấy tất cả các website đã tạo bởi người dùng hiện tại
    past_websites = GeneratedWebsite.objects.filter(user=request.user)
    
    # Website mới nhất sẽ được hiển thị trong iframe
    latest_website = past_websites.first()

    if request.method == "POST":
        topic = request.POST.get('topic', '').strip()
        
        if topic:
            # Prompt để Gemini tạo nội dung HTML
            prompt = f"""
            As an expert web designer, create a single-file HTML page for the topic: "{topic}".
            Requirements:
            1. Use Bootstrap 5 for a modern look (via CDN).
            2. Include a placeholder login form (Username/Password fields and a button).
            3. Personalize the page by including a welcome message: "Welcome, {request.user.username}!".
            4. The entire output must be a single block of HTML code. Do not include markdown like ```html.
            """
            
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                ai_content = response.text
                
                # Lưu kết quả vào database
                GeneratedWebsite.objects.create(
                    user=request.user,
                    topic=topic,
                    generated_content=ai_content
                )
                
                # Redirect để làm mới trang và hiển thị kết quả
                return redirect('generator_view')

            except Exception as e:
                # Handle API errors gracefully
                # For now, we just print, but in production, you'd log this
                print(f"Error calling Gemini API: {e}")
                # You could add a message to the user here via Django's messages framework
                pass

    context = {
        'past_websites': past_websites,
        'latest_website': latest_website,
    }
    return render(request, 'generator/generator_page.html', context)

@login_required
def website_content_view(request, pk):
    """
    A view to safely serve the raw HTML content of a generated website.
    This is used as the 'src' for the iframe.
    """
    try:
        website = GeneratedWebsite.objects.get(pk=pk, user=request.user)
        return render(request, 'generator/website_content.html', {'content': website.generated_content})
    except GeneratedWebsite.DoesNotExist:
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound("Website not found or you don't have permission to view it.")
