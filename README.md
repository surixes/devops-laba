# Задание

> Необходимо развернуть микросервис на виртуальной машине (ВМ), используя систему управления конфигурациями и описать выполненные действия.
> Стек:
> VirtualBox
> Vagrant
> Ansible
> Python
> Docker

1. Для начала необходимо установить `Virtual Box` и `Vagrant`. Инструкции по установке можно найти на официальных сайтах:

   - [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
   - [Vagrant](https://developer.hashicorp.com/vagrant/install)

2. Установим нужные зависимости для работы с Vagrant:

   ```bash
   sudo apt install vagrant
   sudo apt install virtualbox
   ```

3. Инициализируем Vagrant в папке проекта:

   ```bash
   vagrant init rockylinux/9 --box-version 5.0.0
   ```

4. Нужно выбрать способ запуска микросервиса
   Если мы хотим запустить микросервис стандартно, то просто переходим к 5 пункту.
   Если мы хотим запустить микросервис в контейнере, то нужно в файле `VagrantFile` заменить строку:
   `ansible.playbook = "ansible/playbook.yml"` на `ansible.playbook = "ansible/docker.yml"`

5. Запустим развертывание сервера:

   ```bash
   vagrant up --provider=virtualbox
   ```

   После этого будет долгое разверывание и настройка виртуальной машины, и установка нужных зависимостей.

6. Для проверки работы нашего сервера, подключаемся к нему по `ssh`:

   ```bash
   vagrant ssh
   ```

7. И проверим `curl localhost:8080`
   Вывод:
   
   ```
   # HELP python_gc_objects_collected_total Objects collected during gc
   # TYPE python_gc_objects_collected_total counter
   python_gc_objects_collected_total{generation="0"} 391.0
   python_gc_objects_collected_total{generation="1"} 0.0
   python_gc_objects_collected_total{generation="2"} 0.0
   ...
   ```
