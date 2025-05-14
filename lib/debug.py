#!/usr/bin/env python3

from dog import Dog
import ipdb

ipdb.set_trace()
ipdb> Dog("Fido", "Corgi")
<dog.Dog object at 0x1051dc700>
ipdb> Dog("Fido the Pug who likes to roll in the mud", "Pug")
*** ValueError: Name must be string between 1 and 25 characters.
