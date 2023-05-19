#  manifest that kills a process named killmenow
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin/',
  logoutput   => true,
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}

