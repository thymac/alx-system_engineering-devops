server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location /redirect_me {
        return 301 https://twitter.com/jdrestre;
    }

    location / {
        add_header Content-Type "text/html";
        return 200 "Hello World!";
    }

    error_page 404 /page_error_404.html;
    location = /page_error_404.html {
        root /usr/share/nginx/html;
        internal;
    }
}
