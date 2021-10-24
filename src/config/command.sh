sudo rm /etc/nginx/sites-enabled/astrolabium_viber_bot
sudo rm /etc/systemd/system/astrolabium_viber_bot.service
sudo ln -s /home/jurgeon/projects/astrolabium/astrolabium_viber_bot/src/config/astrolabium_viber_bot        /etc/nginx/sites-enabled/
sudo ln -s /home/jurgeon/projects/astrolabium/astrolabium_viber_bot/src/config/astrolabium_viber_bot.service /etc/systemd/system/
sudo nginx -s reload
sudo systemctl enable astrolabium_viber_bot
sudo systemctl start astrolabium_viber_bot
sudo systemctl restart astrolabium_viber_bot
sudo systemctl daemon-reload
sudo certbot --nginx -d astrolabiumviberbot.starway.agency
sudo certbot renew --dry-run