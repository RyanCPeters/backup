class profile::base {
  $user = 'vagrant'

  user { $user:
    ensure => present
  }

  file { "/home/${user}":
    ensure => directory,
    owner  => $user,
    mode   => "0750"
  }

  file { "/home/${profile::base::user}/.bashrc":
    ensure => present,
    owner  => $profile::base::user,
    mode   => "0644",
    source => 'puppet:///modules/profile/bashrc',
  }

  file { '/root/.ssh':
    ensure => directory,
    owner => 'root',
    mode => '700'
  }

  file { '/root/.ssh/authorized_keys':
    ensure => present,
    owner => 'root',
    mode => '600',
    source => 'puppet:///modules/profile/id_rsa.pub'
  }

  file { '/root/.ssh/id_rsa':
    ensure => present,
    owner => 'root',
    mode => '600',
    source => 'puppet:///modules/profile/id_rsa'
  }

  file { "/home/${profile::base::user}/.my.cnf":
    ensure => present,
    owner  => $profile::base::user,
    mode   => "0600",
    source => 'puppet:///modules/profile/.my.cnf'
  }

  file { "/root/.my.cnf":
    ensure => present,
    owner  => 'root',
    mode   => "0600",
    source => 'puppet:///modules/profile/.my.cnf'
  }

  $packages = [
    'vim',
    'netcat',
    'percona-server-client-5.7',
    'percona-server-server-5.7',
    'percona-toolkit',
    'percona-xtrabackup-24',
    'python3.9-dev', 'python3.9', 'python', 'virtualenv',
    'gcc',
    'zlibc',
    'openssl',
    'docker.io',
    'strace',
    'jq',
    'make'
  ]

  package { $packages:
    ensure  => installed,
  }

  service { 'docker':
    ensure => running,
    enable => true,
    require => [
      Package['docker.io'],
    ]
  }

  exec { 'net.ipv4.ip_forward':
    path    => '/bin:/sbin',
    command => '/sbin/sysctl net.ipv4.ip_forward=1',
    unless  => 'sysctl net.ipv4.ip_forward | grep "net.ipv4.ip_forward = 1"'
  }

  file { "/etc/twindb":
    ensure => directory,
    owner  => 'root',
    mode   => "0700"
  }

  file { "/etc/twindb/twindb-backup.cfg":
    ensure  => present,
    owner   => 'root',
    mode    => "0600",
    source  => 'puppet:///modules/profile/twindb-backup.cfg',
    require => File['/etc/twindb']
  }

}
