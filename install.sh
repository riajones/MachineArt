echo installing opencv

sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
sudo apt-get install python3.5-dev
python3.5-config --includes
-I/usr/include/python3.5m -I/usr/include/x86_64-linux-gnu/python3.5m
sudo cp /usr/include/x86_64-linux-gnu/python3.5m/pyconfig.h /usr/include/python3.5m/
mkdir OpenCV-tmp
cd OpenCV-tmp
git clone https://github.com/Itseez/opencv.git
sudo apt install cmake
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ../opencv
make
sudo make install

cd ..
python3.5 testCV2.py


echo Installing mongodb

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo apt install mongodb-clients
cd /lib/systemd/system/
sudo subl mongod.service

systemctl daemon-reload
systemctl start mongod
systemctl enable mongod

sudo apt-get install lsof
sudo lsof -i :27017
read -p "Press enter to continue"



