# Increase the limit of nginx processes
exec { 'enlarge_processes':
    command  => 'sed -i "s/worker_processes 4;/worker_processes 100;/g /etc/nginx/nginx.conf"; sudo service nginx restart',
    provider => 'shell',
}
