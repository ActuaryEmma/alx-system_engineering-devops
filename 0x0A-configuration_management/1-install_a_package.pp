# install flask(2.1.0) from pip3
package {'python3':
  ensure => installed,
}
package {'python3-pip':
  ensure => installed,
}
# command - specifies the command to be used to install flask
# path - specifies an array of dir where puppet should look for executable
# spefied in command
# unless - check if Flask is installed otherewise it installs
exec {'flask':
  command => 'pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => 'pip3 show Flask',
}
