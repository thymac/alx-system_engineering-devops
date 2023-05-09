#7-puppet_install_nginx_web_server.pp

#Install Nginx package
package { 'nginx':
  ensure => installed,
}

#Configure Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

#Configure Nginx virtual host
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => "
    server {
      listen 80;
      server_name _;
      root /var/www/html;
      index index.html;

      location / {
        return 301 http://\$host/redirect_me;
      }

      location /redirect_me {
        return 301 http://\$host/hello;
      }

      location /hello {
        echo 'Hello World!';
      }
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
