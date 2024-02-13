
Write-Output "------------------"
Write-Output "Start install SteamCMD script"
Write-Output "------------------"

# Script Settings
$steam_cmd_zip_download_url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
$steam_cmd_zip_download_path = "./temp/steamcmd.zip"
$steam_cmd_download_path = [System.IO.Path]::GetDirectoryName($steam_cmd_zip_download_path)
$steam_cmd_exe_path = "$env:STEAMCMD_PATH"
$steam_cmd_path = [System.IO.Path]::GetDirectoryName($steam_cmd_exe_path)

# Create Folder
[void](New-Item -ItemType Directory -Path "." -Name $steam_cmd_download_path)
if (!(Test-Path $steam_cmd_path -PathType Container)) {
  New-Item -ItemType Directory -Force -Path $steam_cmd_path
}

Write-Output "------------------"
Write-Output "Download SteamCMD"
Write-Output "------------------"

# Download steamcmd.zip
Invoke-WebRequest $steam_cmd_zip_download_url -OutFile ($steam_cmd_zip_download_path)

Write-Output "------------------"
Write-Output "Unzip/Install SteamCMD"
Write-Output "------------------"

# unzip steamcmd.zip
if (!(Test-Path ($steam_cmd_exe_path)))
{
  Expand-Archive ($steam_cmd_zip_download_path) -DestinationPath $steam_cmd_path
}
else 
{
  Write-Output $steam_cmd_exe_path
  Write-Output "::SteamCMD.exe already exists"
}
# install steamcmd.exe
Start-Process -FilePath $steam_cmd_exe_path

Write-Output "------------------"
Write-Output "Remove temp files"
Write-Output "------------------"

# remove temp folder
if (Test-Path $steam_cmd_download_path)
{
  Remove-Item -Recurse -Force $steam_cmd_download_path
}
