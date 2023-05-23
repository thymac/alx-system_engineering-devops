exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/nginx.conf':
  ensure   => present,
  content  => "http {\n\tadd_header Y-Served-By \"${hostname}\";",
  match    => 'http {',
  notify   => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}

