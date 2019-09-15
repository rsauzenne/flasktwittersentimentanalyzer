Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/xenial64"

  config.vm.synced_folder "./src", "/home/vagrant/src"

  config.vm.network :forwarded_port, guest: 5000, host: 5000

    # run Ansible from the Vagrant VM
  config.vm.provision "ansible_local" do |ansible|
    ansible.install = true
    ansible.playbook = "deploy.yml"
  end

end
