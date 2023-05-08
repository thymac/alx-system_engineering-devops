exec { 'killmenow':
  command     => 'pkil -f killmenow',
  path        => 'usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}
