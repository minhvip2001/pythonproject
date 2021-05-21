Django

---------------------------------------------------------------
-Mô hình MVT(Model-View-Temple)
  
  - Model chứa các mô hình cho cơ sở dữ liệu(mỗi class là một bảng, được kế thừa từ lớp model)
  - View: tương tác với cơ sở dữ liệu và gọi ra template
  - Template: Giao diện để hiện thị cho người dùng thấy
  -> Giống MVC(Model - Model, View - Template, Controller - View)

-Cách tạo project django

  - Tải python phiên bản mới nhất
  - Tải django
  B1: django-admin startproject projectname
    - manage.py: Cho phép bạn tương tác với dự án Django theo các cách khác nhau
    - __init__.py: Nói với trình thông dịch python là thư mục nên được coi là một python package. Tập tin này chủ yếu là trống. 
    - settings.py: Tập tin cấu hình
    - urls.py: Bao gồm tất cả khai báo URL cho dự án Django và mục lục của trang web Django
    - wsgi.py: Đây là lối vào cho các máy chủ web tương thích WSGI để phục vụ các dự án của bạn và deploy với WSGI.
  B2: py manage.py startapp appname
    - admin.py: Thực hiện đăng ký đối tượng ứng dụng (thường là mô hình cơ sở dữ liệu) trên trang admin của django
    - apps.py: Thông tin cấu hình ứng dụng
    - migrations: 1 thư mục dùng để lưu lại các lịch sử thay đổi của database khi chúng ta thực chỉnh sửa
    - models.py: Chứa khai báo các mô hình dữ liệu(models), kiến thức models sẽ được trình bày trong bài sau
    - test.py: Chứa các đoạn code testing của app
    - views.py: Thực hiện chức năng như là 1 Controller trong MVC, nhận các yêu cầu, xử lý yêu cầu lấy data từ database sau đó trả về view(HTML,CSS,JS).
    - urls.py: chứa các UL, điều hướng khi có các Url khác nhau
    - templates: chứa các giao diện để hiện thị dưới dạng HTML, gọi appname/namefile.html
    - static: chứa các file css, js
      + load file css hoặc js ra html: {% load staticfiles %} : static=/appname/static/  

---------------------------------------------------------------

Model
  - Model là j?
    - Thừa kế từ lớp models
    - Mỗi class model nếu không chỉ định trường khóa chính thì tự động sẽ được thêm một trường id(tự động tăng-id = models.AutoField(primary_key=True)),nếu được chỉ định khóa chính sẽ không thêm vào nữa,mỗi class model cần có một trường khóa chính
    - verbose_name : một tên khác của trường,trong các mối quan hệ (1-1,1-n,n-n) phải chỉ định rõ verbose_name="?"(vì đối số đầu tiên liên quan đến mô hình khác tham chiếu đến),không viết hoa chữ cái đầu tiên.
    - Có các kiểu dữ liệu như :
      - Kiểu cột: database sẽ liệu những kiểu này: integer,char,text...
        + CharField:cho các chuỗi có kích thước nhỏ,phải có maxleng->truy xuất nhanh hơn TextField
        + FileField(to_upload,max_length,**option)
        + ForeignKey( to,on_delete,**option):mối quan hệ nhiều-một :to(bảng tham chiếu đến),on_delete() 
          + to:bảng tham chiếu đến,tham chiếu đệ quy đến bản thân ('self'),tham chiếu     đến một mô hình chưa xác định('modelname'), mô hình ở ứng dụng khác: 'appname.modelname' 
          + on_delete:
            + cascade : khi xóa một đối tượng thì đối tượng liên quan chứa ForeignKey đến nó cũng bị xóa theo
            + Protect: ngăn việc xóa đối tượng đượng tham chiếu đến
            + Restrict:   
        + ManyToManyField(to, **options):quan hệ nhiều nhiều    
        + OneToOneField(to,on_delete,parent_link=?,**option): 1-1,là khóa chính của một mô hình khác,có thể truy cập đến các trường của nhau
    - Kiểu widget: khi sử dụng form (class,id :để liên kết với css)
    - class Meta: lưu trữ các thông tin cấu hình về model đó: sắp xếp dữ liệu(ordering),tên bảng(db_table) ...
       thừa kế
    - Thêm dữ liệu : modelname(:,...) : tạo dữ liệu cho modelname nhưng chưa lưu -> save()->create với (n-n) tạo thể hiện -> add   
    - Truy xuất các dữ liệu :
      - modelname.objects.all(): lấy toàn bộ dữ liệu của bảng modelname
      - modelname.objects.get(option): trả về đối tượng duy nhất
    - migrate: áp dụng vào cơ sở dữ liệu, không áp dụng di chuyển.
    - sqlmigrate: hiển thị các câu lệnh SQL để di chuyển.

---------------------------------------------------------------

View

    - Chạy vào đường dẫn được cài đặt trong ROOT_URLCF->urlpatterns[] ->appname.urls...
    - re_path()
    - Regex: *
    - tài khoản admin: + py manage.py createsuperuser
    - cấu hình trong admins:để tùy chọn những dữ liệu được hiển thị trong trang quản trị
      - tạo một class(classA) kế thừa từ lớp admin .ModelAdmin và khai báo một list có tên các thuộc tính muốn hiện trong trang admin :
        - fields = ['?', '?','?']
        - admin.site.register(model,classA)
    - render( request , template_name , context = None , content_type = None , status = None , using = None )
      - request : đối tượng yêu cầu
        - template_name : trang html
        - context : các cặp (key : value) để hiển thị trong te,plate_name
        - contect_type : mặc định là text/html
        - status : mã trạng thái cho phản hồi mặc định là 200
        - using    
    - @require_http_methods( request_method_list ): chỉ chấp nhật các phương thức yêu cầu cụ thể

    - Lấy dữ liệu từ form: cần dùng cleaned_data để lấy dữ liệu được post lên
      - Cần data.is_valid()    
    - Session:
    - lấy giá trị :
      - request.session['name']
      - request.session.get('name','default')
    - Thiết lập: request.session['name'] = 'value'
    - Xóa session:
      del request.session['name']: xóa một session
      request.session.flush() : xóa toàn bộ dữ liệu session
    - Thiết lập thời gian tồn tại : request.session.set_expiry(?) : nếu 0 là tồn tại đến khi tắt trình duyệt  
    Kiểm tra tồn tại: 'name' in request.session

---------------------------------------------------------------

Template

  - {{ variable }} :Biến
  - {% tag %} :Thẻ tag
  - autoescape(on,off) :chuyển đổi các kí tự đặc biệt trong HTML sang một dạng mã-> bảo vệ website,tắt trên từng biến (| safe)
  - có thể gọi được phương thức nhưng là các phương thức không tham số

  - Model Form :Kế thừa từ lớp form

    - class Meta:
      - model : liên hệ với các lớp trong model
      - fields : chỉ định các trường hiển thị trong form
    trong form luôn có {% csrf_token %} để bảo mật.  


   



       

  
