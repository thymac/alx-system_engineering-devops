class nginx_hello_world {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => "Hello World!\n",
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
      server {
        listen 80 default_server;
        listen [::]:80 default_server;
        return 301 \"https://$server_name$request_uri\";
      }

      server {
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;
        ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
        ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;
        root /var/www/html;
        index index.html;
        server_name _;
        location /redirect_me {
          return 301 \"https://$server_name/\";
        }
        location / {
          try_files $uri $uri/ =404;
        }
      }
    ",
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
  }

  exec { 'nginx-reload':
    command     => '/usr/sbin/service nginx reload',
    refreshonly => true,
  }
}

include nginx_hello_world
