# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define a custom fact to retrieve the hostname
facts::custom_fact { 'hostname_fact':
  fact_source => 'hostname',
}

# Configure Nginx with the custom HTTP response header
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
}
