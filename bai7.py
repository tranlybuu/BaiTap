import smtplib
import getpass

email=input("Email: ")
#password = getpass.getpass("Mật khẩu: ")
password = input("Mật khẩu: ")
address = input("Gửi đến: ")
mess=input("Nội dung: ")
time=int(input("Số lần muốn gửi: "))

client=smtplib.SMTP("smtp.gmail.com",587)
client.starttls()
client.login(email, password)

for i in range(1,time+1):
    content=mess + " - Lan thu " + str(i)
    client.sendmail(email,address,content)
    print("/\nTin nhắn đã được gửi đến {} lần thứ {}\n/\n".format(email,i))

client.quit()
end=input("ENTER để kết thúc")