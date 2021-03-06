Use build_config.sh from fedora kernel spec repo:

$ wget https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/linux-5.6.19.tar.gz
$ wget https://cdn.kernel.org/pub/linux/kernel/projects/rt/5.6/older/patch-5.6.19-rt111.patch.gz
$ tar xvfz linux-5.6.19.tar.gz
$ gunzip patch-5.6.19-rt11.patch.gz
$ cd linux-5.6.19
$ patch -p1 < ../patch-5.6.19-rt11.patch

$ git clone https://src.fedoraproject.org/rpms/kernel.git
$ cd kernel
$ git switch f32
$ ./build_config.sh kernel-5.6.19

Copy kernel-5.6.19-x86_64.config as '.config' in the linux kernel source directory.

$ make xconfig

Since 5.6.*: check General setup -> Configure standard kernel features (expert users). This will toogle the "Fully preemptible kernel).

Enable CONFIG_PREEMPT_RT_FULL (menu General setup -> Preemption model -> Fully preemptible kernel).
Enable CONFIG_HZ_1000 (menu Processor type and features -> Timer frequency -> 1000 Hz).

Save the configuration file.

Copy back .config file into kernel-config-5.16.

To clean-up the boot menu:

$ grub2-mkconfig -o /boot/grub2/grub.cfg
