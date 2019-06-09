title: Saltstack Orchestration Testing
date: 2019-06-08
category: saltstack
slug: saltstack-orchestration-testing
tags: salt, qemu, devops
summary: Testing Saltstack orchestration

### Simple Setup 

This simple setup defines the initial POC for this work.  The following items must exist:

1 - Default Qemu image
2 - Socket networking for qemu configured
3 - User mode (SLIRP) networking for qemu configured
4 - Entropy device passthru active in qemu? (see virtio section of qemu manual)
5 - Salt minion already installed in qemu image

### Qemu commands 

The following will be translated to python for use with pytest

```
# Test system1 mcast socket
qemu-system-x86_64 -daemonize \
-display gtk \
-m 512 \
-enable-kvm \
-device e1000,netdev=n0,mac=52:54:00:12:34:56 \
-netdev user,id=n0,hostfwd=tcp::1111-:22 \
-device e1000,netdev=n1,mac=52:54:00:12:34:57 \
-netdev socket,id=n1,mcast=230.0.0.1:1234,localaddr=127.0.0.1 \
-device virtio-rng-pci \
-device virtio-scsi-pci,id=scsi \
-device scsi-hd,drive=drive0 \
-drive if=none,id=drive0,snapshot=on,file=/var/lib/libvirt/images/centos7_test.qcow2

# Test system2 mcast socket
qemu-system-x86_64 -daemonize \
-display gtk \
-m 512 \
-enable-kvm \
-device e1000,netdev=n2,mac=52:54:00:12:34:58 \
-netdev user,id=n2,hostfwd=tcp::2222-:22 \
-device e1000,netdev=n3,mac=52:54:00:12:34:59 \
-netdev socket,id=n3,mcast=230.0.0.1:1234,localaddr=127.0.0.1 \
-device virtio-rng-pci \
-device virtio-scsi-pci,id=scsi \
-device scsi-hd,drive=drive0 \
-drive if=none,id=drive0,snapshot=on,file=/var/lib/libvirt/images/centos7_test.qcow2

# Test system3 mcast socket
qemu-system-x86_64 -daemonize \
-display gtk \
-m 512 \
-enable-kvm \
-device e1000,netdev=n4,mac=52:54:00:12:34:60 \
-netdev user,id=n4,hostfwd=tcp::3333-:22 \
-device e1000,netdev=n5,mac=52:54:00:12:34:61 \
-netdev socket,id=n5,mcast=230.0.0.1:1234,localaddr=127.0.0.1 \
-device virtio-rng-pci \
-device virtio-scsi-pci,id=scsi \
-device scsi-hd,drive=drive0 \
-drive if=none,id=drive0,snapshot=on,file=/var/lib/libvirt/images/centos7_test.qcow2
```

### Qemu setup 

Once the images are booted, networking needs to be configured on the guests to allow connectivity between them.

Host 1 (master): 
```
nmcli con mod "Wired connection 2" ipv4.addresses "10.0.200.101/24"
nmcli con mod "Wired connection 2" ipv4.method manual

Git setup required
```

Host 2 (minion):
```
nmcli con mod "Wired connection 2" ipv4.addresses "10.0.200.102/24"
nmcli con mod "Wired connection 2" ipv4.method manual

echo "10.0.200.101 cicdsalt" >> /etc/hosts
echo "minion0" > /etc/salt/minion_id
systemctl restart salt-minion
```

Host 3 (minion):
```
nmcli con mod "Wired connection 2" ipv4.addresses "10.0.200.103/24"
nmcli con mod "Wired connection 2" ipv4.method manual

echo "10.0.200.101 cicdsalt" >> /etc/hosts
echo "minion1" > /etc/salt/minion_id
systemctl restart salt-minion
```

SSH to guests via `ssh -p1111 kitchen@localhost -o StrictHostKeyChecking=no`


