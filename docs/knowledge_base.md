# Tài liệu Cơ sở Tri thức (Knowledge Base)

## 1. Tổng quan

Tài liệu này mô tả **cơ sở tri thức (Knowledge Base)** được sử dụng trong hệ thống **SGU Student Chatbot áp dụng mô hình RAG (Retrieval-Augmented Generation)**.

Cơ sở tri thức được xây dựng từ **Sổ tay sinh viên của Trường Đại học Sài Gòn**. Nội dung của tài liệu được xử lý và chia nhỏ thành các **chunk dữ liệu** nhằm giúp hệ thống chatbot có thể truy xuất và tìm kiếm thông tin một cách hiệu quả.

Hệ thống RAG sử dụng cơ chế **truy xuất thông tin từ cơ sở tri thức trước khi sinh câu trả lời**, nhờ đó chatbot có thể cung cấp thông tin chính xác dựa trên dữ liệu chính thức của nhà trường.

---

## 2. Nguồn dữ liệu

Cơ sở tri thức của hệ thống được xây dựng từ tài liệu sau:

- **Tên tài liệu:** `so_tay_sv.pdf`
- **Loại tài liệu:** Sổ tay sinh viên Trường Đại học Sài Gòn
- **Ngôn ngữ:** Tiếng Việt

Tài liệu này chứa các thông tin quan trọng dành cho sinh viên, bao gồm:

- Giới thiệu về Trường Đại học Sài Gòn
- Thông tin về các phòng ban và đơn vị chức năng
- Các thủ tục hành chính dành cho sinh viên
- Quy định học vụ
- Thông tin học phí và hỗ trợ tài chính
- Các dịch vụ dành cho sinh viên
- Các câu hỏi thường gặp (FAQ)

Nội dung của tài liệu được sử dụng làm **nguồn tri thức chính cho hệ thống chatbot**.

---

## 3. Mục đích của cơ sở tri thức

Cơ sở tri thức được xây dựng nhằm phục vụ các mục tiêu sau:

### 3.1 Hỗ trợ truy xuất thông tin

Sinh viên có thể đặt câu hỏi liên quan đến các vấn đề học tập hoặc thủ tục hành chính, hệ thống chatbot sẽ tìm kiếm thông tin phù hợp trong cơ sở tri thức để trả lời.

### 3.2 Cung cấp ngữ cảnh cho mô hình ngôn ngữ

Các đoạn thông tin được truy xuất từ cơ sở tri thức sẽ được đưa vào mô hình ngôn ngữ để làm ngữ cảnh khi tạo câu trả lời.

### 3.3 Tăng độ chính xác của chatbot

Nhờ sử dụng dữ liệu từ tài liệu chính thức của nhà trường, chatbot có thể cung cấp các câu trả lời đáng tin cậy và đúng với quy định.

### 3.4 Tối ưu khả năng tìm kiếm

Việc chia tài liệu lớn thành nhiều đoạn nhỏ giúp hệ thống dễ dàng tìm kiếm và truy xuất thông tin phù hợp hơn.

---

## 4. Cấu trúc dữ liệu Chunk

Toàn bộ dữ liệu của cơ sở tri thức được lưu trong file:
