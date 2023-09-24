# create a file in temp and give permissions, add data, owner and group
file {'/tmp/school':
    ensure  => present,
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
}
