# 🚀 Đồ án: AI Web Builder (Hệ thống tạo Website tự động bằng AI)
**Sinh viên thực hiện:** Huỳnh Tiến Đạt-N23DCDK011 (Vincent)

## 📌 Giới thiệu
Hệ thống sử dụng Gemini API để sinh mã nguồn HTML/CSS/JS tự động dựa trên prompt của người dùng. Dự án được triển khai toàn diện trên môi trường Docker với Django framework. Hệ thống có phân quyền Admin và Staff riêng biệt.

## ⚙️ Yêu cầu hệ thống
- Máy tính đã cài đặt **Docker** và **Docker Compose**.

## 🚀 Hướng dẫn chạy dự án

**Bước 1: Cấu hình biến môi trường**
- Đổi tên file `.env.example` thành `.env`.
- Điền API Key Gemini của you vào biến `GEMINI_API_KEY` trong file `.env`.

**Bước 2: Khởi chạy bằng Docker**
Mở Terminal tại thư mục gốc của dự án và chạy lệnh:
`docker-compose up --build`

**Bước 3: Trải nghiệm hệ thống**
Truy cập vào trình duyệt: `http://localhost:8000/`

**Tài khoản Test có sẵn:**
1. Tài khoản Superuser (Truy cập được trang Quản trị `/admin/`):
   - Username: `vincent`
   - Password: `[123]`
2. Tài khoản Staff (Chỉ dùng chức năng AI):
   - Username: `@admin`
   - Password: `[@Admin123456789]`
3. Tạo tài khoản để sử dụng chức năng AI.