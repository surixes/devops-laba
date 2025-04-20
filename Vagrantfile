# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "rockylinux/9"
  config.vm.box_version = "5.0.0"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", 
    guest: 22, 
    host: 2222,
    id: "ssh",
    auto_correct: true

  config.vm.provider "virtualbox" do |vb|
    vb.name = "metrics-server-vm"
    vb.memory = "2048"
  end

  # config.vm.provision "ansible" do |ansible|
  #   ansible.playbook = "ansible/playbook.yml"
  #   ansible.inventory_path = "ansible/inventory.ini"
  #   ansible.compatibility_mode = "2.0"
  # end

  # config.vm.provision "docker" do |d|
  #   d.build_image <<-DOCKERFILE
  #     FROM python:3.9
  #     RUN pip install ansible
  #   DOCKERFILE
  # end

  config.vm.provision "shell", inline: <<-SHELL
    # Установка EPEL и Ansible
    sudo dnf install -y epel-release
    sudo dnf install -y ansible 
    
    # Проверка версии Ansible
    echo "Ansible version:"
    ansible --version

    # Установка Docker
    sudo dnf install -y dnf-plugins-core
    sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    sudo dnf install -y docker-ce docker-ce-cli containerd.io
    sudo systemctl enable --now docker
    
    # Добавление пользователя в группу docker (требует перелогина)
    sudo usermod -aG docker vagrant
    newgrp docker 2>/dev/null || true  # Применяем изменения группы без перезагрузки

    # Запуск playbook с явным указанием пути
    echo "Starting Ansible playbook..."
    /usr/bin/ansible-playbook \
      /vagrant/ansible/playbook.yml \
      -i /vagrant/ansible/inventory.ini \
      -e "ansible_user=vagrant"
  SHELL

end
