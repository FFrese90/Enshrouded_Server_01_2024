# Enshrouded: Early Access - Server - 01.2024

Documentation of scripts, saves, and configuration for the Enshrouded server running as a dedicated server on various hosts.

## Clone Repository

Run:
```sh
git clone https://github.com/FFrese90/Enshrouded_Server_01_2024.git
```
Example:
```sh
git clone https://github.com/FFrese90/Enshrouded_Server_01_2024.git
```

## Configure Local Path

Copy the `server_secrets_template.py` file from `Scripts/private/server_secrets/` and rename it to `server_secrets.py`. Then, fill in your FTP server details:
```py
FTP_HOST = "0.0.0.0"  # Host Server
FTP_PORT = 21         # Host Port (Default=21)
FTP_USER = "gp****"   # Login Username
FTP_PASS = "********" # Login Password
FTP_REMOTE_DIR = "/savegame" # Replace with the target directory on the server
```

## Install SteamCMD

Run the script to install SteamCMD:
```sh
Scripts/install_SteamCMD.bat
```

## Start Server

Run the script to start the Enshrouded server:
```sh
Scripts/start_server_Enshrouded_JTown_Windows.bat
```

## Download Savegame from FTP

Run the script to download the savegame from the FTP server:
```sh
Scripts/download_savegame_from_ftp.bat
```

## Upload Savegame to FTP

Run the script to upload the savegame to the FTP server:
```sh
Scripts/upload_savegame_to_ftp.bat
```

## Manually Update Server Saves

Run the script to manually update server saves:
```sh
Scripts/manually_update_server_saves.bat
```

## Project Structure

- `.github/workflows/`: Contains CI/CD pipeline configurations.
- `.vscode/settings.json`: Configures VS Code for testing with Unittest.
- `Savegame/`: Contains savegame files and logs.
- `Scripts/`: Contains various scripts for server management.
  - `download_savegame_from_ftp.bat`: Batch script to download savegames from the FTP server.
  - `install_SteamCMD.bat`: Batch script to install SteamCMD.
  - `manually_update_server_saves.bat`: Batch script to manually update server saves.
  - `private/`: Contains private scripts and server secrets.
    - `clear_and_upload_to_ftp_server.py`: Python script to clear and upload savegames to the FTP server.
    - `download_from_ftp_server.py`: Python script to download savegames from the FTP server.
    - `install_SeamCMD.ps1`: PowerShell script to install SteamCMD.
    - `server_secrets/server_secrets_template.py`: Template for server secrets.
    - `test/test_download_from_ftp_server.py`: Unit tests for the FTP download script.
  - `start_server_Enshrouded_JTown_Windows.bat`: Batch script to start the Enshrouded server.
  - `upload_savegame_to_ftp.bat`: Batch script to upload savegames to the FTP server.
- `ServerData/`: Contains server data files.

## Running Tests

To run the tests, use the following command:
```sh
python -m unittest discover -s Scripts/private/test -p "test_*.py"
```

## Continuous Integration

The project uses GitHub Actions for continuous integration. The configuration is located in `.github/workflows/python_ci.yml`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.