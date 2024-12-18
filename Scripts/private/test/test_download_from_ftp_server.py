import unittest
from unittest.mock import MagicMock, patch

import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))

class TestFTPDownload(unittest.TestCase):
    @patch.dict('sys.modules', {'server_secrets': MagicMock(server_secrets={'host': 'mock_host', 'username': 'mock_user', 'password': 'mock_pass'})})
    @patch('ftplib.FTP')
    def test_download_files_success(self, MockFTP):
        from download_from_ftp_server import download_files  # Angenommene Funktion
        # Mock FTP-Verbindung
        mock_ftp = MockFTP.return_value
        mock_ftp.login.return_value = None
        mock_ftp.retrbinary.return_value = None

        # Testen der Download-Funktion
        result = download_files('ftp.example.com', 'user', 'password', 'remote_path', 'local_path')

        # Sicherstellen, dass FTP-Verbindung ge�ffnet und Datei heruntergeladen wurde
        mock_ftp.login.assert_called_once_with('user', 'password')
        mock_ftp.retrbinary.assert_called_once()
        self.assertTrue(result)
    @patch.dict('sys.modules', {'server_secrets': MagicMock(server_secrets={'host': 'mock_host', 'username': 'mock_user', 'password': 'mock_pass'})})
    @patch('ftplib.FTP')
    def test_download_files_failure(self, MockFTP):
        from download_from_ftp_server import download_files  # Angenommene Funktion
        # Mock FTP-Verbindung mit Fehler
        mock_ftp = MockFTP.return_value
        mock_ftp.login.side_effect = Exception("Login failed")

        # Testen der Download-Funktion bei Fehler
        result = download_files('ftp.example.com', 'user', 'password', 'remote_path', 'local_path')

        # Sicherstellen, dass Fehler richtig behandelt wird
        mock_ftp.login.assert_called_once_with('user', 'password')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
