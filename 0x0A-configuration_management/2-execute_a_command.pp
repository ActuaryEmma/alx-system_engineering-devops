# kills a proocess named killmenow
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
