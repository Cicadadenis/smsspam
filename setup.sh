apt update 
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
curl -O https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
tar -xf Python-3.8.2.tar.xz
cd Python-3.8.2
./configure --enable-optimizations
make -j 4
make altinstall
mkdir ~/my_app && cd ~/my_app
python3.8 -m venv my_app_venv
source my_app_venv/bin/activate
cd ..
pip install poetry
pip install --upgrade pip
poetry install
poetry run python -m app
