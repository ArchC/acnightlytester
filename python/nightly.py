
from python import utils
import os, re
from random import randint
from .html import *

class Env:
    random     = ""
    scriptroot = ""
    workspace  = ""

    htmlroot   = ""
    index      = "0"


    def __init__(self):
        self.random     = randint(0000,9999)
        self.scriptroot = os.getcwd()

    def set_workspace(self, workspace):
        self.workspace = self.resolvenv(workspace)

    def set_htmlroot(self, htmlroot):
        self.htmlroot = self.resolvenv(htmlroot)

    def resolvenv(self,cmd):
        cmd = re.sub(r"\$\{RANDOM\}", str(self.random), cmd)
        cmd = re.sub(r"\$\{SCRIPTROOT\}", str(self.scriptroot), cmd)
        return cmd

    def printenv(self):
        print("Environment: ")
        print("| workspace: "+self.workspace)
        print("| scriptroot: "+self.scriptroot)
        print("| htmlroot: "+self.htmlroot)
    
class Nightly:

    env        = None
    archc      = None
    simulators = []
    mibench    = None
    spec2006   = None

    htmlindex   = None
    htmllog     = None

    def __init__(self):
        self.env        = None
        self.archc      = None
        self.simulators = []
        self.mibench    = None
        self.spec2006   = None


    def init_htmlindex(self):
        self.htmlindex  = HTMLIndex(self.env)

    def init_htmllog(self):
        self.htmllog = HTMLLog(self.env)

    def build_and_install_archc(self):
        htmlline = self.archc.build();
        self.htmllog.appendtable1(htmlline)
        self.htmllog.close()



    def gen_and_build_simulator (self, simulator):
        archc_env = self.archc.archc_prefix+'/etc/env.sh'
        simulator.gen_and_build(archc_env);

#    def execute_simulator(self, simulator):

    


