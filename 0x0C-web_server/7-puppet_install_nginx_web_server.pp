# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  content => template('nginx.conf.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['nginx'],
}

# Create custom 404 page
file { '/usr/share/nginx/html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Redirect /redirect_me to /new_location with a 301 redirect
nginx::resource::location { 'redirect_me':
  ensure    => present,
  location  => '/redirect_me',
  content   => 'return 301 /new_location;',
  server    => 'localhost',
  server_ip => '127.0.0.1',
  require   => File['/etc/nginx/sites-available/default'],
}
