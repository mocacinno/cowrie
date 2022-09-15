from __future__ import annotations

import getopt

from cowrie.shell.command import HoneyPotCommand

commands = {}


class Command_bitcoin_cli(HoneyPotCommand):
     def help(self, noargs = 0):
          output = """
Bitcoin Core RPC client version v23.0.0 Modded to simplify for wallet use

Usage:  bitcoin-cli <command> [params]  Send command to Bitcoin Core
or:     bitcoin-cli help                List commands

== Wallet ==
getbalance 
getnewaddress 
getunconfirmedbalance
sendtoaddress "address" amount 

          """
          self.write(output + "\n")
          if noargs == 1:
               self.write("Error: too few parameters\n\n")


     def getbalance(self):
          self.write("15.02481357\n")

     def getnewaddress(self):
          self.write("bc1qw3a554f9k3any23huzre5x6urvl6l5fkwkzffn\n")

     def getunconfirmedbalance(self):
          self.write("0.00000000\n")
     
     def sendtoaddress(self):
          self.write("8c40124f8a09f28cd31515969350c26564e1ffb6a56b02f7d5a7524289822ca7\n")

     def call(self):
          try:
               opts, args = getopt.gnu_getopt(self.args, "h", ["help",  "getbalance", "getnewaddress", "getunconfirmedbalance", "sendtoaddress" ] )
               self.write("debug: %s %s \n\n" % (opts, args))
          except getopt.GetoptError:
               self.help()
               return

          if not opts and not args:
               self.help(1)
               return

          if "getbalance" in args:
               self.getbalance()

          if "help" in args:
               self.help()
          
          if "getnewaddress" in args:
               self.getnewaddress()
          
          if "getunconfirmedbalance" in args:
               self.getunconfirmedbalance()
          
          if args[0] == "sendtoaddress":
               self.sendtoaddress()

          for o, a in opts:
               if o in ("--help") or o in ("-h") or o in ("help"):
                    self.help()
                    return
     

commands["/usr/local/bin/bitcoin-cli"] = Command_bitcoin_cli
commands["bitcoin-cli"] = Command_bitcoin_cli
