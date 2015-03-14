wget http: www.airspayce.com/mikem/bcm2835/bcm2835-1.42.tar.gz
tar zxvf bcm2835-1.42.tar.gz
cd bcm2835-1.42
./configure
make
sudo make check
sudo make install
rm bcm2835-1.42.tar.gz
rm bcm2835-1.42
