from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置 Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "fzzzjnzl@gmail.com"
app.config["MAIL_PASSWORD"] = "fmqr uuiq toqu gkob"  # 应用专用密码
app.config["MAIL_DEFAULT_SENDER"] = "fzzzjnzl@gmail.com"

mail = Mail(app)

@app.route("/send-email")
def send_email():
    try:
        msg = Message("测试邮件", recipients=["fzzzjnzl@gmail.com"])
        msg.body = "你好，这是 Flask 发送的邮件！"
        mail.send(msg)
        return "邮件发送成功！"
    except Exception as e:
        return f"邮件发送失败: {e}"

if __name__ == "__main__":
    app.run(debug=True)
