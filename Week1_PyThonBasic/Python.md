     PyThon

  Variable
     -Có phân biệt chữ hoa chữ thường
     -bắt đầu bằng chữ
     -có thể gán giá trị trên một dòng
     -Có thể gán một giá trí bằng nhiều biến
     -Biến toàn cục

  Data struct

     List:
       -Lưu trữ nhiều giá trị trong một biến
       -Chứa được nhiều kiểu dữ liệu trong mảng
       -Có thể chèn, thêm, xóa
       -list có thể thay đổi phần tử bằng index
      Tuples:
      -Được sắp xếp theo thứ tự và không thể thay đổi
      -Giống list nhưng không thể thay đổi thêm sửa xóa, chỉ có thể xóa tuples
      -tốc độ truy xuaats nhanh hơn list và chiếm ít bộ nhớ hơn list
     Dictionaries
      -Lưu theo kiểu key:value
      -Sắp xếp theo thứ tự,có thể thay đổi và không trùng lặp(key)
      -Dùng các key để phân biệt
     Vòng lặp
       For, While,Do While

  Function

    def myfuncition()
     -Số lượng đối số không xác định :def myfuncition(*a) và a[i] là đối số nếu muốn dùng,
     -Tham số default phải ở cuối,nếu truyền thiếu tham số sẽ lấu default :def funcition(name,age=1)
     -Đối số từ khóa:myfuncition(key=value,,)->thứ tự đối số không quan trọng
     -Đối số từ khóa tùy ý:def myfuncition(**a) và a["key"] là đối số nếu muốn dùng
     -có thể return về nhiều giá trị

  Class

     -class không cần thân hàm vẫn có thể gán được thuộc tính
     -hàm khởi tạo init(self):"chỉ có một hàm khởi tạo duy nhất(khác với các nn khác)",self đại diện cho bản thân đối tượng được tạo ra
     -Thường được dùng để tạo đối tượng,xử lý trước các thông tin đưa vào trước khi tạo ra một đối tượng
     -Kế thừa :class nameclass(class) :kế thừa các thuộc tính và phương thức của lớp cha(kể cả contructor)
     -có thể viết lại các thuộc tính và phương thức của lớp cha(supper...)

  Module

      -Module là các mã thư viện Python ,và có thể tái sử dụng.
      -Import module:import modulemodule as ...
      -liệt kê tất cả tên hàm,biến :dir(modulename)
      -nhập một bộ phân trong module: from modulename import ...

  Pip

      -quản lý gói ,module
      -py -m pip install --upgrade pip;cập nhật,(-m)
      -pip help
      -pip install +tên gói(==: để chỉ định gói cài đặt): cài đặt gói
      -pip list : liệt kê các gói
      -pip freeze > requirements.txt :ghi danh sách các gói cài đặt vào file
      -pip install -r requirements.txt :cài đặt ,sao chép môi trường(cài các gói,thư viện trong file chỉ định),các phiên bản cũng sẽ khớp với các phiên bản trong file
      -pip install --upgrade -r requirements.txt :cập nhật các phiên bản mới nhất với các gói trong file
      -pip uninstall :gỡ bỏ gói  

  Convention
      -4x khoảng trắng
      -chiều dài tối đa
      -ngắt dòng trước các toán tử ,toán hạng(nếu dòng dài muốn ngắt)
      -Dòng trống: cách 1-2 dòng với các phương thức,class ,khối code
      -import lên đặt trên mỗi dòng riêng biệt
      -thư viện chuẩn->của nhà cung cấp thứ ba->cục bộ
      -tên biến bắt đầu bằng hai dấu __ trong module
      -dùng khoảng trắng sau các dấu ",",":",";" cho dễ nhìn
      -Quy tắc đặt tên:
      -Phân biệt chữ hoa chữ thường
      -dùng _để ngăn cách
      -tên biến,funcition chữ thường,tên hằng chữ hoa
      -tên package,module:lên viết thường ,ngắn gọn(dùng _nếu có nhiều từ),khác các module có sẵn
      -các class được viết hoa chữ cái đầu mỗi từ:ClassName
      -đặt tên với attribute/function trong class:
      -Mặc định, các attribute/function của một lớp được khai báo là public
      -protected , đặt 01 ký tự _ ở đầu tiên: _protected_attribute_name
      -private, đặt 02 ký tự _ ở đầu tiên: __private_attribute_name

   Virtualenv
      -Mỗi trường ảo
      -Cách dùng:
        +python3 -m venv env
        +source env/bin/activate  # On Windows use `env\Scripts\activate`
        +pip install django
        

