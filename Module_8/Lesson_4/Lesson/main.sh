python3 -V
sudo apt install python3-virtualenv
sudo apt update
sudo apt upgrade
sudo apt install vim
cat << EOF > ~/.vimrc
set number
set cursorline
set encoding=UTF-8
EOF
cat ~/.vimrc
mkdir workspace
cd workspace
python3 -m virtualenv -p python3 venv
source venv/bin/activate
pip install flask
touch app.py
vim app.py
flask run
flask run -h 111.222.333.444
cat app.py
flask run -h 111.222.333.444
