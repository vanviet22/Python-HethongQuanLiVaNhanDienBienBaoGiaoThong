I) Mục tiêu 
  - Là tạo ra một ứng dụng có khả năng nhận diện và phân loại các biển báo giao thông dựa trên hình ảnh đầu vào,giúp cải thiện quá trình quản lý giao thông và an toàn trên đường bằng cách tự động nhận diện biển báo. Nhận diện các biển báo một cách dễ dàng và hiệu quả với độ chính xác cao, giúp người dân biết và tránh được các vi phạm giao thông liên quan đến các biển báo giao thông.
II) Dự án
  - Dữ liệu được thu thập trên mạng với tổng cộng 173 biển báo khác nhau của việt nam ta.
  - Có sử dụng MySql để lưu trữ thông tin của 173 biển báo này để quản lí.
  - Về giao diện có trang chủ, quản lí biển báo cấm, biển báo hiệu lệnh, biển báo phụ, biển báo nguy hiểm, biển báo chỉ dẫn với các chức năng thêm sửa xóa. Và cuối cùng là giao diện tra cứu với 2 các thức nhận diện là tải ảnh lên và chụp ảnh.
  - Xây dựng mô hình CNN để huấn luyện nhưng trước khi đưa vào mô hình CNN thì dữ liệu được xoay 8 hướng để mỗi loại biển báo sẽ có được thêm dữ liệu. Độ chính xác đạt được là hơn 90%.
 
