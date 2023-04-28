# Install Nginx web server
class nginx {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  # Set up custom HTTP header response
  file { '/usr/share/nginx/html/page_error_404.html':
    ensure  => 'present',
    content => 'Ceci n\'est pas une page',
    require => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'present',
    content => template('nginx/default.erb'),
    require => Service['nginx'],
  }
}

class { 'nginx': }

# Set up 301 redirect
nginx::resource::location { 'redirect_me':
  location   => '^/redirect_me$',
  ensure     => 'present',
  destination => 'https://twitter.com/jdrestre',
  status     => '301',
}
