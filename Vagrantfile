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

  config.vm.provision "shell", inline: <<-SHELL
    sudo dnf install -y python3
  SHELL

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "ansible/playbook.yml"
  end

end
