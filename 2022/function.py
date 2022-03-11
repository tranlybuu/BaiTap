import os
from datetime import date, datetime
import requests
from bs4 import BeautifulSoup

#Hàm này để làm sạch màn hình hiển thị
#Kết quả trả về là thông tin quá trình crawl
def lam_sach_va_tom_tat_lai(url, max_page, count):
    os.system('cls')
    print("\n\tBạn muốn cào dữ liệu bắt đầu từ url:",url)
    print("\tTổng số trang bạn muốn cào là:", max_page)
    print("\t----------------------------")
    print("\tĐã thực hiện được {}% \n".format(round((count / max_page) *100)))

#Hàm này kiểm tra và tạo thư mục CRAWLER
#path: đường dẫn đến ổ C:\
def kiem_tra(path):
    os.chdir(path)  #Di chuển đến thư mục trong đường dẫn path
    check = os.listdir(path)    #List các thư mục hiện có ở ổ C:\
    if 'CRAWLER' not in check:      #Nếu chưa có thư mục CRAWLER thì tạo thư mục CRAWLER
        os.mkdir('CRAWLER')

    #Tạo file History.txt
    path = 'C:\\CRAWLER\\'
    os.chdir(path)  # Di chuển đến thư mục trong đường dẫn path
    check = os.listdir(path)  # List các thư mục hiện có ở ổ C:\CRAWLER

    # Nếu chưa có file History.txt thì tạo thư mục trong CRAWLER
    if 'History.txt' not in check:
        line_1 = "\t+------------------------------------------------------+\n"
        line_2 = "\t|  Đây là file ghi lại lịch sử các url đã cào dữ liệu  |\n"
        line_3 = "\t+------------------------------------------------------+\n\n"
        line_4 = "Số thứ tự của đường link chính là số thứ tự của thư mục chứa nội dung đường dẫn đã cào\n"
        line_5 = "<Ví dụ đường dẫn có số thứ tự 1 thì thư mục chứ nội dung là Trang_web_đã_cào_dữ_liệu_thứ_1>\n\n"
        content = [line_1, line_2, line_3, line_4, line_5]
        file = open("History.txt", "w", encoding="utf-8")
        for item in content:
            file.write(item)
        file.close()

    # Nếu chưa có file Error.txt thì tạo thư mục trong CRAWLER
    if 'Error.txt' not in check:
        line_1 = "\t+-----------------------------------------------------+\n"
        line_2 = "\t|  Đây là file ghi lại các url không thể cào dữ liệu  |\n"
        line_3 = "\t+-----------------------------------------------------+\n\n"
        content = [line_1, line_2, line_3]
        file = open("Error.txt", "w", encoding="utf-8")
        for item in content:
            file.write(item)
        file.close()


#Hàm tạo tên folder tự động <Trang web đã cào dữ liệu thứ + số_thứ_tự>
#Kết quả trả về là tên của thư mục
#Số thứ tự: Đếm số lượng folder trong folder CRAWLER rồi tạo folder với số thứ tự tiếp theo
#path: đường dẫn để tạo và lưu nội dung
def tao_ten_folder_tu_dong(path, url):
    os.chdir(path)      #Di chuển đến thư mục trong đường dẫn path
    const = "Trang_web_đã_cào_dữ_liệu_thứ_"
    count = len(os.listdir(path)) - 1       #Đếm số file và folder hiện có trong thư mục
    name_folder = const + str(count)     #Trang web đã cào dữ liệu thứ + số_thứ_tự
    os.mkdir(name_folder)   #Tạo thư mục
    return name_folder

