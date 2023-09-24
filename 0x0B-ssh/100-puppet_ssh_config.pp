#!/usr/bin/env bash
#set up client SSH configuration to connect a server without typing password

# Puppet manifest to configure SSH client for passwordless authentication

# Ensure the SSH client configuration directory exists
file_line {'Turn off passwd auth]':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}

file_line {'Declare identity file SSHclient configuration using private key':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}
