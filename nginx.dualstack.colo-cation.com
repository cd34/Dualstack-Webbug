server {
    listen   66.244.147.43:81;
    listen   66.244.147.44:81;
    listen   66.244.147.46:80;
    listen   [2604:3500:1:78:4646:4646:4646:4646]:80; 
    listen   [2604:3500:1:78:6666:6666:6666:6666]:80;
    server_name  dualstack.colo-cation.com ipv4.colo-cation.com ipv6.colo-cation.com;
    access_log /var/log/nginx/dualstack.colo-cation.com-access.log;

    location ~* (css|js|png|jpe?g|gif|ico|swf|flv)$ {
        expires max;
    }

    gzip on;
    gzip_min_length 500;
#    gzip_types text/plain application/xml text/html text/javascript;
    gzip_disable "MSIE [1-6]\.";

    location ^~ /favicon.ico {
    	root   /var/www/sflhackers.com/static/;
    }

    location / {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://dualstack_tornado;
    }

}
