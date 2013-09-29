Attribute VB_Name = "Module2"
Option Explicit


Public sBC(106) As String
Public sCA(106) As String
Public sCC(106) As String

Public Sub BC_Init()
    sBC(0) = "212222"
    sBC(1) = "222122"
    sBC(2) = "222221"
    sBC(3) = "121223"
    sBC(4) = "121322"
    sBC(5) = "131222"
    sBC(6) = "122213"
    sBC(7) = "122312"
    sBC(8) = "132212"
    sBC(9) = "221213"
    sBC(10) = "221312"
    sBC(11) = "231212"
    sBC(12) = "112232"
    sBC(13) = "122132"
    sBC(14) = "122231"
    sBC(15) = "113222"
    sBC(16) = "123122"
    sBC(17) = "123221"
    sBC(18) = "223211"
    sBC(19) = "221132"
    sBC(20) = "221231"
    sBC(21) = "213212"
    sBC(22) = "223112"
    sBC(23) = "312131"
    sBC(24) = "311222"
    sBC(25) = "321122"
    sBC(26) = "321221"
    sBC(27) = "312212"
    sBC(28) = "322112"
    sBC(29) = "322211"
    sBC(30) = "212123"
    sBC(31) = "212321"
    sBC(32) = "232121"
    sBC(33) = "111323"
    sBC(34) = "131123"
    sBC(35) = "131321"
    sBC(36) = "112313"
    sBC(37) = "132113"
    sBC(38) = "132311"
    sBC(39) = "211313"
    sBC(40) = "231113"
    sBC(41) = "231311"
    sBC(42) = "112133"
    sBC(43) = "112331"
    sBC(44) = "132131"
    sBC(45) = "113123"
    sBC(46) = "113321"
    sBC(47) = "133121"
    sBC(48) = "313121"
    sBC(49) = "211331"
    sBC(50) = "231131"
    sBC(51) = "213113"
    sBC(52) = "213311"
    sBC(53) = "213131"
    sBC(54) = "311123"
    sBC(55) = "311321"
    sBC(56) = "331121"
    sBC(57) = "312113"
    sBC(58) = "312311"
    sBC(59) = "332111"
    sBC(60) = "314111"
    sBC(61) = "221411"
    sBC(62) = "431111"
    sBC(63) = "111224"
    sBC(64) = "111422"
    sBC(65) = "121124"
    sBC(66) = "121421"
    sBC(67) = "141122"
    sBC(68) = "141221"
    sBC(69) = "112214"
    sBC(70) = "112412"
    sBC(71) = "122114"
    sBC(72) = "122411"
    sBC(73) = "142112"
    sBC(74) = "142211"
    sBC(75) = "241211"
    sBC(76) = "221114"
    sBC(77) = "413111"
    sBC(78) = "241112"
    sBC(79) = "134111"
    sBC(80) = "111242"
    sBC(81) = "121142"
    sBC(82) = "121241"
    sBC(83) = "114212"
    sBC(84) = "124112"
    sBC(85) = "124211"
    sBC(86) = "411212"
    sBC(87) = "421112"
    sBC(88) = "421211"
    sBC(89) = "212141"
    sBC(90) = "214121"
    sBC(91) = "412121"
    sBC(92) = "111143"
    sBC(93) = "111341"
    sBC(94) = "131141"
    sBC(95) = "114113"
    sBC(96) = "114311"
    sBC(97) = "411113"
    sBC(98) = "411311"
    sBC(99) = "113141"
    sBC(100) = "114131"
    sBC(101) = "311141"
    sBC(102) = "411131"
    sBC(103) = "211412"
    sBC(104) = "211214"
    sBC(105) = "211232"
    sBC(106) = "2331112"
    
    sCA(0) = "SP"
    sCA(1) = "!"
    sCA(2) = "��"
    sCA(3) = "#"
    sCA(4) = "$"
    sCA(5) = "%"
    sCA(6) = "&"
    sCA(7) = "��"
    sCA(8) = "("
    sCA(9) = ")"
    sCA(10) = "*"
    sCA(11) = "+"
    sCA(12) = ","
    sCA(13) = "-"
    sCA(14) = "."
    sCA(15) = "/"
    sCA(16) = "0"
    sCA(17) = "1"
    sCA(18) = "2"
    sCA(19) = "3"
    sCA(20) = "4"
    sCA(21) = "5"
    sCA(22) = "6"
    sCA(23) = "7"
    sCA(24) = "8"
    sCA(25) = "9"
    sCA(26) = ":"
    sCA(27) = ";"
    sCA(28) = "<"
    sCA(29) = "="
    sCA(30) = ">"
    sCA(31) = "?"
    sCA(32) = "@"
    sCA(33) = "A"
    sCA(34) = "B"
    sCA(35) = "C"
    sCA(36) = "D"
    sCA(37) = "E"
    sCA(38) = "F"
    sCA(39) = "G"
    sCA(40) = "H"
    sCA(41) = "I"
    sCA(42) = "J"
    sCA(43) = "K"
    sCA(44) = "L"
    sCA(45) = "M"
    sCA(46) = "N"
    sCA(47) = "O"
    sCA(48) = "P"
    sCA(49) = "Q"
    sCA(50) = "R"
    sCA(51) = "S"
    sCA(52) = "T"
    sCA(53) = "U"
    sCA(54) = "V"
    sCA(55) = "W"
    sCA(56) = "X"
    sCA(57) = "Y"
    sCA(58) = "Z"
    sCA(59) = "["
    sCA(60) = "\"
    sCA(61) = "]"
    sCA(62) = "^"
    sCA(63) = "_"
    sCA(64) = "NUL"
    sCA(65) = "SOH"
    sCA(66) = "STX"
    sCA(67) = "ETX"
    sCA(68) = "EOT"
    sCA(69) = "ENQ"
    sCA(70) = "ACK"
    sCA(71) = "BEL"
    sCA(72) = "BS"
    sCA(73) = "HT"
    sCA(74) = "LF"
    sCA(75) = "VT"
    sCA(76) = "FF"
    sCA(77) = "CR"
    sCA(78) = "SO"
    sCA(79) = "SI"
    sCA(80) = "DLE"
    sCA(81) = "DC1"
    sCA(82) = "DC2"
    sCA(83) = "DC3"
    sCA(84) = "DC4"
    sCA(85) = "NAK"
    sCA(86) = "SYN"
    sCA(87) = "ETB"
    sCA(88) = "CAN"
    sCA(89) = "EM"
    sCA(90) = "SUB"
    sCA(91) = "ESC"
    sCA(92) = "FS"
    sCA(93) = "GS"
    sCA(94) = "RS"
    sCA(95) = "US"
    sCA(96) = "FNC3"
    sCA(97) = "FNC2"
    sCA(98) = "SHIFT"
    sCA(99) = "CODEC"
    sCA(100) = "CODEB"
    sCA(101) = "FNC4"
    sCA(102) = "FNCl"
    sCA(103) = "StartA"
    sCA(104) = "StartB"
    sCA(105) = "StartC"
    sCA(106) = "Stop"
        
    sCC(0) = "00"
    sCC(1) = "01"
    sCC(2) = "02"
    sCC(3) = "03"
    sCC(4) = "04"
    sCC(5) = "05"
    sCC(6) = "06"
    sCC(7) = "07"
    sCC(8) = "08"
    sCC(9) = "09"
    sCC(10) = "10"
    sCC(11) = "11"
    sCC(12) = "12"
    sCC(13) = "13"
    sCC(14) = "14"
    sCC(15) = "15"
    sCC(16) = "16"
    sCC(17) = "17"
    sCC(18) = "18"
    sCC(19) = "19"
    sCC(20) = "20"
    sCC(21) = "21"
    sCC(22) = "22"
    sCC(23) = "23"
    sCC(24) = "24"
    sCC(25) = "25"
    sCC(26) = "26"
    sCC(27) = "27"
    sCC(28) = "28"
    sCC(29) = "29"
    sCC(30) = "30"
    sCC(31) = "31"
    sCC(32) = "32"
    sCC(33) = "33"
    sCC(34) = "34"
    sCC(35) = "35"
    sCC(36) = "36"
    sCC(37) = "37"
    sCC(38) = "38"
    sCC(39) = "39"
    sCC(40) = "40"
    sCC(41) = "41"
    sCC(42) = "42"
    sCC(43) = "43"
    sCC(44) = "44"
    sCC(45) = "45"
    sCC(46) = "46"
    sCC(47) = "47"
    sCC(48) = "48"
    sCC(49) = "49"
    sCC(50) = "50"
    sCC(51) = "51"
    sCC(52) = "52"
    sCC(53) = "53"
    sCC(54) = "54"
    sCC(55) = "55"
    sCC(56) = "56"
    sCC(57) = "57"
    sCC(58) = "58"
    sCC(59) = "59"
    sCC(60) = "60"
    sCC(61) = "61"
    sCC(62) = "62"
    sCC(63) = "63"
    sCC(64) = "64"
    sCC(65) = "65"
    sCC(66) = "66"
    sCC(67) = "67"
    sCC(68) = "68"
    sCC(69) = "69"
    sCC(70) = "70"
    sCC(71) = "71"
    sCC(72) = "72"
    sCC(73) = "73"
    sCC(74) = "74"
    sCC(75) = "75"
    sCC(76) = "76"
    sCC(77) = "77"
    sCC(78) = "78"
    sCC(79) = "79"
    sCC(80) = "80"
    sCC(81) = "81"
    sCC(82) = "82"
    sCC(83) = "83"
    sCC(84) = "84"
    sCC(85) = "85"
    sCC(86) = "86"
    sCC(87) = "87"
    sCC(88) = "88"
    sCC(89) = "89"
    sCC(90) = "90"
    sCC(91) = "91"
    sCC(92) = "92"
    sCC(93) = "93"
    sCC(94) = "94"
    sCC(95) = "95"
    sCC(96) = "96"
    sCC(97) = "97"
    sCC(98) = "98"
    sCC(99) = "99"
    sCC(100) = "CODEB"
    sCC(101) = "CODEA"
    sCC(102) = "FNCl"
    sCC(103) = "StartA"
    sCC(104) = "StartB"
    sCC(105) = "StartC"
    sCC(106) = "Stop"
End Sub












