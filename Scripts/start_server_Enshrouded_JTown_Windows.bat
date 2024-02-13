@echo off

echo ------------------
echo Updating server
echo ------------------
call %STEAMCMD_PATH% +force_install_dir %SERVER_DATA_PATH% +login anonymous +app_update 2278520 validate +quit

echo ------------------
echo Updating git changes
echo ------------------
rem git pull

echo ------------------
echo Starting server
echo ------------------
call %SERVER_DATA_PATH%enshrouded_server.exe
  
echo ------------------
echo Server stopped
echo ------------------

echo ------------------
echo Git add changes
echo ------------------
pushd %GIT_PROJECT_PATH%
rem git add --all
rem git commit -m "update: (Saves) post Server stopped saves update"
rem git push
popd

echo ------------------
echo Script end
echo ------------------
pause