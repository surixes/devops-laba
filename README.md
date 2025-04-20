# Задание

> Необходимо развернуть микросервис на виртуальной машине (ВМ), используя систему управления конфигурациями и описать выполненные действия.

1. Для начала необходимо установить `Virtual Box` и `Vagrant`. Инструкции по установке можно найти на официальных сайтах:
   - [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
   - [Vagrant](https://developer.hashicorp.com/vagrant/install)

2. Будем использовать ОС `Rocky Linux`, которую можно скачать по [ссылке](https://rockylinux.org/ru-RU/download)

3. Установим нужные зависимости для работы с Vagrant:
   ```bash
   sudo apt install vagrant Vagrant
   sudo apt install virtualbox
   ```
    # хз надо ли (sudo apt install qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils)

3. Инициализируем Vagrant в папке проекта:
   ```bash
   vagrant init rockylinux/9 --box-version 5.0.0
   ```
    Это создаст файл `Vagrantfile`, в котором нужно настроить параметры виртуальной машины.

4. Настроим Vagrantfile:
   ```ruby
   Vagrant.configure("2") do |config|
   config.vm.box = "rockylinux/9"
   config.vm.box_version = "5.0.0"
   config.vm.network "forwarded_port", guest: 8080, host: 8080

      config.vm.provider "virtualbox" do |vb|
         vb.name = "microservice1"
         vb.memory = "1024"
         vb.cpus = 1
      end

      config.vm.provision "ansible" do |ansible|
         ansible.playbook = "provision.yml"
         ansible.compatibility_mode = "2.0"
      end
   end
   ```

5. Установим Ansible:
   ```bash
   sudo apt install ansible
   ```

6. Создадим папку `ansible` и файл `playbook.yml`:
   ```bash
   mkdir ansible
   cd ansible
   touch playbook.yml
   ```