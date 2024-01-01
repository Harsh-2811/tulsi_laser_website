python3 manage.py collectstatic
PID=$(systemctl show --value -p MainPID gunicorn.service) && sudo kill -HUP $PID
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx

