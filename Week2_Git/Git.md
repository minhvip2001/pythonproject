 Git
- Là hệ thông kiểm soát phiên bản.
- git status: kiểm tra trạng thái
- git add filename: theo dõi tệp file để chuẩn bị commit.
- git commit : lưu lịch sử và cam kết cho sự thay đổi
- git commit -m"mess":
- git commit --amend -m"mess": không tạo mới commit,cập nhật vào commit gần nhất

Không theo dõi một số file

- .gitignore:chưa danh sách các file ,thư phục không theo dõi (được đặt ở trong thư mục gốc)

Phục hồi file

-git restore :phục hồi file
-git restore filename:

Xem lịch xử commit

- git log: hiển thị các danh sách các commit
- git log --oneline:gọn hơn
- git log --oneline --graph:sơ đồ gộp nhánh và commit

Xóa commit: git reset:xóa commit

Xem sự thay đổi: git diff:xem các thay đổi

Nhánh

- git branch:liệt kê các nhánh
- git branch name:tạo nhánh mới
- git branch -a:xem trên remote đang có những nhánh nào

Đổi nhánh

- git checkout namebranch: chuyển sang nhánh khác

Remote

- git remote add origin url:liên kết local với remote origin
- git clone url:tải về kho chứa chỉ tải về nhánh master,ở nhánh master
- git branch -a :kiểm tra remote có những nhánh nào
- git fetch (+origin:tên remote):tải về không tin từ remote,chưa áp dụng vào local,nhưng có thể lấy thông tin từ nó
- git log -p -n:xem thay đổi giữa các commit
- git diff commit commit xem sự thay đổi giữa commit trên local và remote
- git checkout namebranch:tải về nhánh trên remote(không tải tất cả nhánh,fetch trước đó rồi )


