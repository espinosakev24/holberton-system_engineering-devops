# Killing a process with puppet command
exec { 'killmenow':
  command => 'pkill -f killnow',
  path    => ['usr/bin'],
}
