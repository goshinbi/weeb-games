echo -e " \e[32m----> installing pip3, and nginx \e[0m"
sudo apt-get install -y python3-pip nginx
echo -e " \e[32m----> installing hug and gunicorn \e[0m"
sudo pip3 install hug
sudo pip3 install gunicorn
echo -e " \e[32m----> make weebGames.sh executable \e[0m"
sudo chmod +x weebGames.sh
echo -e " \e[32m----> start gunicorn \e[0m"
./weebGames.sh
echo -e " \e[32m----> placing the nginx.conf file in /etc/nginx.conf \e[0m"
sudo mv nginx.conf /etc/nginx/nginx.conf
echo -e " \e[32m----> restart nginx \e[0m"
sudo service nginx stop
sudo service nginx start
