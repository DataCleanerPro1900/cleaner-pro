from http.server import BaseHTTPRequestHandler
import json
import csv
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 从环境变量读取配置
SENDER_EMAIL = os.environ.get('SENDER_EMAIL', '416465186@qq.com')
SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD', '')
CSV_FILE = "/tmp/collected_emails.csv"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            email = data.get('email', '')
            
            if email:
                # 保存到CSV
                self.save_email(email)
                
                # 发送自动回复邮件
                if SENDER_PASSWORD:
                    self.send_welcome_email(email)
                
                # 返回成功
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True}).encode())
            else:
                self.send_response(400)
                self.end_headers()
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def save_email(self, email):
        """保存邮箱到CSV"""
        file_exists = os.path.exists(CSV_FILE)
        
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['email', 'collected_at', 'source'])
            writer.writerow([email, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'landing_page'])
        
        print(f"[收集] 新邮箱: {email}")
    
    def send_welcome_email(self, recipient):
        """发送欢迎邮件"""
        try:
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient
            msg['Subject'] = "Data Cleaner Pro - 您的免费资源已送达"
            
            body = """亲爱的用户，

感谢您订阅 Data Cleaner Pro！

以下是您获取的免费资源：

1. Data Cleaner Pro 7天试用版
   下载链接：https://github.com/yourusername/data-cleaner-pro
   激活码：FREE-TRIAL-2024

2. 《Python数据清洗实战指南》PDF
   下载链接：[待添加]

3. 100+ 数据清洗代码模板
   下载链接：[待添加]

如有任何问题，请回复此邮件或联系我们的技术支持。

祝使用愉快！
Data Cleaner Pro 团队"""
            
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            # 连接QQ邮箱服务器
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            print(f"[邮件] 已发送欢迎邮件到: {recipient}")
        except Exception as e:
            print(f"[邮件] 发送失败: {e}")
