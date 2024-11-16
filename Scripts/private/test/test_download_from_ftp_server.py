import unittest
from unittest.mock import patch, MagicMock
from download_from_ftp_server import download_file  # Angenommene Funktion

class TestFTPDownload(unittest.TestCase):
    
    @patch('ftplib.FTP')
    def test_download_file_success(self, MockFTP):
        # Mock FTP-Verbindung
        mock_ftp = MockFTP.return_value
        mock_ftp.login.return_value = None
        mock_ftp.retrbinary.return_value = None

        # Testen der Download-Funktion
        result = download_file('ftp.example.com', 'user', 'password', 'remote_path', 'local_path')

        # Sicherstellen, dass FTP-Verbindung ge�ffnet und Datei heruntergeladen wurde
        mock_ftp.login.assert_called_once_with('user', 'password')
        mock_ftp.retrbinary.assert_called_once()
        self.assertTrue(result)

    @patch('ftplib.FTP')
    def test_download_file_failure(self, MockFTP):
        # Mock FTP-Verbindung mit Fehler
        mock_ftp = MockFTP.return_value
        mock_ftp.login.side_effect = Exception("Login failed")

        # Testen der Download-Funktion bei Fehler
        result = download_file('ftp.example.com', 'user', 'password', 'remote_path', 'local_path')

        # Sicherstellen, dass Fehler richtig behandelt wird
        mock_ftp.login.assert_called_once_with('user', 'password')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()