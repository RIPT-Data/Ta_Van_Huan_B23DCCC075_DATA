# Báo cáo: Crawler Data trên Trang Mapstudy.vn

## Giới thiệu

Bài báo cáo này trình bày về việc xây dựng một crawler dữ liệu sử dụng Python để thu thập thông tin khóa học từ trang web Mapstudy.vn

### Mục tiêu

- **Thu thập dữ liệu**: Thu thập thông tin khóa học từ nhiều trang khác nhau trên trang web
- **Lưu trữ dữ liệu**: Lưu trữ dữ liệu thu thập được vào một file Excel để dễ dàng cho việc xử lý và phân tích sau này

### Tầm quan trọng

- **Tự động hóa**: Giúp tự động hóa quá trình thu thập dữ liệu, tiết kiệm thời gian và công sức
- **Phân tích dữ liệu**: Dữ liệu thu thập được có thể sử dụng cho các mục đích phân tích, báo cáo hoặc nghiên cứu

## Công nghệ và thư viện sử dụng

### 1. Python

Python là ngôn ngữ lập trình được sử dụng để phát triển crawler này. Python nổi bật với cú pháp đơn giản và phong phú, giúp lập trình viên dễ dàng phát triển các ứng dụng web scraping

### 2. Thư viện Requests

[Requests] là một thư viện Python dùng để gửi các yêu cầu HTTP một cách dễ dàng và hiệu quả. Trong dự án này, Requests được sử dụng để gửi yêu cầu GET tới trang web Mapstudy.vn để lấy dữ liệu HTML

### 3. Thư viện BeautifulSoup

[BeautifulSoup] là một thư viện mạnh mẽ để phân tích cú pháp HTML và XML. Thư viện này giúp chúng ta dễ dàng tìm kiếm và trích xuất dữ liệu từ các thẻ HTML. Trong bài crawler này, BeautifulSoup được sử dụng để lấy thông tin về tiêu đề, giáo viên và link chi tiết của các khóa học

### 4. Thư viện xlwings

[xlwings] là một thư viện Python cho phép tương tác với Microsoft Excel. Nó giúp chúng ta dễ dàng tạo và chỉnh sửa các file Excel từ mã Python. Trong dự án này, xlwings được sử dụng để lưu trữ dữ liệu thu thập được vào một file Excel mới

## Các bước thực hiện

### Bước 1: tạo tệp Excel và cấu trúc trang và import các thư viện cần sử dụng

- Khởi tạo một tệp Excel mới bằng cách sử dụng thư viện `xlwings`. File Excel này sẽ được sử dụng để lưu trữ dữ liệu khóa học mà ta sẽ thu thập được.
- Cấu trúc trang của website được xác định thông qua việc phân tích HTML, cụ thể là các phần tử chứa khóa học, giáo viên và link
- import thư viện xlwings để tạo file excel, thư viện requests và thư viện BeautifulSoup để yêu cầu dữ liệu trang web và truy xuất lấy nội dung trang web

```python
import requests
from bs4 import BeautifulSoup
import xlwings as xw

wb = xw.Book()
tep = wb.sheets[0]

# tạo cột hàng
tep.range('A1').value = 'Tiêu đề'
tep.range('B1').value = 'Giáo viên'
tep.range('C1').value = 'Link chi tiết'

# Biến để đếm số hàng trong Excel
row_idx = 2
so_trang = 5
```

### Bước 2: Gửi yêu cầu http và lấy nội dung của trang web

- Sử dụng thư viện requests để gửi yêu cầu HTTP đến trang web Mapstudy.vn và lấy nội dung HTML của từng trang.

```python
base_url = 'https://mapstudy.vn/danh-muc/khoa-hoc/0/tat-ca'
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
```

### Bước 3: phân tích cú pháp HTML và tìm kiếm các dữ liệu khóa học

- Sau khi nhận được nội dung HTML, sử dụng BeautifulSoup để phân tích và trích xuất thông tin của các khóa học. Mỗi khóa học sẽ được tìm trong các phần tử HTML có class tương ứng, và chúng ta sẽ thu thập tiêu đề khóa học, giáo viên giảng dạy và đường link chi tiết

- Sau khi lấy được thông tin từ mỗi khóa học, chúng ta sẽ lưu trữ dữ liệu này vào file Excel. Mỗi thông tin như tiêu đề khóa học, giáo viên, và đường link sẽ được ghi vào từng cột tương ứng trong bảng tính

```python
# Lặp qua từng khóa học và lấy thông tin cần thiết
        for khoa_hoc in khoa_hoc_elements:

            tieu_de = khoa_hoc.find('a', class_='').text.strip()
            giao_vien = khoa_hoc.find('span', class_='').text.strip()
            link = khoa_hoc.find('a')['href']

            # lưu trữ dữ liệu
            tep.range(f'A{row_idx}').value = tieu_de
            tep.range(f'B{row_idx}').value = giao_vien
            tep.range(f'C{row_idx}').value = link

            # Tăng chỉ số hàng
            row_idx += 1

    else:
        print(f"Không thể truy cập, lỗi: {response.status_code}")
        break
```

### Bước 4: Lưu dữ liệu và đóng file

- dữ liệu sẽ được lưu và đóng file

```python
wb.save('khoa_hocc.xlsx')
wb.close()
print("Dữ liệu đã được ghi vào 'khoa_hocc.xlsx'")
```
