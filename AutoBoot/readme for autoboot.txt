# to make a file bootable here  you need to follow these simple steps 
# to make this work please ensure you have a file called autostart.py  saved home/pi/autostart.py

#Step-1 copy paste the below code it will create a file autostart.service and open it in nano
sudo nano /etc/systemd/system/autostart.service

#Step2 -  copy pase the below code in autostart.service 

[Unit]
Description=Autostart Robot Listener
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/autostart.py
WorkingDirectory=/home/pi
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target

# Step 3 
Save with Ctrl + O, press Enter, and exit Nano with Ctrl + X.

# Step-4 Reload systemd to recognize the new service:
sudo systemctl daemon-reload

# Step-5 Enable it so it runs automatically on every boot:
sudo systemctl enable autostart.service

