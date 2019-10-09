# ref: https://qiita.com/SHASE03/items/16fd31d3698f207b42c9

# need only once
sudo easy_install pip
pip install --upgrade pip
conda activate cv_env  # use python3
python --version
pip install opencv-python -t ./
rm -rf bin/
rm -rf *.dist-info
