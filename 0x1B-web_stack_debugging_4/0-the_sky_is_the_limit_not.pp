#change ULIMIT
exec { 'Change ULIMIT':
<<<<<<< HEAD
  command  => 'echo "ULIMIT=\"-n 25000\"" > /etc/default/nginx && sudo service nginx restart',
  provider => shell,
=======
  command => 'sudo sed -i "s/^ULIMIT=\"-n = 15\"/ULIMIT=\"-n 2500\"/" /etc/default/nginx && sudo service nginx restart',
  path    => shell,
>>>>>>> b2af7950bd0996114633e7c0e77871eab2dd6ab9
}
