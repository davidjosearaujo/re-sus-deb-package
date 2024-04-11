Vagrant.configure("2") do |config|
  config.vm.box = "kalilinux/rolling"

  #config.vm.provision "shell", inline: "sudo apt update && sudo apt install ghidra -y"

  config.vm.provider "virtualbox" do |v|
    v.cpus = 2
    v.memory = 2048
  end  

  if ENV['FILE'] != nil
    config.vm.provision "file", source: ENV['FILE'], destination: "/home/vagrant/imported/"+ENV['FILE']
  end

  if ENV['DIR'] != nil
    config.vm.provision "file", source: ENV['DIR'], destination: "/home/vagrant/imported"
  end

  if ENV['HEADLESS'] == "YES"
    config.vm.provider "virtualbox" do |v|
      v.gui = false
      v.cpus = 2
    end
  end
end
