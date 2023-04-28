# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/var/www/html/index.nginx-debian.html':
  content => "<html><body>Hello World!</body></html>",
}

file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;
                root /var/www/html;
                index index.nginx-debian.html;
                server_name _;
                location /redirect_me {
                  return 301 https://twitter.com/jdrestre;
                }
              }",
}

# Enable the site and restart Nginx
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => File['/etc/nginx/sites-enabled/default'],
}
