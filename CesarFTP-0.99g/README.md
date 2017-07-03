# Ansammlung an Skripten zum Fuzzing des CesarFTP-Programms
# 
# FuzzCesar.py              - Sendet "\n" Strings von steigender Länge an den MKD Befehl in einer Schleife
# FuzzCesarOnce.py          - Sendet einen "\n" String von angegebener Länge (argv[1]) and MKD
# FuzzCesarEIP.py           - Erweitert den String aus FuzzCesarOnce.py um einen angehängten "A" string von Variabler Länge (argv[1])
# FuzzCesarEIPoffset.py     - Ersetzt den "A" String durch einen pattern-string um das Segment im String zu finden, welches EIP überschriebt (pattern_create / pattern_offset)
# FuzzCesarEIPpayload.py    - Ersetzt den Pattern-String durch NOPS (\x90) gefolgt von einem Breakpoint (\xcc) und weiteren NOPS, um zu testen, ob EIP korrekt auf den Shellcode-Platz verweist.
# FuzzCesarEIPbadchars.py   - Ersetzt den vorherigen String durch 16-Byte-Zeilen mit Hex-Chars, um zu testen welche Zeichen nicht gesendet werden können (Bad Chars: \x00 \x5C \x89 \x8A \x0A \x0C \x0D)
# FuzzCesarEIPshellcode.py  - Ersetzt den Test-String durch den erstellten Shellcode. Hierbei handelt es sich bereits um den Exploit.

