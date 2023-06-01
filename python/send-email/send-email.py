import email.message as em

msg=em.EmailMessage()
msg['From']='jay.*******t.com'
msg['To']='angry******ook.com'
msg['Subject']='Hello Subject !'

# 寄送純文字內容
# msg.set_content("測試看看")

# 寄送比較多樣式的內容(html)
msg.add_alternative("<h3>大大大優惠券</h3>滿五百送一百",subtype="html")

# print(msg)

import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("jay.*******t.com","********")
server.send_message(msg)
server.close()