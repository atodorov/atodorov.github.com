---
layout: post
title: "Exploring BlackBerry 10 - Environment Variables"
date: 2013-08-05 00:20
comments: true
categories: ['blackberry']
---

Just a quick reference of environment variables as seen by the 
`BGshellPlusFree` terminal app.

{% codeblock lang:bash %}
APPCPU=
AUTOORIENTS=portrait
BASEFS=/base
BMETRICS_NAME=launcher
BOARDFILE=/base/board.tdf
BOARD_CONFIG=factory_sfi
BOOT_LOADER=RIMBOOT
BOOT_START_TIME=1375381026
CELLULAR_NET_IF_PREFIX=cellular
COVERHEIGHT=396
COVERWIDTH=334
CPU=armle-v7
DECKARD_DEBUG=0
DECKARD_DEBUG_SCRIPT=0
DISK_ALIMIT=65536
FLASHTMP=/tmp
FLASH_FONT_CFG_PATH=/etc/system/config/flash-font.cfg
FONTCONFIG_FILE=/etc/fontconfig/fonts.conf
GRAPHICS_ROOT=/usr/lib/graphics/omap4470
HEIGHT=1280
HMI_REMOTE=FALSE
HMI_VOLUME_SCALE=50
HOME=/accounts/1000/appdata/com.BGmot.BGshellPlusFree.gYABgHVtFpaI1Xhiaw0hMuCbPNk/data
IFS='   
'
IFS_BOOT_ENV=yes
KSH_VERSION='@(#)PD KSH v5.2.14 99/07/13.2'
LANG=C
LD_LIBRARY_PATH=/usr/lib/qt4/lib:app/native/lib:/usr/lib/appserv
LIBIMG_CFGFILE=/etc/system/config/img.conf
LOCFILE=/usr/share/locale/locale.file
LOGDIR=/var/log
MAILCHECK=600
MHSDEVICE=tiw_sap0
MIN_VALID_DATE=200905010000.00
MIN_VALID_DATE_SEC=1241136000
MM_INIT=/base/lib/dll/mmedia
NET_PPS_ROOT=/pps/services/networking
OLDPWD=/accounts/1000
OPTIND=1
ORIENTATION=0
OS_VERSION=10.1.0.1720
PATH=app/native:/base/bin:/base/usr/bin:/base/sbin:/base/usr/sbin:/base/usr/photon/bin:/base/scripts:/radio/bin:/radio/usr/bin:/radio/sbin:/radio/usr/sbin:/radio/scripts:/proc/boot:/base/bin:/base/sbin:/base/usr/bin:/base/usr/sbin
PERIMETER=personal
PERIMETER_HOME=/accounts/1000
PERSISTENCE_DATA=/
PHFONT=/dev/phfont
PHKSCOPE=1
PHOTON=/dev/photon
PLATFORM=London
PLATFORM_CLASS=phone
PLATFORM_FAMILY=
PLATFORM_FAMILY_LC=
PLATFORM_LOWERCASE=london
PLATFORM_REV=08
PPID=19493019
PPSDIR=/pps
PS1='$ '
PS2='> '
PS3='#? '
PS4='+ '
PWD=/accounts/1000/appdata/com.BGmot.BGshellPlusFree.gYABgHVtFpaI1Xhiaw0hMuCbPNk/data
QML_IMPORT_PATH=/base/usr/lib/qt4/imports
QT_LIB_PATH=/base/usr/lib/qt4/lib
QT_PLUGIN_PATH=/base/usr/lib/qt4/plugins
QT_QPA_PLATFORM=blackberry
RADIOBOARDFILE=/radio/radio.tdf
RADIOFS=/radio
RADIO_BOARD_CONFIG=m5730
RADIO_NET_IF_LIST=' cellular0 cellular1 cellular2 cellular3 cellular4'
RADIO_VERSION=10.1.0.1721
RAMSIZE=1G
RANDOM=18235
ROOTFS=/
ROTATION=top_up
RTC_CLOCK_OPTS=
RTC_CLOCK_TYPE=
RTC_OPTS=
SANDBOX=/accounts/1000/appdata/com.BGmot.BGshellPlusFree.gYABgHVtFpaI1Xhiaw0hMuCbPNk
SECONDS=2167
SHELL
STDIO_DEFAULT_BUFSIZE=8192
SYSNAME=nto
TEMP=/accounts/1000/appdata/com.BGmot.BGshellPlusFree.gYABgHVtFpaI1Xhiaw0hMuCbPNk/tmp
TERM=ansi
TMOUT=0
TMP=/accounts/1000/appdata/com.BGmot.BGshellPlusFree.gYABgHVtFpaI1Xhiaw0hMuCbPNk/tmp
TMPDIR=/accounts/1000/appdata/com.BGmot.BGshellPlusFree.gYABgHVtFpaI1Xhiaw0hMuCbPNk/tmp
WIDTH=768
WIFIDEVICE=tiw_sta0
WLANCHP=ti1283
WLANDEV=london
WLANDRV=mcp33
WLANSUPPVER=08
_=set
uname_m=OMAP4470_ES1.0_HS_London_Rev:08
{% endcodeblock %}