#Hàm lưu file vào thư mục tự động
# Biến data là 1 list bao gồm:
# 1. Nội dung HTML
# 2. Danh sách mới tìm thấy
# 3. Đường dẫn gốc
# 4. #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
#Kết quả trả về là 3 file txt bao gồm:
# -- Thông_tin_url_đã_cào.txt
# -- Nội_dung.txt
# -- Các_url_mới_tìm_được.txt
def luu_file(data, name_folder):
    path = "C:\\CRAWLER\\"
    os.chdir(path + str(name_folder))    #Di chuyển đến thư mục vừa được tạo tự động
    now = datetime.now()            # \ Lấy dữ liệu thời gian hiện tại
    time = now.strftime("%H:%M")    # / Định dạng về kiểu giờ:phút
    today = date.today()                # \ Lấy dữ liệu ngày tháng năm
    day = today.strftime("%d %B, %Y")   # / Định dạng về kiểu ngày:tháng:năm

    # -- Thông_tin_url_đã_cào.txt
    line_info_1 = "\tĐây là thông tin về đường dẫn vừa cào được"
    line_info_2 = "\n\t------------------------------------------\n"
    line_info_3 = "\tURL: " + str(data[2]) + "\n"
    line_info_4 = "\tNgày: " + str(day) + "\n"
    line_info_5 = "\tThời gian: " + str(time) + "\n"
    # Ghi nội dung vào file txt
    info = [line_info_1,line_info_2,line_info_3,line_info_4,line_info_5]
    file = open("1 - Thông tin url đã cào.txt", "w+", encoding="utf-8")
    for item in info:
        file.write(item)
    file.close()

    # -- Nội_dung.txt
    line_content_1 = "\tĐây là file code HTML vừa cào được"
    line_content_2 = "\n\t------------------------------------------\n\n"
    line_content_3 = str(data[0])
    # Ghi nội dung vào file txt
    url = [line_content_1, line_content_2, line_content_3]
    file = open("2 - File HTML.txt", "w+", encoding="utf-8")
    for item in url:
        file.write(item)
    file.close()

    # -- Các_url_mới_tìm_được.txt
    line_url_1 = "\tĐây là những url mới được tìm thấy trong url này"
    line_url_2 = "\n\t------------------------------------------\n\n"
    line_url_3 = ""
    line_url_4 = data[1]
    #Nội dung của line_url_3
    max_url = data[3]      #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
    if len(line_url_4) == max_url:
        line_url_3 = "Đã tìm thấy nhiều hơn " + str(max_url) + " url mới:\n"
    else:
        line_url_3 = "Đã tìm thấy " + str(len(line_url_4)) + " url mới:\n"
    #Ghi nội dung vào file txt
    url = [line_url_1, line_url_2, line_url_3]
    file = open("3 - Những url mới được tìm thấy.txt", "w+", encoding="utf-8")
    for item in url:
        file.write(item)
    for item in range(len(line_url_4)):
        add_url = str(item + 1) + " - " + str(line_url_4[item]) + "\n"
        file.write(str(add_url))
    file.close()

def luu_lich_su_cac_url(url):
    path = "C:\\CRAWLER\\"
    os.chdir(path)

    # Lấy số thứ tự
    file = open("History.txt", mode='r+', encoding='utf-8')
    STT = len(file.readlines()) - 6
    file.close()

    # Ghi thêm đường dẫn vừa được duyệt vào lịch sử
    file = open("History.txt", mode='a+', encoding='utf-8')
    content = str(STT) + " -- " + str(url) + "\n"
    file.write(content)
    file.close()

def error_url(url):
    path = "C:\\CRAWLER\\"
    os.chdir(path)  # Di chuyển đến thư mục vừa được tạo tự động

    # Lấy số thứ tự
    file = open("Error.txt", mode='r+', encoding='utf-8')
    STT = len(file.readlines()) - 3
    file.close()

    # Ghi thêm đường dẫn bị lỗi
    file = open("Error.txt", mode='a+', encoding='utf-8')
    content = str(STT) + " -- " + str(url) + "\n"
    file.write(content)
    file.close()

