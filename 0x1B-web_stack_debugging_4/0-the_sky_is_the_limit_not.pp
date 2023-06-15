# Fixing the issue of failed requests by modifying the ULIMIT in the /etc/default/nginx file.

exec { 'Change ULIMIT':
  command => 'sudo sed -i "s/^ULIMIT=\"-n = 15\"/ULIMIT=\"-n 2500\"/" /etc/default/nginx && sudo service nginx restart',
  path    => shell,
}

