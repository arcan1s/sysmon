#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import argparse,  os,  shutil

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Create and install Kit SysMon by arcanis')
    
    parser.add_argument('-v','--version', dest='ver',
            help = 'Show version and exit',
            action='store_true', default = False)
    
    parser.add_argument('-l','--lang', dest='lang',
            help = 'Language (eng/rus/ger/fr). Default is "eng"',
            action='store', default = 'eng')
    
    parser.add_argument('-d','--directory', dest='dir',
            help = 'Path to install. Default is current directory',
            action='store', default = False)
    
    parser.add_argument('-m','--mark', dest='mark',
            help = 'Mark for directory (if you wish use more than one copy of Kit SysMon). Directory must be enable. Default is False',
            action='store', default = False)

    parser.add_argument('-s','--startup', dest='startup',
            help = 'Enable autostart on KDE4 startup. It must be something like "~/,kde4/Autostart". Default is False',
            action='store', default = False)
    
    parser.add_argument('-ch','--colorhead', dest='colhead',
            help = 'Color for headlines. Format "RRR,GGG,BBB", for example "255,255,255". Default is "70,216,29"',
            action='store', default = '70,216,29')
    
    parser.add_argument('-cm','--colormain', dest='colmain',
            help = 'Color for main text. Format "RRR,GGG,BBB", for example "255,255,255". Default is "255,255,255"',
            action='store', default = '255,255,255')
    
    parser.add_argument('-c1','--color1', dest='col1',
            help = 'Color for CPU0, and DL-speed. Format "RRR,GGG,BBB", for example "255,255,255". Default is "53,229,82"',
            action='store', default = '53,229,82')
    
    parser.add_argument('-c2','--color2', dest='col2',
            help = 'Color for CPU1, and UL-speed. Format "RRR,GGG,BBB", for example "255,255,255". Default is "255,0,0"',
            action='store', default = '255,0,0')
    
    parser.add_argument('-c3','--color3', dest='col3',
            help = 'Color for CPU2. Format "RRR,GGG,BBB", for example "255,255,255". Default is "0,128,255"',
            action='store', default = '0,128,255')
    
    parser.add_argument('-c4','--color4', dest='col4',
            help = 'Color for CPU3. Format "RRR,GGG,BBB", for example "255,255,255". Default is "253,233,16"',
            action='store', default = '253,233,16')
    
    parser.add_argument('-si','--sysinfo', dest='sysinfo',
            help = 'Disable sysinfo bar. Default is True',
            action='store_false', default = True)
    
    parser.add_argument('-ci','--cpuinfo', dest='cpuinfo',
            help = 'Disable cpuinfo bar. Default is True',
            action='store_false', default = True)

    parser.add_argument('-pi','--procinfo', dest='procinfo',
            help = 'Disable procinfo bar. Default is True',
            action='store_false', default = True)
    
    parser.add_argument('-mi','--meminfo', dest='meminfo',
            help = 'Disable meminfo bar. Default is True',
            action='store_false', default = True)

    parser.add_argument('-hi','--hddinfo', dest='hddinfo',
            help = 'Number of mount point in HDD bar ([0..3]). "0" is disable HDD bar. Default is "3"',
            action='store', default = "3")  
    
    parser.add_argument('-ni','--netinfo', dest='netinfo',
            help = 'Disable netinfo bar. Default is True',
            action='store_false', default = True)
  
    parser.add_argument('-a','--amarok', dest='amarok',
            help = 'Disable amarok bar. Default is True',
            action='store_false', default = True)
    
    parser.add_argument('-ab','--amarokbuttons', dest='abut',
            help = 'Enable buttons on amarok bar. Default is False',
            action='store_true', default = False)
    
    parser.add_argument('-n','--net', dest='net',
            help = 'Name of network interface (if you use one device). Default is "eth0"',
            action='store', default = 'eth0')
    
    parser.add_argument('-n1','--net1', dest='net1',
            help = 'Name of first network interface (if you use two devices). Default is False',
            action='store', default = False)
    
    parser.add_argument('-n2','--net2', dest='net2',
            help = 'Name of second network interface (if you use two devices). Default is False',
            action='store', default = False)
    
    parser.add_argument('-hdd','--harddisk', dest='hdd',
            help = 'Name of hard disk drive device. Default is "/dev/sda"',
            action='store', default = '/dev/sda')

    parser.add_argument('-mp1','--mountpoint1', dest='mountpoint1',
            help = 'Path to first mountpoint. Default is "/"',
            action='store', default = '/')

    parser.add_argument('-mp2','--mountpoint2', dest='mountpoint2',
            help = 'Path to second mountpoint. Default is "/home"',
            action='store', default = '/home')
    
    parser.add_argument('-mp3','--mountpoint3', dest='mountpoint3',
            help = 'Path to third mountpoint. Default is "/usr"',
            action='store', default = '/usr')
    
    parser.add_argument('-co','--core', dest='core',
            help = 'Number of processor cores. Default is "1"',
            action='store', default = '1')

    parser.add_argument('-c','--cpufile', dest='cpu',
            help = 'File with cpu information. Default is "/proc/cpuinfo"',
            action='store', default = '/proc/cpuinfo')
    
    parser.add_argument('-px','--positionx', dest='posx',
            help = 'Position of the applet (X Axis), pixels. Default is "1366" (Right)',
            action='store', default = '1366')
    
    parser.add_argument('-py','--positiony', dest='posy',
            help = 'Position of the applet (Y Axis), pixels. Default is "768" (Up)',
            action='store', default = '768')
    
    args = parser.parse_args()
    
    
    if (args.ver):
        print ("                    Kit System Monitor")
        print ("System information and hardware monitor based on EG Sysmon")
        print ("Version : 1.2                                License : GPL")
        print ("                                                by arcanis")
        print ("                              E-mail : esalexeev@gmail.com")


    else:
        with open("sysmon.theme", 'w') as theme:
            height=7
            if (args.sysinfo):
                height+=101
            if (args.cpuinfo):
                if (args.core=="2"):
                    height+=158
                elif (args.core=="1"):
                    height+=143
                else:
                    height+=188
            if (args.procinfo):
                height+=68
            if (args.meminfo):
                height+=106
            if (args.hddinfo=="3"):
                height+=165
            elif (args.hddinfo=="2"):
                height+=130
            elif (args.hddinfo=="1"):
                height+=98
            if (args.netinfo):
                height+=138
            if (args.amarok):
                if (args.abut):
                    height+=160
                else:
                    height+=110
            height_string=str(height)
            theme.write("karamba x="+args.posx+" y="+args.posy+" w=300 h="+height_string+" locked=True\n")
            theme.write("defaultfont font=\"Arial\" fontsize=10 color="+args.colmain+"\nimage x=15 y=4 path=\"img/bckgrnd.png\"\n\x23\nimage x=10 y=1 path=\"img/ligne.png\"\n")


            height=7
            if (args.sysinfo):
                height_string=str(height)
                theme.write("\x23\n\x23 System group\n\x23\n<group> x=0 y="+height_string+"\n  image x=33 y=35 path=\"icones/sysinfo.png\"\n")
                theme.write("  text x=160 y=7 value=\"")
                if (args.lang=="rus"):
                    line=u"Информация о Системе"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="System Informantion"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="System-Informationen"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Système d'information"
                    theme.write(line.encode('utf-8'))
                theme.write("\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n  text x=85 y=35  value=\"")
                if (args.lang=="rus"):
                    line=u"Пользователь"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="User"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Benutzer"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="Utilisateur"
                    theme.write(line)
                theme.write(" :\" fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n")
                theme.write("  text x=290 y=35 sensor=program program=\"echo ${USER}\" line=1 fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\n")
                theme.write("  text x=85 y=53 value=\"")
                if (args.lang=="rus"):
                    line=u"Аптайм"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Uptime"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Betriebszeit"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Disponibilité"
                    theme.write(line.encode('utf-8'))
                theme.write(" :\" fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n")
                theme.write("  text x=290 y=53 sensor=uptime format=\"%d Day(s) %Hh%Mmin\" line=1 fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\n")
                theme.write("  text x=85 y=71 value=\"Kernel :\" fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n")
                theme.write("  text x=290 y=71 sensor=program program=\"uname -r\" line=1 fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\nЭ")
                height+=101
                img_pos=height-13
                img_pos_str=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
            
            
            if (args.cpuinfo):
                height_string=str(height)
                theme.write("\x23 CPU Group\n\x23\n<group> x=0 y="+height_string+"\n  image x=27 y=70 path=\"icones/cpu.png\"\n  text x=160 y=7 value=\"CPU\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n")
                theme.write("  text x=160 y=30 sensor=program program=\"cat ")
                theme.write(args.cpu)
                theme.write(" | grep 'model name' | sed -e 's/.*: //'\" line=1 fontsize=10 font=\"Droid Sans Mono\" color="+args.colmain+" align=center\n")
                theme.write("  text x=97 y=48 value=\"")
                if (args.lang=="rus"):
                    line=u"Температура"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Temperature"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Temperatur"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Température"
                    theme.write(line.encode('utf-8'))
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n")
                theme.write("  text x=290 y=48 sensor=program program=\"sensors | grep  'high' | awk '{print $2 }'\"  fontsize=12 font=\"Droid Sans Mono\"  interval=50000 color="+args.colmain+" align=right\n")
                if (args.core=="2"):
                    theme.write("  image x=103 y=70 path=\"img/cpugrille.png\"\n  graph x=103 y=70 w=177 h=23 sensor=cpu cpu=0 interval=2000 color="+args.col1+"\n  graph x=103 y=70 w=177 h=23 sensor=cpu cpu=1 interval=2000 color="+args.col2+"\n\x23\n")
                    theme.write("  text x=97 y=100 value=\"Core 0 : \" fontsize=12 font=\"Arial\" color="+args.col1+" align=left\n  text x=190 y=100 sensor=cpu cpu=0 format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col1+" interval=2000 aligh=right\n")
                    theme.write("  text x=197 y=100 value=\"Core 1 :\"  fontsize=12 font=\"Arial\" color="+args.col2+" align=left\n  text x=290 y=100 sensor=cpu cpu=1 format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col2+" interval=2000 align=right\n")
                    theme.write("  text x=97 y=115 value=\"MHz :\"  fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=190 y=115 sensor=program program=\"cat ")
                    theme.write(args.cpu)
                    theme.write(" | grep MHz | awk '{print $4}' | cut -c -6 | head -n1\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col1+" interval=2000 aligh=right\n  text x=290 y=115 sensor=program program=\"cat ")
                    theme.write(args.cpu)
                    theme.write(" | grep MHz | awk '{print $4}' | cut -c -6 | tail -n1\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col2+" interval=2000 aligh=right\n  text x=97 y=130 value=\"")
                    if (args.lang=="rus"):
                        line=u"Общая загрузка"
                        theme.write(line.encode('utf-8'))
                    elif (args.lang=="eng"):
                        line="All"
                        theme.write(line)
                    elif (args.lang=="ger"):
                        line="Alle"
                        theme.write(line)
                    elif (args.lang=="fr"):
                        line="Tous"
                        theme.write(line)
                    theme.write(" :\"  fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=290 y=130 sensor=cpu cpu=all format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" interval=2000 align=right\n")
                    height+=158
                    img_pos=height-13
                    img_pos_str=str(img_pos)
                    theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
                elif (args.core=="1"):
                    theme.write("  image x=103 y=70 path=\"img/cpugrille.png\"\n  graph x=103 y=70 w=177 h=23 sensor=cpu cpu=0 interval=2000 color="+args.col1+"\n\x23\n")
                    theme.write("  text x=97 y=100 value=\"Core 0 : \" fontsize=12 font=\"Arial\" color="+args.col1+" align=left\n  text x=290 y=100 sensor=cpu cpu=0 format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col1+" interval=2000 aligh=right\n")
                    theme.write("  text x=97 y=115 value=\"MHz :\"  fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=290 y=115 sensor=program program=\"cat ")
                    theme.write(args.cpu)
                    theme.write(" | grep MHz | awk '{print $4}' | cut -c -6 | head -n1\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col1+" interval=2000 aligh=right\n")
                    height+=143
                    img_pos=height-13
                    img_pos_str=str(img_pos)
                    theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
                else:
                    theme.write("  image x=103 y=70 path=\"img/cpugrille.png\"\n  graph x=103 y=70 w=177 h=23 sensor=cpu cpu=0 interval=2000 color="+args.col1+"\n  graph x=103 y=70 w=177 h=23 sensor=cpu cpu=1 interval=2000 color="+args.col2+"\n")
                    theme.write("  graph x=103 y=70 w=177 h=23 sensor=cpu cpu=2 interval=2000 color="+args.col3+"\n  graph x=103 y=70 w=177 h=23 sensor=cpu cpu=3 interval=2000 color="+args.col4+"\n\x23\n")
                    theme.write("  text x=97 y=100 value=\"Core 0 : \" fontsize=12 font=\"Arial\" color="+args.col1+" align=left\n  text x=190 y=100 sensor=cpu cpu=0 format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col1+" interval=2000 aligh=right\n")
                    theme.write("  text x=197 y=100 value=\"Core 1 :\"  fontsize=12 font=\"Arial\" color="+args.col2+" align=left\n  text x=290 y=100 sensor=cpu cpu=1 format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col2+" interval=2000 align=right\n")
                    theme.write("  text x=97 y=115 value=\"MHz :\"  fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=190 y=115 sensor=program program=\"cat ")
                    theme.write(args.cpu)
                    theme.write(" | grep MHz | awk '{print $4}' | cut -c -6 | head -n1\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col1+" interval=2000 aligh=right\n  text x=290 y=115 sensor=program program=\"cat ")
                    theme.write(args.cpu)
                    theme.write(" | grep MHz | awk '{print $4}' | cut -c -6 | head -n2 | tail -n1\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col2+" interval=2000 aligh=right\n")
                    theme.write("  text x=97 y=130 value=\"Core 2 : \" fontsize=12 font=\"Arial\" color="+args.col3+" align=left\n  text x=190 y=130 sensor=cpu cpu=2 format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col3+" interval=2000 aligh=right\n")
                    theme.write("  text x=197 y=130 value=\"Core 3 :\"  fontsize=12 font=\"Arial\" color="+args.col4+" align=left\n  text x=290 y=130 sensor=cpu cpu=3 format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col4+" interval=2000 align=right\n")
                    theme.write("  text x=97 y=145 value=\"MHz :\"  fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=190 y=145 sensor=program program=\"cat ")
                    theme.write(args.cpu)
                    theme.write(" | grep MHz | awk '{print $4}' | cut -c -6 | tail -n2 | head -n1\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col3+" interval=2000 aligh=right\n  text x=290 y=145 sensor=program program=\"cat ")
                    theme.write(args.cpu)
                    theme.write(" | grep MHz | awk '{print $4}' | cut -c -6 | tail -n1\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.col4+" interval=2000 aligh=right\n  text x=97 y=160 value=\"")
                    if (args.lang=="rus"):
                        line=u"Общая загрузка"
                        theme.write(line.encode('utf-8'))
                    elif (args.lang=="eng"):
                        line="All"
                        theme.write(line)
                    elif (args.lang=="ger"):
                        line="Alle"
                        theme.write(line)
                    elif (args.lang=="fr"):
                        line="Tous"
                        theme.write(line)
                    theme.write(" :\"  fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=290 y=160 sensor=cpu cpu=all format=\"%v%\" align=right fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" interval=2000 align=right\n")
                    height+=188
                    img_pos=height-13
                    img_pos_str=str(img_pos)
                    theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
            
            
            if (args.procinfo):
                height_string=str(height)
                theme.write("\x23 Process group\n\x23\n<group> x=0 y="+height_string+"\n  text x=30 y=7 value=\"")
                if (args.lang=="rus"):
                    line=u"Процессы"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Tasks"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Aufgaben"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Tâches"
                    theme.write(line.encode('utf-8'))
                theme.write(" :\" fontsize=12 font=\"Arial\" align=left color="+args.colmain+"\n")
                theme.write("  text x=290 y=7  sensor=program program=\"ps xa | wc -l\" align=right fontsize=12 font=\"Droid Sans Mono\" interval=5000 align=right color="+args.colmain+"\n")
                theme.write("  text x=30 y=22 value=\"")
                if (args.lang=="rus"):
                    line=u"Запущенно"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Running"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Laufen"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="Course"
                    theme.write(line)
                theme.write(" :\" color="+args.col1+" fontsize=12 font=\"Arial\" align=left\n  text x=160 y=22 sensor=program program=\"ps axr| wc -l\" align=left interval=2000 color="+args.col1+" fontsize=12 font=\"Droid Sans Mono\" align=right\n")
                theme.write("  text x=180 y=22 value=\"")
                if (args.lang=="rus"):
                    line=u"Загрузка"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Load"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Last"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="Poids"
                    theme.write(line)
                theme.write(" :\" color="+args.col2+" fontsize=12 font=\"Arial\" align=left\n  text x=290 y=22 sensor=cpu cpu=all format=%load% interval=2000 color="+args.col2+" fontsize=12 font=\"Droid Sans Mono\" align=right\n")
                theme.write("  text x=30 y=37 value=\"System :\" color="+args.col3+" fontsize=12 font=\"Arial\" align=left\n")
                theme.write("  text x=167 y=37 sensor=cpu cpu=all format=%system% interval=2000 color="+args.col3+" fontsize=12 font=\"Droid Sans Mono\" align=right\n")
                theme.write("  text x=180 y=37 value=\"User :\" color="+args.col4+" fontsize=12 font=\"Arial\" align=left\n")
                theme.write("  text x=290 y=37 sensor=cpu cpu=all format=%user% interval=2000 color="+args.col4+" fontsize=12 font=\"Droid Sans Mono\" align=right\n")
                height+=68
                img_pos=height-13
                img_pos_str=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")

            
            if (args.meminfo):
                height_string=str(height)
                theme.write("\x23 Memory\n\x23\n<group> x=0 y="+height_string+"\n  image x=25 y=35 path=\"icones/memory.png\"\n  text x=160 y=5 value=\"")
                if (args.lang=="rus"):
                    line=u"Память"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Memory"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Speicher"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Mémoire"
                    theme.write(line.encode('utf-8'))
                theme.write("\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n  text x=130 y=25 sensor=memory format=\"%umb\"  fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\n  text x=260 y=25 sensor=memory format=\"")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %tm Mb (RAM)\"  fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\n\x23\n  image x=83 y=41 vertical=false path=\"img/jauge_fond.png\"\n")
                theme.write("  bar x=88 y=46 sensor=memory format=\"%umb\" interval=\"1000\" vertical=false path=\"img/jauge.png\" mountpoint=\"/home\"\n\x23\n  text x=125 y=60 sensor=memory format=\"%us\"  fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\n  text x=265 y=60 sensor=memory format=\"")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %ts Mb (SWAP)\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+"  align=right\n\x23\n  image x=83 y=77 vertical=false path=\"img/jauge_fond.png\"\n")
                theme.write("  bar x=88 y=82 sensor=memory format=\"%us\" interval=\"1000\" vertical=false path=\"img/jauge.png\" mountpoint=\"/home\"\n\x23\n")
                height+=106
                img_pos=height-13
                img_pos_str=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
            
            
            if (args.hddinfo=="3"):
                height_string=str(height)
                theme.write("\x23 HDD group\n\x23\n<group> x=0 y="+height_string+"\n  image x=27 y=60 path=\"icones/hdd.png\"\n  text x=160 y=7 value=\"HDD\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n")
                theme.write("  text x=90 y=28 value=")
                if (args.lang=="rus"):
                    line=u"Температура"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Temperature"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Temperatur"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Température"
                    theme.write(line.encode('utf-8'))
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n")
                theme.write("  text x=290 y=28 sensor=program program=\"hddtemp "+args.hdd+" | awk '{print $4}'\"  fontsize=12 font=\"Droid Sans Mono\"  interval=50000 color="+args.colmain+" align=right\n\x23\n")
                theme.write("  text x=188 y=47 sensor=disk format=\"%ug  ")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %tg Gb ("+args.mountpoint1+")\" mountpoint=\""+args.mountpoint1+"\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=center interval=10000\n")
                theme.write("  image x=88 y=63 vertical=false path=\"img/jauge_fond.png\"\n  bar x=93 y=68 sensor=disk mountpoint=\""+args.mountpoint1+"\" vertical=false path=\"img/jauge.png\" interval=10000\n\x23\n")
                theme.write("  text x=188 y=82 sensor=disk format=\"%ug  ")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %tg Gb ("+args.mountpoint2+")\" mountpoint=\""+args.mountpoint2+"\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=center interval=10000\n")
                theme.write("  image x=88 y=98 vertical=false path=\"img/jauge_fond.png\"\n  bar x=93 y=103 sensor=disk mountpoint=\""+args.mountpoint2+"\" vertical=false path=\"img/jauge.png\" interval=10000\n\x23\n")
                theme.write("  text x=188 y=117 sensor=disk format=\"%ug  ")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %tg Gb ("+args.mountpoint3+")\" mountpoint=\""+args.mountpoint3+"\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=center interval=10000\n")
                theme.write("  image x=88 y=133 vertical=false path=\"img/jauge_fond.png\"\n  bar x=93 y=138 sensor=disk mountpoint=\""+args.mountpoint3+"\" vertical=false path=\"img/jauge.png\" interval=10000\n")
                height+=165
                img_pos=height-13
                img_pos_str=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
            elif(args.hddinfo=="2"):
                height_string=str(height)
                theme.write("\x23 HDD group\n\x23\n<group> x=0 y="+height_string+"\n  image x=27 y=45 path=\"icones/hdd.png\"\n  text x=160 y=7 value=\"HDD\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n")
                theme.write("  text x=90 y=28 value=")
                if (args.lang=="rus"):
                    line=u"Температура"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Temperature"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Temperatur"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Température"
                    theme.write(line.encode('utf-8'))
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n")
                theme.write("  text x=290 y=28 sensor=program program=\"hddtemp "+args.hdd+" | awk '{print $4}'\"  fontsize=12 font=\"Droid Sans Mono\"  interval=50000 color="+args.colmain+" align=right\n\x23\n")
                theme.write("  text x=188 y=47 sensor=disk format=\"%ug  ")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %tg Gb ("+args.mountpoint1+")\" mountpoint=\""+args.mountpoint1+"\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=center interval=10000\n")
                theme.write("  image x=88 y=63 vertical=false path=\"img/jauge_fond.png\"\n  bar x=93 y=68 sensor=disk mountpoint=\""+args.mountpoint1+"\" vertical=false path=\"img/jauge.png\" interval=10000\n\x23\n")
                theme.write("  text x=188 y=82 sensor=disk format=\"%ug  ")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %tg Gb ("+args.mountpoint2+")\" mountpoint=\""+args.mountpoint2+"\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=center interval=10000\n")
                theme.write("  image x=88 y=98 vertical=false path=\"img/jauge_fond.png\"\n  bar x=93 y=103 sensor=disk mountpoint=\""+args.mountpoint2+"\" vertical=false path=\"img/jauge.png\" interval=10000\n\x23\n")
                height+=130
                img_pos=height-13
                img_pos_str=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
            elif(args.hddinfo=="1"):
                height_string=str(height)
                theme.write("\x23 HDD group\n\x23\n<group> x=0 y="+height_string+"\n  image x=27 y=30 path=\"icones/hdd.png\"\n  text x=160 y=7 value=\"HDD\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n")
                theme.write("  text x=90 y=28 value=")
                if (args.lang=="rus"):
                    line=u"Температура"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Temperature"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Temperatur"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line=u"Température"
                    theme.write(line.encode('utf-8'))
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n")
                theme.write("  text x=290 y=28 sensor=program program=\"hddtemp "+args.hdd+" | awk '{print $4}'\"  fontsize=12 font=\"Droid Sans Mono\"  interval=50000 color="+args.colmain+" align=right\n\x23\n")
                theme.write("  text x=188 y=47 sensor=disk format=\"%ug  ")
                if (args.lang=="rus"):
                    line=u"из"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="of"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="von"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="de"
                    theme.write(line)
                theme.write("  %tg Gb ("+args.mountpoint1+")\" mountpoint=\""+args.mountpoint1+"\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=center interval=10000\n")
                theme.write("  image x=88 y=63 vertical=false path=\"img/jauge_fond.png\"\n  bar x=93 y=68 sensor=disk mountpoint=\""+args.mountpoint1+"\" vertical=false path=\"img/jauge.png\" interval=10000\n\x23\n")
                height+=98
                img_pos=height-13
                img_pos_str=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23\n")
            
            
            if (args.netinfo):
                height_string=str(height)
                theme.write("\x23 Internet\n\x23\n<group> x=0 y="+height_string+"\n  image x=32 y=50 PATH=\"icones/internet.png\"\n  text x=160 y=7 value=\"")
                if (args.lang=="rus"):
                    line=u"Интернет"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Internet"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Internet"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="Internet"
                    theme.write(line)
                theme.write("\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n  text  x=97 y=26 value=\"IP (\" color="+args.colmain+" fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n")
                if (args.net1):
                    theme.write("  text  x=150 y=26 sensor=program program=\"if ! (ifconfig ")
                    theme.write(args.net2)
                    theme.write(" | grep 'inet ' > /dev/null); then if ! (ifconfig ")
                    theme.write(args.net1)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo ")
                    theme.write(args.net1)
                    theme.write("; fi; else echo ")
                    theme.write(args.net2)
                    theme.write("; fi\" color="+args.colmain+" fontsize=12 font=\"Arial\" color="+args.colmain+" align=right interval=10000\n  text  x=160 y=26 value=\"):\" color="+args.colmain+" fontsize=12 font=\"Arial\" color="+args.colmain+" align=right\n")
                    theme.write("  text x=290 y=26 sensor=program program=\"NETDEV=`if ! (ifconfig ")
                    theme.write(args.net2)
                    theme.write(" | grep 'inet ' > /dev/null); then if ! (ifconfig ")
                    theme.write(args.net1)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo ")
                    theme.write(args.net1)
                    theme.write("; fi; else echo ")
                    theme.write(args.net2)
                    theme.write("; fi`; ifconfig $NETDEV | grep 'inet ' | awk '{print $2 }'\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right interval=10000\n  text x=97 y=41 value=\"")
                    if (args.lang=="rus"):
                        line=u"Внешний IP"
                        theme.write(line.encode('utf-8'))
                    elif (args.lang=="eng"):
                        line="External IP"
                        theme.write(line)
                    elif (args.lang=="ger"):
                        line="Externe IP"
                        theme.write(line)
                    elif (args.lang=="fr"):
                        line="IP Externe"
                        theme.write(line)
                    theme.write(" :\" color="+args.colmain+" fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=297 y=41 sensor=program program=\"wget http://checkip.dyndns.org/ -q -O - | awk '{print $6}' | sed 's/<.*>//g'\" interval=10000 fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\n")
                    theme.write("  text x=97 y=56 value=\"Hostname :\" fontsize=12 font=\"Arial\"  color="+args.colmain+" align=left\n  text x=290 y=56 sensor=program program=\"'hostname'\" color="+args.colmain+" fontsize=12 font=\"Droid Sans Mono\" align=right\n\x23\n  image x=101 y=75 path=\"img/grille.png\"\n")
                    theme.write("  graph x=101 y=75 w=184 h=28 color="+args.col1+" sensor=network device=")
                    theme.write(args.net1)
                    theme.write(" format=\"%in\" interval=1000 max=250\n  graph x=101 y=75 w=184 h=28 color=247,1,1 sensor=network device=")
                    theme.write(args.net1)
                    theme.write(" format=\"%out\" interval=1000 max=250\n  graph x=101 y=75 w=184 h=28 color="+args.col1+" sensor=network device=")
                    theme.write(args.net2)
                    theme.write(" format=\"%in\" interval=1000 max=250\n  graph x=101 y=75 w=184 h=28 color=247,1,1 sensor=network device=")
                    theme.write(args.net2)
                    theme.write(" format=\"%out\" interval=1000 max=250\n\x23\n  text x=97 y=110 sensor=program program=\"if ! (ifconfig ")
                    theme.write(args.net2)
                    theme.write(" | grep 'inet ' > /dev/null); then if ! (ifconfig ")
                    theme.write(args.net1)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo ")
                    theme.write(args.net1)
                    theme.write("; fi; else echo ")
                    theme.write(args.net2)
                    theme.write("; fi\" fontsize=12 font=\"Arial\" decimals=1 color="+args.colmain+" align=left\n  text x=290 y=110 sensor=program program=\"NETDEV=`if ! (ifconfig ")
                    theme.write(args.net2)
                    theme.write(" | grep 'inet ' > /dev/null); then if ! (ifconfig ")
                    theme.write(args.net1)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo ")
                    theme.write(args.net1)
                    theme.write("; fi; else echo ")
                    theme.write(args.net2)
                    theme.write("; fi`; RXB=$(cat /sys/class/net/$NETDEV/statistics/rx_bytes) && TXB=$(cat /sys/class/net/$NETDEV/statistics/tx_bytes) && sleep 2 && ")
                    theme.write("RXBN=$(cat /sys/class/net/$NETDEV/statistics/rx_bytes) && TXBN=$(cat /sys/class/net/$NETDEV/statistics/tx_bytes) && RXDIF=$(echo $((RXBN - RXB)) ) && TXDIF=$(echo $((TXBN - TXB)) ) && ")
                    theme.write("echo -en $((RXDIF/1024/2)) && echo -n ' / ' && echo -en $((TXDIF/1024/2)) && echo ' KB/s'\" fontsize=12 font=\"Droid Sans Mono\" decimals=1 color="+args.colmain+" align=right interval=1000\n")
                else:
                    theme.write("  text  x=150 y=26 sensor=program program=\"if ! (ifconfig ")
                    theme.write(args.net)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo "+args.net+"; fi\" color="+args.colmain+" fontsize=12 font=\"Arial\" color="+args.colmain+" align=right interval=10000\n")
                    theme.write("  text  x=160 y=26 value=\"):\" color="+args.colmain+" fontsize=12 font=\"Arial\" color="+args.colmain+" align=right\n")
                    theme.write("  text x=290 y=26 sensor=program program=\"NETDEV=`if ! (ifconfig ")
                    theme.write(args.net)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo "+args.net+"; fi`")
                    theme.write("; ifconfig $NETDEV | grep 'inet ' | awk '{print $2 }'\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right interval=10000\n  text x=97 y=41 value=\"")
                    if (args.lang=="rus"):
                        line=u"Внешний IP"
                        theme.write(line.encode('utf-8'))
                    elif (args.lang=="eng"):
                        line="External IP"
                        theme.write(line)
                    elif (args.lang=="ger"):
                        line="Externe IP"
                        theme.write(line)
                    elif (args.lang=="fr"):
                        line="IP Externe"
                        theme.write(line)
                    theme.write(" :\" color="+args.colmain+" fontsize=12 font=\"Arial\" color="+args.colmain+" align=left\n  text x=297 y=41 sensor=program program=\"wget http://checkip.dyndns.org/ -q -O - | awk '{print $6}' | sed 's/<.*>//g'\" interval=10000 fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right\n")
                    theme.write("  text x=97 y=56 value=\"Hostname :\" fontsize=12 font=\"Arial\"  color="+args.colmain+" align=left\n  text x=290 y=56 sensor=program program=\"'hostname'\" color="+args.colmain+" fontsize=12 font=\"Droid Sans Mono\" align=right\n\x23\n  image x=101 y=75 path=\"img/grille.png\"\n")
                    theme.write("  graph x=101 y=75 w=184 h=28 color="+args.col1+" sensor=network device=")
                    theme.write(args.net)
                    theme.write(" format=\"%in\" interval=1000 max=250\n  graph x=101 y=75 w=184 h=28 color=247,1,1 sensor=network device="+args.net+" format=\"%out\" interval=1000 max=250\n\x23\n")
                    theme.write("  text x=97 y=110 sensor=program program=\"if ! (ifconfig "+args.net)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo "+args.net+"; fi\" fontsize=12 font=\"Arial\" decimals=1 color="+args.colmain+" align=left\n")
                    theme.write("  text x=290 y=110 sensor=program program=\"NETDEV=`if ! (ifconfig "+args.net)
                    theme.write(" | grep 'inet ' > /dev/null); then echo lo; else echo "+args.net+"; fi`")
                    theme.write("; RXB=$(cat /sys/class/net/$NETDEV/statistics/rx_bytes) && TXB=$(cat /sys/class/net/$NETDEV/statistics/tx_bytes) && sleep 2 && ")
                    theme.write("RXBN=$(cat /sys/class/net/$NETDEV/statistics/rx_bytes) && TXBN=$(cat /sys/class/net/$NETDEV/statistics/tx_bytes) && RXDIF=$(echo $((RXBN - RXB)) ) && TXDIF=$(echo $((TXBN - TXB)) ) && ")
                    theme.write("echo -en $((RXDIF/1024/2)) && echo -n ' / ' && echo -en $((TXDIF/1024/2)) && echo ' KB/s'\" fontsize=12 font=\"Droid Sans Mono\" decimals=1 color="+args.colmain+" align=right interval=1000\n")
                height+=138
                img_pos=height-13
                img_pos_string=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_string+" path=\"img/ligne.png\"\n\x23\n")

            
            if (args.amarok):
                height_string=str(height)
                theme.write("\x23 Amarok Bar\n\x23\n<group> x=0 y="+height_string+"\n  text x=160 y=7 value=\"Amarok\" fontsize=14 font=\"Arial\" color="+args.colhead+" align=center\n\x23\n")
                theme.write("  text x=30 y=30 value=\"")
                if (args.lang=="rus"):
                    line=u"Композиция"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Title"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Songtitel"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="Titre"
                    theme.write(line)
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n  text x=290 y=30 sensor=program program=\"title=")
                theme.write("`qdbus org.kde.amarok /Player GetMetadata | grep -m1 title: | cut -c 7- | sed -e 's/^[ \\t]*//'`;[ `echo $title |  wc -c` -lt 20 ] && echo $title || echo `echo $title | cut -c -16`...\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right interval=2000\n\x23\n")
                theme.write("  text x=30 y=47 value=\"")
                if (args.lang=="rus"):
                    line=u"Исполнитель"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Artist"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line=u"Künstler"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="fr"):
                    line="Artiste"
                    theme.write(line)
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n  text x=290 y=47 sensor=program program=\"artist=")
                theme.write("`qdbus org.kde.amarok /Player GetMetadata | grep -m1 artist: | cut -c 14-`;[ `echo $artist | wc -c` -lt 20 ] && echo $artist || echo `echo $artist | cut -c -16`...\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right interval=2000\n")
                theme.write("\x23\n  text x=30 y=64 value=\"")
                if (args.lang=="rus"):
                    line=u"Альбом"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Album"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Album"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="Album"
                    theme.write(line)
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n  text x=290 y=64 sensor=program program=\"album=")
                theme.write("`qdbus org.kde.amarok /Player GetMetadata | grep -m1 album: | cut -c 7- | sed -e 's/^[ \\t]*//'`;[ `echo $album |  wc -c` -lt 20 ] && echo $album || echo `echo $album | cut -c -18`...\" fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right interval=2000\n")
                theme.write("\x23\n  text x=30 y=81 value=\"")
                if (args.lang=="rus"):
                    line=u"Время"
                    theme.write(line.encode('utf-8'))
                elif (args.lang=="eng"):
                    line="Time"
                    theme.write(line)
                elif (args.lang=="ger"):
                    line="Zeit"
                    theme.write(line)
                elif (args.lang=="fr"):
                    line="Temps"
                    theme.write(line)
                theme.write(" :\" align=left fontsize=12 font=\"Arial\" color="+args.colmain+"\n  text x=235 y=81 sensor=program program=\"milTime=")
                theme.write("`qdbus org.kde.amarok /Player PositionGet`;[ `expr length $((milTime/1000 % 60))` -lt 2 ] && echo $((milTime/60000)):0$((milTime/1000 % 60)) || echo $((milTime/60000)):$((milTime/1000 %60))\"  fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right interval=2000\n")
                theme.write("  text x=250 y=81 value=\"/\" align=right fontsize=12 font=\"Arial\" color=255.255.255\n  text x=290 y=81 sensor=program program=\"timeall=")
                theme.write("`qdbus org.kde.amarok /Player GetMetadata | grep mtime | awk '{print $2 }'`;[ `expr length $((timeall/1000 % 60))` -lt 2 ] && echo $((timeall/60000)):0$((timeall/1000 % 60)) || echo $((timeall/60000)):$((timeall/1000 %60))\"  fontsize=12 font=\"Droid Sans Mono\" color="+args.colmain+" align=right interval=2000\n")
                if (args.abut):
                    theme.write("\x23\n  image x=60 y=101 path=\"img/prev.png\"\n  image x=105 y=91 path=\"img/play.png\"\n  image x=175 y=101 path=\"img/next.png\"\n  image x=220 y=101 path=\"img/stop.png\"\n")
                    theme.write("  clickarea x=60 y=101 w=40 h=40 preview=false onclick=\"qdbus org.kde.amarok /Player Prev\" name=\"Previous\"\n")
                    theme.write("  clickarea x=105 y=91 w=60 h=60 preview=false onclick=\"qdbus org.kde.amarok /Player Play\" name=\"Play\"\n")
                    theme.write("  clickarea x=175 y=101 w=40 h=40 preview=false onclick=\"qdbus org.kde.amarok /Player Next\" name=\"Next\"\n")
                    theme.write("  clickarea x=220 y=101 w=40 h=40 preview=false onclick=\"qdbus org.kde.amarok /Player Stop\" name=\"Stop\"\n")
                if (args.abut):
                    height+=160
                else:
                    height+=110
                img_pos=height-13
                img_pos_str=str(img_pos)
                theme.write("</group>\n\x23\nimage x=10 y="+img_pos_str+" path=\"img/ligne.png\"\n\x23")
        
        
        with open("maindata.xml",  'w') as xml:
            xml.write("<?xml version=\"2.2\" encoding=\"UTF-8\"?>\n<!DOCTYPE superkaramba_theme>\n<superkaramba_theme>\n")
            xml.write(" <themefile>sysmon.theme</themefile>\n <name>System Monitor</name>\n <icon>Logo.png</icon>\n")
            xml.write(" <description>System information and hardware monitor based on EG Sysmon. Monitors CPU, memory (HDD and RAM/SWAP), network and amarok. </description>")
            xml.write(" <author>Evgeniy Alexeev aka arcanis</author>\n <author_email>esalexeev@gmail.com</author_email>\n")
            xml.write("\t<version>1.2</version>\n\t<license>GPL</license>\n</superkaramba_theme>")
    
    
        if (args.startup):
            src=os.getcwd()+"/startup.sh"
            if (args.mark and args.dir):
	        new_st=os.getcwd()+"/sysmon_startup_"+args.mark+".sh"
	    else:
                new_st=os.getcwd()+"/sysmon_startup.sh"
            shutil.copy(src, new_st)
            with open(new_st, 'a') as start:
                start.write("superkaramba ")
                if (args.dir):
                    if (args.mark):
                        path=os.path.abspath(args.dir)+"/sysmon_"+args.mark+"/sysmon.theme"
                    else:
                        path=os.path.abspath(args.dir)+"/sysmon/sysmon.theme"
                else:
                    path=os.getcwd()+"/sysmon.theme\n"
                start.write(path)
            
            tar=os.path.abspath(args.startup)
            shutil.copy(new_st,  tar)


        if (args.dir):
            tar_dir=os.path.abspath(args.dir)+"/sysmon"
            if (args.mark):
                tar_dir+="_"+args.mark
            if (os.path.exists(tar_dir)):
                shutil.rmtree(tar_dir)
            cur_dir=os.getcwd()
            shutil.copytree(cur_dir, tar_dir)
            rem=tar_dir+"/KitSysMon.py"
            os.remove(rem)
            rem=tar_dir+"/startup.sh"
            os.remove(rem)
            rem=tar_dir+"/INSTALL"
            os.remove(rem)