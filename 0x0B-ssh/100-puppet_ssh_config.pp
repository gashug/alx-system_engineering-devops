# Puppet manifest to configure SSH client

file { '/etc/ssh/ssh_config':
  ensure => file,
}

# Ensure SSH client uses the private key ~/.ssh/school
file_line { 'Set IdentityFile':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile\s+~/.ssh/school$',
}

# Ensure SSH client refuses to authenticate using a password
file_line { 'Disable PasswordAuthentication':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^#?PasswordAuthentication\s+no$',
}
