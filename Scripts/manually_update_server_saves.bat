echo ------------------
echo Git add changes
echo ------------------
pushd %GIT_PROJECT_PATH%
git add --all
git commit -m "update: (Saves) manually save update"
git push
popd