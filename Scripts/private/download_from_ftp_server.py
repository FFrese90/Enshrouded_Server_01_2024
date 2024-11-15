import os
from ftplib import FTP
from own_secrets import own_secrets

# FTP-Verbindungsdaten
FTP_HOST = "saves.4netplayers.de"  # Ersetze durch die FTP-Server-Adresse
FTP_USER = own_secrets.FTP_USER
FTP_PASS = own_secrets.FTP_PASS
FTP_REMOTE_DIR = "/1314901/savegame" # Ersetze durch das Zielverzeichnis auf dem Server
LOCAL_DIR = os.path.join("..","..", "bak_Savegames")  # Der Ordner auf deinem lokalen PC, der die Savegames enthaelt

def connect_to_ftp():
    """Stellt eine Verbindung zum FTP-Server her."""
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp

def download_files(ftp, remote_dir, local_dir):
    """Laedt alle Dateien aus einem remote Verzeichnis in ein lokales Verzeichnis herunter."""
    # Wechselt in das remote Verzeichnis
    ftp.cwd(remote_dir)
    
    # Erstellen des lokalen Verzeichnisses, falls es noch nicht existiert
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    files = ftp.nlst()
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
