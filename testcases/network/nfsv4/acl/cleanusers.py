#!/usr/bin/python3
from random_gen import *
from optparse import OptionParser
import subprocess
import os
import random

test = RandomGen()
test.getUserList()
test.getGroupList()
test.cleanUsers()
test.cleanGroups()
