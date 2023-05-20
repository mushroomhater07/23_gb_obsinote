opencore github download `iso.gz`
2. download any macOS iso
3.  Create VM
4. Default GPU/ q35 machine / UEFI/ Add UEFI Disk(another LVM) / EFI Storage
5. EFI pre enroll key untick
6. Disks bus = VirtIO Block 0
7. CPU Penryn
8. Network VMWare
9. Add CDROM/DVD macOS iso
10.  `nano /etc/pve/qemu-server/100.conf`
11.  ide0: xxxxxxxxxxxx.iso,cache=unsafe,size=192831029373847M
12. ide2:                        .iso,cache=unsafe,size
13. Bottom line: add intel/AMD cpu args
14. Start machine UEFI shell
15. `Shell> fs0:\System\Library\CoreServices\boot.efi
16. 