#Hàm này để lấy đoạn code HTML
#Kết quả trả về là kiểu dữ liệu văn bản chứa code HTML
def doc_noi_dung(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    return content

#Hàm này dùng để lọc ra các đường dẫn
#Kết quả trả về là list chứa các đường dẫn hợp lệ
def lay_cac_duong_link(content):
    url_list = []
    result = []
    raw = content.find_all("a")
    for item in raw:
        link = item.get("href")
        url_list.append(link)
    for item in url_list:
        item = str(item)
        # Lấy các đường dẫn đầy đủ
        if not (item.find("http", 0, 4)):
            result.append(item)
        # Lấy các đường dẫn còn thiếu http...
        else:
            if not (item.find("http", 0, 4)):   #Lấy các đường dẫn chưa có http
                if not (item.find("java", 0, 4)):   #Loại các phần tử Javascript
                        if not (item.find("#", 0, 4)):   #Loại các phần tử "#"
                            if not (item.find("None", 0, 4)):   #Loại các phần tử None
                                if len(item) > 2:
                                    result.append(item)
    return result

#Hàm này dùng để chỉnh sửa đường dẫn
#Kết quả trả về là True nếu đường dẫn đầy đủ và False nếu đường dẫn chưa đầy đủ
def kiem_tra_link(link):
    if link[:4] == "http":
        return True
    else:
        return False


def chinh_sua_link(url,item):
    item = item.split(" ")
    url_new= str(url) + item[0]
    return url_new

""" ---------------------------------------------------------- """
""" --------------------> CODE RUN <-------------------------- """
""" ---------------------------------------------------------- """

first_url = str(input("Nhập đường dẫn ban đầu bạn muốn cào dữ liệu: "))
max_page = int(input("Bạn muốn cào tối đa bao nhiêu url: "))    #Quy định số lượng trang web được tải về
url_list = []  #Chứa các đường link chưa duyệt
url_list_const=10000        #Số lượng tối đa mà danh sách chờ duyệt có thể chứa
error = []  # Những đường dẫn không thể cào dữ liệu
history=[]  #Chứa các đường link đã duyệt
count=0     #Đếm số lượng trang web đã tải
kiem_tra("C:\\")    #Kiểm tra và tạo thư mục CRAWLER để lưu trữ
data_folder = 'C:\\CRAWLER'     #Lưu vào ổ C thư mục CRAWLER
url_list.append(str(first_url))

while (count < max_page) and (len(url_list) > 0):
    if (count == 0) or (count % 5 == 0):
        lam_sach_va_tom_tat_lai(first_url, max_page, count)
    url_new = []  # Chứa các đường link mới được tìm thấy
    url_new_const = 500  #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
    url = url_list.pop(0)   #Lấy đường dẫn đầu tiên trong danh sách chưa duyệt

    try:
        page = doc_noi_dung(url)
        links = lay_cac_duong_link(page)
        for item in links:     #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if kiem_tra_link(item)==False:
                item = chinh_sua_link(url,item)     #Chỉnh sửa nếu thiếu phần http://...
            if (item not in url_list) and (item not in history) and (item not in url_new) and (item != url):   #  <=======\\
            #Nếu đường link chưa được duyệt vào hàng đợi, chưa có trong lịch sử, khác đường dẫn đang duyệt                //
            #và chưa được tìm thấy trong danh sách các đường dẫn mới được tìm thấy              [========================//
                if len(url_new)<url_new_const:      #Nếu danh sách các đường link vừa tìm thấy lớn hơn thì không thêm vào nữa
                    url_new.append(item)            #Thêm link mới vào danh sách chờ duyệt
        if (len(url_list) + len(url_new) <= url_list_const):    #Chuyển các đường dẫn mới tìm thấy vào danh sách chờ duyệt
            url_list = url_list + url_new
        else:
            check = int(url_list_const - len(url_list))      #Tính số lượng đường dẫn có thể thêm vào danh sách chờ duyệt
            array =url_new[:check]
            url_list = url_list + array

        history.append(url)        #Lưu url vừa duyệt vào lịch sử
        count += 1             #Đếm số url đã duyệt

        # Lưu lại dữ liệu vừa cào được vào thư mục
        data_array = [page, url_new, url, url_new_const]
        #Bao gồm:
        # 1. Nội dung HTML
        # 2. Danh sách mới tìm thấy
        # 3. Đường dẫn gốc
        # 4. Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
        name_folder = tao_ten_folder_tu_dong(data_folder,url)    #Tạo thư mục tự động và kết quả trả về là tên thư mục vừa tạo
        luu_file(data_array, name_folder)
        luu_lich_su_cac_url(url)
        print("\tĐã duyệt " + str(count) + " url")
    except:
        print("\tCó đường dẫn bị lỗi ")
        error.append(url)
        error_url(url)

lam_sach_va_tom_tat_lai(first_url, max_page, count)
#Thông báo
if len(error) != 0:
    print("\tCó " + str(len(error)) +  " đường dẫn không lấy được dữ liệu:")
    for i in range(len(error)):
        print(str(i+1) + " - " + str(error[i]))
else:
    print("\tKhông có đường dẫn nào bị lỗi")
print("\n\t+-------------------------------------------+\n\t| Dữ liệu đã cào đã được lưu tại C:\\CRAWLER |\n\t+-------------------------------------------+\n\t")