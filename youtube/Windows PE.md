# Windows PE

Already: HBCD Hiren Boot CD

[https://www.hirensbootcd.org/download/](https://www.hirensbootcd.org/download/)

[https://www.hirensbootcd.org/old-versions/](https://www.hirensbootcd.org/old-versions/)

[https://www.comss.ru/page.php?id=4425](https://www.comss.ru/page.php?id=4425)

To create a CMD based PE: (Windows 10) [https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-intro](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-intro)

instruction:[https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/download-winpe--windows-pe](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/download-winpe--windows-pe)

[https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive)

Windows ADK installed

WindowsPE add-on 

cmd: copype amd64/x86/arm <directory>

Win PE Optional Components[https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-add-packages--optional-components-reference](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-add-packages--optional-components-reference)

cmd: MakeWinPEMedia

Usable normal PE:

[https://www.tenforums.com/software-apps/117664-win10xpe-build-your-own-rescue-media.html](https://www.tenforums.com/software-apps/117664-win10xpe-build-your-own-rescue-media.html)

Windows PE (Windows 7)

[https://www.youtube.com/watch?v=2qb5jGaKnsw](https://www.youtube.com/watch?v=2qb5jGaKnsw)

1. Download Windows AIK

[https://www.microsoft.com/en-us/download/details.aspx?id=5753](https://www.microsoft.com/en-us/download/details.aspx?id=5753)
2. Install Windows AIK (Burn to CD or Unpack to Desktop) Run StartCD.exe
3. Click Windows AIK Setup
4. Now Create WinPE (Open Microsoft Windows AIK, click Deployment Tools Command Prompt Right click it and Run as Admisitrator)
5. Now type: copype amd64 or x86 c:\winpe
6. Check c: root for winpe folder
7. Now type copy c:\winpe\winpe.wim c:\winpe\iso\sources\boot.wim
8. Now prepare your flash drive using Diskpart.exe
9. Open Run and type Diskpart
10. Type list disk
11. Type select disk 1 or usb drive number
12. Type clean
13. Type create partition primary
14. Type active
15. Type format fs=ntfs quick label=winpe
16. Type assign
17. Type exit
18. Open command prompt
19. Type xcopy c:\winpe\iso\*.* f:\ /e
20. f is drive letter of usb or copy and paste to pen drive
21. Create iso of your winpe type: oscdimg – n –bc:\winpe\etfsboot.com c:\winpe\iso c:\winpe\winpe.iso
22. Type exit
23. Now burn your disc