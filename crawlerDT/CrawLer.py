import requests
from bs4 import BeautifulSoup
import xlwings as xw

base_url = 'https://mapstudy.vn/danh-muc/khoa-hoc/0/tat-ca'

# Tạo một tệp Excel mới 
wb = xw.Book()  
tep = wb.sheets[0]  # Chọn tệp đầu tiên

# Ghi tiêu đề cột
tep.range('A1').value = 'Tiêu đề'
tep.range('B1').value = 'Giáo viên'
tep.range('C1').value = 'Link chi tiết'

# Biến để đếm số hàng trong Excel
row_idx = 2

# Số trang bạn muốn lấy 
so_trang = 5


for trang in range(1, so_trang + 1):
    # Tạo URL với số trang
    url = f'{base_url}?page={trang}'
    
    response = requests.get(url)
    
    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        khoa_hoc_elements = soup.find_all('div', class_='row-item col-md-6 col-lg-4 col-xl-4')
        
        # Nếu không có khóa học nào, dừng lại (có thể là trang cuối)
        if not khoa_hoc_elements:
            print(f"Không tìm thấy khóa học ở trang {trang}. Dừng lại.")
            break
        
        # Lặp qua từng khóa học và lấy thông tin cần thiết
        for khoa_hoc in khoa_hoc_elements:

            tieu_de = khoa_hoc.find('a', class_='').text.strip()
            giao_vien = khoa_hoc.find('span', class_='').text.strip()
            link = khoa_hoc.find('a')['href']
            

            tep.range(f'A{row_idx}').value = tieu_de
            tep.range(f'B{row_idx}').value = giao_vien
            tep.range(f'C{row_idx}').value = link
            
            # Tăng chỉ số hàng
            row_idx += 1
    
    else:
        print(f"Không thể truy cập, lỗi: {response.status_code}")
        break


wb.save('khoa_hocc.xlsx')
wb.close()  
print("Dữ liệu đã được ghi vào 'khoa_hocc.xlsx'")
