   streamreader = pynmea2.NMEAStreamReader(input)
    while 1:
        for msg in streamreader.next():
        print msg
