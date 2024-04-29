

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import unittest
from unittest.mock import Mock, patch, ANY


def send_mail(smtp_server, smtp_port, from_addr, to_addr, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body)) #, 'plain'))

    server = smtplib.SMTP(host=smtp_server, port=smtp_port)
    server.starttls()
    server.login(from_addr, 'password')
    #server.send_message(msg)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

class TestSendMail(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_send_mail(self, mock_smtp):
        
        send_mail('smtp.example.com', 587, 'from@example.com', 'to@example.com', 'Test', 'Body')

        # mock_smtp.assert_called_once_with('smtp.example.com', 587)
        mock_smtp.assert_called_once_with(host='smtp.example.com', port=587)
        # instance.connect.assert_called_once_with('smtp.example.com', 587)
        instance = mock_smtp.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once_with('from@example.com', 'password')
        instance.sendmail.assert_called_once_with('from@example.com', 'to@example.com', ANY)
        instance.quit.assert_called_with()

if __name__ == '__main__':
    unittest.main()