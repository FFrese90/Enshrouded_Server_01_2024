import os
from ftplib import FTP
from server_secrets import server_secrets

# FTP-Verbindungsdaten
FTP_HOST = server_secrets.FTP_HOST
FTP_PORT = server_secrets.FTP_PORT
FTP_USER = server_secrets.FTP_USER
FTP_PASS = server_secrets.FTP_PASS
FTP_REMOTE_DIR = server_secrets.FTP_REMOTE_DIR
LOCAL_DIR = os.path.join("..","..", "Savegame")  # Der Ordner auf deinem lokalen PC, der die Savegames enthaelt

def connect_to_ftp():
    """Stellt eine Verbindung zum FTP-Server her."""
    print('Connect to FTP')
    ftp = FTP()
    ftp.connect(FTP_HOST,FTP_PORT)
    print('Login to FTP')
    ftp.login(FTP_USER, FTP_PASS)
    print('Connected and logged in to FTP')

    return ftp


def download_files(ftp, remote_dir, local_dir):
    """Laedt alle Dateien aus einem remote Verzeichnis in ein lokales Verzeichnis herunter."""
    # Wechselt in das remote Verzeichnis
    ftp.cwd(remote_dir)
    
    # Erstellen des lokalen Verzeichnisses, falls es noch nicht existiert
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    try:
        files = ftp.nlist()
    except Exception as error:
        print(f"FTP NLST not worked: {error}")
        try:
            print("FTP DIR")
            files = []
            ftp.dir(lambda line: files.append(line.split()[-1]))
        except Exception as error:
            print(f"FTP DIR not worked: {error}")

    for file in files:
        remote_file_path = f"{remote_dir}/{file}"
        local_file_path = os.path.join(local_dir, file)
        
        # Wenn es sich um ein Verzeichnis handelt, rekursiv herunterladen
        if file.endswith('/'):
            download_files(ftp, remote_file_path, local_file_path)
        else:
            # Datei herunterladen
            with open(local_file_path, 'wb') as file_handle:
                ftp.retrbinary(f"RETR {remote_file_path}", file_handle.write)
            print(f"Datei {remote_file_path} erfolgreich heruntergeladen!")

def main():
    # Verbindung zum FTP-Server herstellen
    ftp = connect_to_ftp()
    
    try:
        # Dateien vom Server herunterladen
        print("Lade Dateien herunter...")
        download_files(ftp, FTP_REMOTE_DIR, LOCAL_DIR)
        
    finally:
        ftp.quit()
        print("FTP-Verbindung geschlossen.")

if __name__ == "__main__":
    main()
