---
layout: post
title: "Exploring BlackBerry 10 - Application Security Model"
date: 2013-08-04 00:02
comments: true
categories: ['BlackBerry']
---

BlackBerry 10 OS application security model is enforced by two major components:
[app permissions](https://developer.blackberry.com/native/documentation/bb10/com.qnx.doc.native_sdk.devguide/com.qnx.doc.native_sdk.devguide/topic/c_appfund_accessing_restricted_functionality.html)
and
[filesystem access privileges](https://developer.blackberry.com/native/documentation/bb10/com.qnx.doc.native_sdk.devguide/com.qnx.doc.native_sdk.devguide/topic/accessible_folders.html).

Also it looks like that each app is assigned a separate group id. Below is a listing
of my currently installed apps as seen from `devuser`. An application can't execute
another apps (e.g. exec) as far as I can see. Not possible with the shell app either.

I think I will have to
bundle all command line tools together with a shell into a single app so the shell
is able to invoke any of the commands that are not system standard. I'm not liking this
very much!


$HOME is inside the app space too :(. See my other post about 
[environment variables](/blog/2013/08/05/exploring-blackberry-10-environment-variables/).



{% codeblock lang:bash %}
$ pwd
/accounts/1000

$ ls -l appdata/ appserv/

appdata/:
total 552
drwxr-x---   6 apps      10143          4096 Jul 25 16:22 com.BGmot.BGshellPlusFree.gYABgHVtFpaI1Xhiaw0hMuCbPNk
drwxr-x---   6 apps      10141          4096 Jul 20 21:34 com.catikkas.jenkins10.gYABgOZDFJiaJUObnHnYGyedaJE
drwxr-x---   6 apps      10134          4096 Jul 17 09:02 com.example.Chat_1.gYABgLTE22iUbVEQqMQWh1h8qGw
drwxr-x---   6 apps      10003          4096 Jul 13 01:56 com.foursquare.blackberry.gYABgBY3zYaCRi7CDRw5ChZRJ18
drwxr-x---   6 apps      10004          4096 Jul 12 22:26 com.linkedin.gYABgPilB6lwL6lsxmVwDOfmbO8
drwxr-x---   6 apps      10145          4096 Jul 27 22:05 com.mappau.SystemInformation.gYABgPYOA670hrzAeZ.Eg91JZFU
drwxr-x---   6 apps      100051000      4096 Jul 12 23:04 com.rim.bb.app.adobeReader.gYABgAxBqJsMx5M..e.RfW5WpTU
drwxr-x---   6 apps      10006          4096 Jul 13 00:06 com.rim.bb.app.facebook.gYABgDLo0nc9AhDgv2JAPixdyvQ
drwxr-x---   6 apps      10123          4096 Jul 23 13:32 com.rim.bb.app.newsstand.gYABgIYcPYRGuuoXUB7e7VfgiaA
drwxr-x---   6 apps      10116          4096 Jul 13 01:16 com.savvysaurus.RssSavvy.gYABgCcU_QDmZyIEIHfBoxukmi4
drwxr-x---   6 apps      100021000      4096 Jul 12 22:39 com.tcs.maps.gYABgCxm2rf5o5xfFP8dPCQnlJY
drwxr-x---   6 apps      10009          4096 Jul 12 22:18 com.twitter.gYABgMxtkHoH6S4G1_Ff5yu0E.I
drwxr-x---   6 apps      10138          4096 Jul 18 21:27 helex.NativeFlash.gYABgHc51xjJK7eHzYQIH2y6hxA
drwxr-x---   6 apps      air_services      4096 Jul 12 21:57 sys.airservices
drwxr-x---   6 apps      100131000      4096 Jul 13 02:24 sys.airtunes.gYABgCWWhIycHhiFjXeIyW1Qvpo
drwxr-x---   6 apps      10014          4096 Jul 12 23:26 sys.android.gYABgKAOw1czN6neiAT72SGO.ns
drwxr-x---   6 apps      10015          4096 Jul 12 23:26 sys.android.shell.gYABgCWpLq.7ipa6NFYT0JaLpt8
drwxr-x---   6 apps      10016          4096 Jul 12 21:58 sys.appworld.gYABgNSvaLtte_snIx7wjRsOcyM
drwxr-x---   6 apps      10017          4096 Jul 12 21:58 sys.bbm.gYABgLOJBR2Vz7FzS.kdgJchuag
drwxr-x---   6 apps      100001000      4096 Jul 12 22:24 sys.browser.gYABgJYFHAzbeFMPCCpYWBtHAm0
drwxr-x---   6 apps      10032          4096 Jul 12 23:00 sys.calculator.gYABgJidBvuZ89m_1j4PV2712.A
drwxr-x---   6 apps      10034          4096 Jul 12 23:14 sys.camera.gYABgAvGHb4h9H5WeWdjQhXgeRM
drwxr-x---   6 apps      10124          4096 Jul 17 10:45 sys.cfs.box.gYABgJKe3gZus2hhkRPM4zcarBU
drwxr-x---   6 apps      10125          4096 Jul 17 10:45 sys.cfs.dropbox.gYABgKi0Cs_hMocaoCB7UgqkaIU
drwxr-x---   6 apps      10126          4096 Jul 15 14:25 sys.cfs.webdav.todtm.gYABgGnToZvN4bqMB3xslfel.KU
drwxr-x---   6 apps      10037          4096 Jul 14 22:21 sys.chat.gYABgADt.JeweQYFvYX28P5bwu0
drwxr-x---   6 apps      10038          4096 Jul 12 23:07 sys.clock.gYABgKNXug.mDFoFoYHLmJofAts
drwxr-x---   6 apps      10039          4096 Jul 12 22:53 sys.compass.gYABgM06vW4QuahSmSW7eBlHxb4
drwxr-x---   6 apps      100101000      4096 Jul 12 22:59 sys.dxtg.launcher.gYABgHFqGG632tetjwVL_egrHHc
drwxr-x---   6 apps      100121000      4096 Jul 12 22:59 sys.dxtg.sstg.gYABgLhf.C6ER6tWA.ObKMKalQU
drwxr-x---   6 apps      100111000      4096 Aug 01 22:55 sys.dxtg.stg.gYABgKF.gjTVTclxOrZ0RRQcoTc
drwxr-x---   6 apps      100871000      4096 Jul 15 00:40 sys.dxtg.wtg.gYABgKH0JhT7tasXrfXUyNxNaew
drwxr-x---   6 apps      100431000      4096 Jul 14 23:30 sys.filepicker.gYABgBUOB4WQ4V0f7gH0kMCrcVA
drwxr-x---   6 apps      10001          4096 Jul 12 21:58 sys.firstlaunch.gYABgE1L_lY.sjW85E1SCBQsrco
drwxr-x---   6 apps      10044          4096 Jul 12 22:53 sys.games.gYABgCM5htxnRwx8VmvFMD0Hbj4
drwxr-x---   6 apps      100451000      4096 Jul 12 23:05 sys.help.gYABgPG.Su8AzxaqqONbaanIprc
drwxr-x---   6 apps      keyboard       4096 Jul 12 21:57 sys.keyboard
drwxr-x---   6 apps      100471000      4096 Jul 27 21:36 sys.mediaplayer.gYABgHtLSIC4bjdb005eaW5ixzU
drwxr-x---   6 apps      10049          4096 Jul 12 23:00 sys.mmagic.gYABgGN_jnGTnVoC_K.mfaBq87g
drwxr-x---   6 apps      nto            4096 Jul 12 21:57 sys.navigator
drwxr-x---   6 apps      100511000      4096 Jul 12 22:24 sys.notification_card.gYABgLyFNMkTny6ihJLjaG02jUU
drwxr-x---   6 apps      10052          4096 Jul 17 10:38 sys.paymentsystem.gYABgPLIJa_bijh7gGqV5LuyCK4
drwxr-x---   6 apps      100531000      4096 Jul 12 23:03 sys.perimeterbrowser.gYABgMgpl40MVrFkZvPEXRuQTGE
drwxr-x---   6 apps      10054          4096 Jul 12 22:01 sys.phone.gYABgB3m3BHdGLR4aicCyzCVsYQ
drwxr-x---   6 apps      10055          4096 Jul 15 00:42 sys.phone_settings.gYABgP8tnMCm3UDXaovgTHoEZB4
drwxr-x---   6 apps      100561000      4096 Jul 15 21:08 sys.pictureeditor.gYABgIRm37_owYKt4P0uCEhSj.o
drwxr-x---   6 apps      100571000      4096 Jul 12 22:01 sys.pictures.gYABgFZ.pCiYHqciL1zClEPjmps
drwxr-x---   6 apps      100581000      4096 Jul 15 16:29 sys.picturesviewer.gYABgFKlvDBH.tdV7sGqIDZHnNY
drwxr-x---   6 apps      10033          4096 Jul 12 22:10 sys.pim.calendar.gYABgG0xvpxP1jARa6DD5o.VL8A
drwxr-x---   6 apps      10059          4096 Jul 16 09:15 sys.pim.calendar.viewer.eventcreate.gYABgBtmuosCGVI3YO1ImfFgbgY
drwxr-x---   6 apps      100601000      4096 Jul 12 22:26 sys.pim.calendar.viewer.ics.gYABgMsLIpp41sIscDzLSeRZuIQ
drwxr-x---   6 apps      10040          4096 Jul 12 22:14 sys.pim.contacts.gYABgGsAOuzqCT1fu5Zx4sqrJdY
drwxr-x---   6 apps      100621000      4096 Jul 12 22:23 sys.pim.email.card.gYABgHLnJMGjgoIAsdeYM2JzUsU
drwxr-x---   6 apps      10063          4096 Jul 13 01:49 sys.pim.email.composer.card.gYABgGkBKIp75QI99dsGTdrb5IE
drwxr-x---   6 apps      10064          4096 Jul 12 21:58 sys.pim.messages.gYABgJ8jn83Ok_NEWYplPYozt5w
drwxr-x---   6 apps      10065          4096 Jul 12 23:00 sys.pim.remember.gYABgF9PcqaN7GRKPlDPuqOyda0
drwxr-x---   6 apps      100671000      4096 Jul 12 23:03 sys.printoutstogo.gYABgPMP3nxNZlNieZUDetUiQio
drwxr-x---   6 apps      10068          4096 Jul 13 13:26 sys.search.gYABgPp5WMkB_07CE6wzbflslRQ
drwxr-x---   6 apps      10069          4096 Jul 12 22:02 sys.settings.gYABgFXZghhSmuJ6oBTACT1DwpQ
drwxr-x---   6 apps      10070          4096 Jul 12 22:01 sys.setupbuffet.gYABgCbSxd9WrFvFV8sJDoI7tlE
drwxr-x---   6 apps      10071          4096 Jul 16 09:18 sys.simtoolkit_ui_app.gYABgNsM_6zxbmp668bBbRexQiA
drwxr-x---   6 apps      10072          4096 Jul 12 23:05 sys.smarttags.gYABgNvWPl0Fpbeva2LkhFplXYY
drwxr-x---   6 apps      10073          4096 Jul 12 22:04 sys.socialconnect.facebook.gYABgPNVFtmlTnTGF_U0dFfTvgQ
drwxr-x---   6 apps      10074          4096 Jul 12 22:26 sys.socialconnect.linkedin.gYABgCUcHQzQnN9ZnpyVppfXHEQ
drwxr-x---   6 apps      10075          4096 Jul 12 22:18 sys.socialconnect.twitter.gYABgB2cPvkIcyPxzQPSK9Jx89U
drwxr-x---   6 apps      10079          4096 Jul 23 13:27 sys.vad.gYABgJPtEgEJTVKTkyq7_BalYto
drwxr-x---   6 apps      100811000      4096 Jul 12 22:37 sys.videoplayer.gYABgEydozZr9q.ClZkrItC9LMM
drwxr-x---   6 apps      10085          4096 Jul 12 22:47 sys.weather.gYABgKOf0EhVEWtCxrbBQ00sPSg
drwxr-x---   6 apps      10086          4096 Jul 12 21:58 sys.zbbiocm.gYABgDZcy0Sq5cvKqkoZgR3qJps

appserv/:
total 0
dr-xr-xr-x   2 root      nto               0 Aug 04 00:03 sys.cfs.box.gYABgJKe3gZus2hhkRPM4zcarBU
dr-xr-xr-x   2 root      nto               0 Aug 04 00:03 sys.cfs.dropbox.gYABgKi0Cs_hMocaoCB7UgqkaIU
dr-xr-xr-x   2 root      nto               0 Aug 04 00:03 sys.cfs.webdav.todtm.gYABgGnToZvN4bqMB3xslfel.KU
{% endcodeblock %}
