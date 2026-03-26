# 🚀 AI Web Builder - Đồ án Tích hợp AI tạo Website
**Sinh viên thực hiện:** Huỳnh Tiến Đạt (Vincent)

## 📌 Giới thiệu
Ứng dụng web cho phép người dùng nhập một chủ đề bất kỳ, hệ thống sẽ gọi API của AI để tự động sinh ra mã nguồn HTML/CSS (có tích hợp Form đăng nhập và Bootstrap 5). 
Hệ thống được thiết kế chạy hoàn toàn trên môi trường **Docker**, sử dụng framework **Django** và cơ sở dữ liệu **SQLite**.

## ⚙️ Yêu cầu hệ thống
- Máy tính đã cài đặt **Docker** và **Docker Compose**.

## 🚀 Hướng dẫn chạy dự án

**Bước 1: Cấu hình API Key**
- Đổi tên file `.env.example` thành `.env`.
- Mở file `.env` và dán Gemini API Key của thầy vào biến `GEMINI_API_KEY`.

**Bước 2: Khởi chạy hệ thống bằng Docker**
Mở Terminal tại thư mục gốc của dự án và chạy lệnh:
```bash
docker-compose up --build