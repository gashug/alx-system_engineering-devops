file { '/etc/ssh/sshd_config':
  ensure  => file,
  content => epp('ssh/sshd_config.epp'),
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['openssh-server'],
  notify  => Service['sshd'],
}

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => epp('ssh/ssh_config.epp'),
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['openssh-client'],
}
