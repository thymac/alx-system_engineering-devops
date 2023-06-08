# Fixes a faulty WordPress site
exec { 'fix-wordpress':
  command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/ /var/www/html/wp-settings.php && service apache2 restart',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}

