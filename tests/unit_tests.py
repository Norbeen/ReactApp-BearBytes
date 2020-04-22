import os, send_sms
import unittest

class unit_testsResponse(unittest.TestCase):
    
    def test_check_name(self):
        result = send_sms.user_name("saman", "samman@gmail.com")
        self.assertEqual(result, "saman")
        
    def test_check_email(self):
        result = send_sms.user_email("saman", "saman@gmail.com")
        self.assertEqual(result, "saman@gmail.com")
        
        
    def test_message(self):
        loggedIn = True
        result = send_sms.user_loggedIn(loggedIn)
        self.assertEqual(result, loggedIn)
        
        
if __name__ == '__main__':
     unittest.main()
