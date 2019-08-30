import unittest
from logger import Logger

class LoggerTest(unittest.TestCase):
    
    def test_info(self):
        log_value=Logger(self.mock_log)
        log_value.info("Pretend log entry")
        self.assertEqual(dummy_file,"[INFO] Pretend log entry", "Did not log properly for info")
        
    def test_error(self):
        log_value=Logger(self.mock_log)
        log_value.error("Pretend error message")
        self.assertEqual(dummy_file,"[WARNING] Pretend error message", "Did not log properly for error")
        
    def mock_log(self, mock_file):
        global dummy_file
        dummy_file=mock_file
        
if __name__ == '__main__':
    unittest.main()
    