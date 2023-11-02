import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

# Change to your own account information
to = 'xxxxxxxxxxxxxxxx@buffalo.edu'
gmail_user = 'xxxxxxxxxxxxxxx@gmail.com'
gmail_password = 'xxxxxxxxxxxxxxxxxxx'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
# Very Linux Specific
arg='ip route list'
encoding = 'utf-8'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index(b'src')+1]
ip = (ipaddr.decode('utf-8'))
my_ip = 'My IP address is %s' %  ip
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi Zero Two on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
