fat16 2gb
fat32 32gb 8tb 4gb
NTFS 16EB 2TB

EfsTools.exe uploadDirectory -i SKTLGU -o / -v

setprop sys.usb.config diag,diag_mdm,diag_mdm2,qdss,qdss_mdm,serial_cdev,dpl,rmnet,adb


EfsTools.exe uploadDirectory -i SKT -o / -v

adb shell settings put secure sysui_rounded_size 1

adb shell settings put secure sysui_rounded_content_padding 5


*#*#4636#*#*
