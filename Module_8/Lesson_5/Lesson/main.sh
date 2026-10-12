ssh -i timeweb user@111.222.333.444
cd workspace/
mkdir new_year_application
cd new_year_application
touch app.py
vim app.py
mkdir templates
pwd
logout
scp -i timeweb /Users/krotose1/workspace/skv/skillbox/python_advanced/module_08_deploy/materials/new_year_application/templates/readme.txt user@111.222.333.444:/home/user/workspace/new_year_application/templates/readme.txt
ls materials/new_year_application/templates/*
scp -i timeweb materials/new_year_application/templates/index.html user@111.222.333.444:/home/user/workspace/new_year_application/templates/index.html
scp -i timeweb materials/new_year_application/templates/css user@111.222.333.444:/home/user/workspace/new_year_application/templates/css
scp -i timeweb -r materials/new_year_application/templates/css user@111.222.333.444:/home/user/workspace/new_year_application/templates/css
sudo apt install rsync
rsync -e "ssh -i timeweb" -Praz materials/new_year_application/templates user@111.222.333.444:/home/user/workspace/new_year_application/
rsync -e "ssh -i timeweb" -Praz materials/new_year_application/templates user@111.222.333.444:/home/user/workspace/new_year_application/
rsync -e "ssh -i timeweb" -Praz materials/new_year_application/templates user@111.222.333.444:/home/user/workspace/new_year_application/
ssh -i timeweb user@111.222.333.444
cd workspace/
ls
source venv/bin/activate
cd new_year_application/
flask run -h 111.222.333.444
