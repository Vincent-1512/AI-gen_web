from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from google import genai
import os
from .models import GeneratedWebsite
from django.shortcuts import redirect

# SỬA LỖI 1: Gán trực tiếp API key nếu bạn chưa cấu hình file .env
# Tuy nhiên, hãy nhớ xóa nó đi hoặc dùng .env trước khi push lên GitHub nhé!
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

@login_required 
def index(request):
    history = GeneratedWebsite.objects.filter(user=request.user).order_by('-created_at')
    generated_html = ""
    topic = ""
    
    website_id = request.GET.get('id')
    if website_id:
        old_website = get_object_or_404(GeneratedWebsite, id=website_id, user=request.user)
        # SỬA LỖI 2.1: Đổi html_content thành generated_content
        generated_html = old_website.generated_content
        topic = old_website.topic
    
    if request.method == "POST":
        topic = request.POST.get('topic')
        
        prompt = f"""
        Bạn là một chuyên gia lập trình Web. Hãy viết một trang web hoàn chỉnh bằng HTML/CSS/JS (gom chung vào 1 file) cho chủ đề: '{topic}'.
        Yêu cầu BẮT BUỘC phải có trên trang web này:
        1. Một Form đăng nhập (gồm Username và Password).
        2. Các chức năng và giao diện mô phỏng đúng chủ đề được yêu cầu.
        3. Giao diện đẹp, hiện đại, sử dụng Bootstrap 5 qua CDN.
        Chỉ trả về toàn bộ mã code HTML, KHÔNG CẦN GIẢI THÍCH, không thêm markdown (```html).
        """
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            generated_html = response.text.replace("```html", "").replace("```", "").strip()
            
            # SỬA LỖI 2.2: Đổi html_content thành generated_content
            GeneratedWebsite.objects.create(
                user=request.user,
                topic=topic,
                generated_content=generated_html
            )
            
        except Exception as e:
            generated_html = f"<div class='alert alert-danger'>Lỗi kết nối AI: {str(e)}</div>"

    return render(request, 'generator/index.html', {
        'generated_html': generated_html,
        'topic': topic,
        'history': history
    })

@login_required
def dispatch_login(request):
    """
    Hàm điều hướng dựa trên quyền hạn (Role)
    """
    if request.user.is_superuser:
        # Nếu là Admin tối cao (như tài khoản Vincent), cho vào trang quản trị luôn
        return redirect('/admin/')
    else:
        # Nếu là Staff hoặc User bình thường, cho ra trang chủ Viewsite luôn
        return redirect('/')