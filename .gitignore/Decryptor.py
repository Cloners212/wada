import os
import signal
import sys
import urllib2

from BeautifulSoup import BeautifulSoup
from typing import Callable

print '\033[94m'
clear = lambda: os.system('clear')  # type: Callable[[], int]
clear()

p1 = "        ____                             __            "
p2 = "       / __ \___  ____________  ______  / /_____  _____"
p3 = "      / / / / _ \/ ___/ ___/ / / / __ \/ __/ __ \/ ___/"
p4 = "     / /_/ /  __/ /__/ /  / /_/ / /_/ / /_/ /_/ / /    "
p5 = "    /_____/\___/\___/_/   \__, / .___/\__/\____/_/     "
p6 = "                         /____/_/                      "
p7 = "  " \
     "                      Unsourced"
DecryptorL = p1 + "\n" + p2 + "\n" + p3 + "\n" + p4 + "\n" + p5 + "\n" + p6 + "\n" + p7 + "\n\n"

h1 = "    .-.  _"
h2 = "    | | / )"
h3 = "    | |/ /"
h4 = "   _|__ /_"
h5 = "  / __)-' )"
h6 = "  \  `(.-')"
h7 = "   > ._>-'"
h8 = "  / \/"
Phand = h1 + "\n" + h2 + "\n" + h3 + "\n" + h4 + "\n" + h5 + "\n" + h6 + "\n" + h7 + "\n" + h8 + "\n\n"

info = "Made By Unsourced, To Exit do CTLR + C\nit can take time before having a reply back"

with open('Info.txt', 'w') as f:
    for inf in info:
        f.write(str(inf))


def signal_handler(signal, frame):
    clear()
    print '\033[93m'
    print (Phand)
    print('You Exited Decryptor Bye Bye')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

print (DecryptorL)
HashInput = raw_input('Hash: ')
HashDecrypted = BeautifulSoup(urllib2.urlopen("http://www.nitrxgen.net/md5db/" + HashInput).read())
clear()
print (DecryptorL)
print "Hash :", HashInput, " = ", HashDecrypted