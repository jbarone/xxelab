# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = true

  #config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder "penlab", "/app"
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -yq \
        apache2 \
        libapache2-mod-php5 \
        php5-gd \
        php5-curl \
        php-pear \
        php5-dev \
        libcurl4-openssl-dev \
        expect-dev \
        php5-sqlite \
        php-apc && \
        pecl install expect && \
        echo "extension=expect.so" >> /etc/php5/apache2/php.ini && \
        rm -rf /var/lib/apt/lists/*
    echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
        sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g" /etc/php5/apache2/php.ini
    rm -fr /var/www/html && ln -s /app /var/www/html
    chown www-data:www-data /app -R
    service apache2 restart
  SHELL
end
