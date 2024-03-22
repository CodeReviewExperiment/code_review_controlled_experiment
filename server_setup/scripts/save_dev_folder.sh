#!/bin/bash

# Save the contents of the folder passed as parameter under the folder
# /home/<user>/user_folders/, renaming it to <folder>_orig, updating
# permissions and zipping it. Additionally, save lighter folder that only
# contains Tako and projects data, as well as code-review.csv located in
# the root of the folder.

BASE_DIR=/home/<user>/user_folders

cp -r "$1" "$BASE_DIR"
dev_dir=$(basename "$1")
mv "$BASE_DIR/$dev_dir" "$BASE_DIR/${dev_dir}_orig"
chmod -R 777 "$BASE_DIR/${dev_dir}_orig"
zip -r "$BASE_DIR/${dev_dir}_orig.zip" "$BASE_DIR/${dev_dir}_orig"

# Save lighter folder
mkdir "$BASE_DIR/${dev_dir}"
cp -r "$BASE_DIR/${dev_dir}_orig/.vscode-server/data/User/globalStorage/codelounge.tako" "$BASE_DIR/${dev_dir}"
cp -r "$BASE_DIR/${dev_dir}_orig/cr-study-2024" "$BASE_DIR/${dev_dir}"
cp "$BASE_DIR/${dev_dir}_orig/code-review.csv" "$BASE_DIR/${dev_dir}"
chmod -R 777 "$BASE_DIR/${dev_dir}"

# Delete original folder
rm -rf "$BASE_DIR/${dev_dir}_orig"
