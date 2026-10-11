ssh -i timeweb root@111.222.33.444
yes
adduser user
usermod -aG sudo user
su - user
logout
ssh -i timeweb user@111.222.33.444
cd ~
mkdir -p .ssh
chmod 700 .ssh
echo "<содержимое публичного ключа>" >> ~/.ssh/authorized_keys