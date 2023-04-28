#Install Nginx
package { 'nginx':
ensure => 'installed',
}

#Create custom HTTP header response
file { '/var/www/html/index.nginx-debian.html':
content => 'Holberton School',
}

#Configure redirect
file_line { 'redirect config':
path => '/etc/nginx/sites-enabled/default',
line => 'rewrite ^/redirect_me https://twitter.com/jdrestre permanent;',
}

#Create custom 404 error page
file { '/usr/share/nginx/html/page_error_404.html':
content => 'Ceci n'est pas une page',
}

#Configure 404 error page
file_line { '404 config':
path => '/etc/nginx/sites-enabled/default',
line => 'error_page 404 /page_error_404.html;',
}

#Configure location for 404 error page
file_line { 'location config':
path => '/etc/nginx/sites-enabled/default',
line => 'location = /page_error_404.html { root /usr/share/nginx/html; internal; }',
}

#Restart Nginx service
service { 'nginx':
ensure => 'running',
enable => 'true',
require => [Package['nginx'], File['/var/www/html/index.nginx-debian.html'], File_line['redirect config'], File['/usr/share/nginx/html/page_error_404.html'], File_line['404 config'], File_line['location config']],
}
