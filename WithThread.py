import threading

import threading
from WithoutThread import *

t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)

t1.start()
t2.start()
