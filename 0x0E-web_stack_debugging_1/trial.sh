#!/usr/bin/env bash

# Check if the server is running on port 80
if ! ss -l -p tcp -n | grep :80; then
  # Start the server
  systemctl start nginx
fi

if ! grep -q "listen 80;" /etc/nginx/nginx.conf; then
  # Nginx is not configured to listen on port 80, so add the line to the configuration file
  echo "listen 80;" >> /etc/nginx/nginx.conf
fi

service nginx restart
