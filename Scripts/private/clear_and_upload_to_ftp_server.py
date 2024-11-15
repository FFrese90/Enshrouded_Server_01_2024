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

def delete_remote_folder(ftp, folder):
    """Laescht den Ordner auf dem FTP-Server, falls er existiert."""
    try:
        ftp.cwd(folder)
        files = ftp.nlst()
        for file in files:
            try:
                ftp.delete(file)
            except:
                # Falls es sich um ein Verzeichnis handelt, muss es rekursiv gelaescht werden.
                delete_remote_folder(ftp, f"{folder}/{file}")
        ftp.rmd(folder)
    except Exception as e:
        print(f"Fehler beim Laeschen des Ordners: {e}")

def upload_files(ftp, local_dir, remote_dir):
    """Laedt alle Dateien aus einem lokalen Verzeichnis in ein remote Verzeichnis hoch."""
    # Wechsel in das remote Verzeichnis
    try:
        ftp.mkd(remote_dir)
    except:
        pass  # Falls das Verzeichnis bereits existiert
    
    ftp.cwd(remote_dir)
    try:
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path =  f"{remote_dir}/{os.path.basename(local_file_path)}"  #os.path.join(remote_dir, os.path.relpath(local_file_path, local_dir))
                
                # Sicherstellen, dass das Verzeichnis auf dem Server existiert
                remote_folder = os.path.dirname(remote_file_path)
                try:
                    ftp.mkd(remote_folder)
                except:
                    pass  # Falls das Verzeichnis bereits existiert
                
                # Datei hochladen
                with open(local_file_path, 'rb') as file_handle:
                    ftp.storbinary(f"STOR {remote_file_path}", file_handle)
                print(f"Datei {local_file_path} erfolgreich hochgeladen!")
    except:
      print(f"# Fehler beim Upload")

def main():
    # Verbindung zum FTP-Server herstellen
    ftp = connect_to_ftp()
    
    try:
        # Loeschen des vorhandenen Ordners auf dem Server
        print("Loesche vorhandenen Ordner auf dem Server...")
        delete_remote_folder(ftp, FTP_REMOTE_DIR)
        
        # Hochladen der lokalen Savegames
        print("Lade Dateien hoch...")
        upload_files(ftp, LOCAL_DIR, FTP_REMOTE_DIR)
        
    finally:
        ftp.quit()
        print("FTP-Verbindung geschlossen.")

if __name__ == "__main__":
    main()
