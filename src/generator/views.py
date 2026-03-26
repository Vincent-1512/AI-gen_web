from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from google import genai # Sử dụng thư viện mới

# Khởi tạo client thay vì dùng genai.configure()
client = genai.Client(api_key="AIzaSyAY13AkicMDx0B-QCvmxXYOu5bgTCpZMo4")

@login_required 
def index(request):
    generated_html = ""
    topic = ""
    
    if request.method == "POST":
        topic = request.POST.get('topic')
        
        prompt = f"""
        Bạn là một chuyên gia lập trình Web. Hãy viết một trang web hoàn chỉnh bằng HTML/CSS/JS (gom chung vào 1 file) cho chủ đề: '{topic}'.
        Yêu cầu BẮT BUỘC phải có trên trang web này:
        1. Một Form đăng nhập (gồm Username và Password).
        2. Các chức năng và giao diện mô phỏng đúng chủ đề được yêu cầu (Ví dụ: Nếu chủ đề là Đặt vé máy bay, phải có form tìm chuyến bay và kiểm tra thông tin giá vé).
        3. Giao diện đẹp, hiện đại, sử dụng Bootstrap 5 qua CDN.
        Chỉ trả về toàn bộ mã code HTML, KHÔNG CẦN GIẢI THÍCH, không thêm markdown (```html).
        """
        
        try:
            # Cú pháp gọi AI của thư viện mới
            response = client.models.generate_content(
                model='gemini-2.5-flash', # Model tốc độ cao
                contents=prompt,
            )
            generated_html = response.text.replace("```html", "").replace("```", "").strip()
        except Exception as e:
            generated_html = f"<div class='alert alert-danger'>Lỗi kết nối AI: {str(e)}</div>"

    return render(request, 'generator/index.html', {
        'generated_html': generated_html,
        'topic': topic
    })