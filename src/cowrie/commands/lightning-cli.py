from __future__ import annotations

import getopt

from cowrie.shell.command import HoneyPotCommand

commands = {}


class Command_lightning_cli(HoneyPotCommand):
     def help(self, noargs = 0):
          output = """
Modded lightning-cli only for wallet functionality
=== bitcoin ===

newaddr [addresstype]
    Get a new {bech32, p2sh-segwit} (or all) address to fund a channel (default is bech32)


=== payment ===

sendpay bolt11 [description]
    Decode {bolt11}, and pay


=== utility ===

getinfo
    Show information about this node

listfunds [spent]
    Show available funds from the internal wallet


---
run `lightning-cli help <command>` for more information on a specific command


          """
          self.write(output + "\n")
          if noargs == 1:
               self.write("Error: too few parameters\n\n")



     def newaddr(self):
          self.write("bc1qw3a554f9k3any23huzre5x6urvl6l5fkwkzffn\n")

     def sendpay(self):
          self.write("payment sent\n")

     def getinfo(self):
          output = """
{
   "id": "03301e633b25d769377bf75ce6b6ed2ec570270bc06c8c02bf33c5bd2aa47da098",
   "alias": "mocacinno",
   "color": "03301e",
   "num_peers": 14,
   "num_pending_channels": 0,
   "num_active_channels": 12,
   "num_inactive_channels": 1,
   "address": [
      {
         "type": "ipv4",
         "address": "193.70.78.148",
         "port": 9735
      },
      {
         "type": "torv3",
         "address": "plbhi3lrp2y3jjqnlcdugorynhd43qs7rovafehar4mgqhfyn22yuzyd.onion",
         "port": 9735
      }
   ],
   "binding": [
      {
         "type": "ipv4",
         "address": "193.70.78.148",
         "port": 9735
      },
      {
         "type": "ipv4",
         "address": "127.0.0.1",
         "port": 9735
      }
   ],
   "version": "v0.11.0.1-231-gddf8fbd-modded",
   "blockheight": 754183,
   "network": "bitcoin",
   "msatoshi_fees_collected": 135225,
   "fees_collected_msat": "135225msat",
   "lightning-dir": "/root/.lightning/bitcoin",
   "our_features": {
      "init": "088000080269a2",
      "node": "888000080269a2",
      "channel": "",
      "invoice": "02000000024100"
   }
}



          """
          self.write(output + "\n")
     
     def listfunds(self):
          output = """
{
   "outputs": [],
   "channels": [
      {
         "peer_id": "02ad6fb8d693dc1e4569bcedefadf5f72a931ae027dc0f0c544b34c1c6f3b9a02b",
         "connected": false,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "551186x1779x0",
         "channel_sat": 85017,
         "our_amount_msat": "85017000msat",
         "channel_total_sat": 100000,
         "amount_msat": "100000000msat",
         "funding_txid": "71a3effc83b1b5664afb6103649b8c6f98c572ffe5f1a8a8abd6727d937cb40b",
         "funding_output": 0
      },
      {
         "peer_id": "0214924c2304fc7505afb3c5a515f4ac15a2404c9751e0cb186182fdc07e8486fe",
         "connected": false,
         "state": "ONCHAIN",
         "short_channel_id": "558649x1314x1",
         "channel_sat": 0,
         "our_amount_msat": "0msat",
         "channel_total_sat": 4499630,
         "amount_msat": "4499630000msat",
         "funding_txid": "62686ac6dc71fc46c1b337a70bb2ab7f5e010cdf0764d0d9d5bf27050acd6791",
         "funding_output": 1
      },
      {
         "peer_id": "02870c077874b6c294f6351511fd2eb239754ebfe91f6c9eccc980c94cecd5fa07",
         "connected": false,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "562081x577x0",
         "channel_sat": 0,
         "our_amount_msat": "0msat",
         "channel_total_sat": 1000000,
         "amount_msat": "1000000000msat",
         "funding_txid": "0e2a8c0d302efb038e2c5009ed6bbcbcf443b41e281769d4a5c1afa92d2da025",
         "funding_output": 0
      },
      {
         "peer_id": "0314d746a8d1bb4ade7bc4223d9bd33069552c946b40947e0b7ddbccea66bd39da",
         "connected": false,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "585138x1779x1",
         "channel_sat": 0,
         "our_amount_msat": "0msat",
         "channel_total_sat": 58108,
         "amount_msat": "58108000msat",
         "funding_txid": "2a9e65ad2fad45741e5d07ce674e4edf804316029c4cbdbdb595bc9fffb24d48",
         "funding_output": 1
      },
      {
         "peer_id": "03d7c2045223dea00373459154b43d0baa140bdb0a618f7f81a566c3f928ed1881",
         "connected": false,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "593441x2317x0",
         "channel_sat": 0,
         "our_amount_msat": "0msat",
         "channel_total_sat": 100000,
         "amount_msat": "100000000msat",
         "funding_txid": "3fc6e5b9301a4d8588e41a29b47fcf8c026e1eec249f9f9b43052ea3e6fe1a00",
         "funding_output": 0
      },
      {
         "peer_id": "03abf6f44c355dec0d5aa155bdbdd6e0c8fefe318eff402de65c6eb2e1be55dc3e",
         "connected": true,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "612761x1199x1",
         "channel_sat": 30113,
         "our_amount_msat": "30113000msat",
         "channel_total_sat": 91000,
         "amount_msat": "91000000msat",
         "funding_txid": "7a3df34221a3ea4ccb77c9658cc22bc84fa049ec521f081c119e7f2962e9f8f6",
         "funding_output": 1
      },
      {
         "peer_id": "0228c3cf3ffbd9cbd228d010cad1216a44a5c7b7effd343739ae5d5f36dd1c59af",
         "connected": true,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "668219x771x0",
         "channel_sat": 0,
         "our_amount_msat": "0msat",
         "channel_total_sat": 50000,
         "amount_msat": "50000000msat",
         "funding_txid": "dc81cff67e6796966bb3ba4816bf7e5fd514c9f58adfe6f0e0ec07f749e2bcf8",
         "funding_output": 0
      },
      {
         "peer_id": "02a7f9c7f87d03be03aeee26beafed72f1a8323d111fa1ca7d11faf16374e38e35",
         "connected": false,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "673463x1870x0",
         "channel_sat": 0,
         "our_amount_msat": "0msat",
         "channel_total_sat": 250000,
         "amount_msat": "250000000msat",
         "funding_txid": "f3f52ffe165cf598921b012aa815ebde054dd8e9db7d7d917176a5a747e61323",
         "funding_output": 0
      },
      {
         "peer_id": "02247d9db0dfafea745ef8c9e161eb322f73ac3f8858d8730b6fd97254747ce76b",
         "connected": true,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "685982x843x0",
         "channel_sat": 6143,
         "our_amount_msat": "6143000msat",
         "channel_total_sat": 65396,
         "amount_msat": "65396000msat",
         "funding_txid": "703e0124d180f8bb54d66c93c5e0c430b9c7242f133ec39913b9f9cd88795c12",
         "funding_output": 0
      },
      {
         "peer_id": "03612b1f6c0a7f3580de5d91ce29fad36dcf871225d4b5ac116b422836da974bc3",
         "connected": true,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "715110x796x0",
         "channel_sat": 30982,
         "our_amount_msat": "30982000msat",
         "channel_total_sat": 100000,
         "amount_msat": "100000000msat",
         "funding_txid": "68d9ccd5fb26f1ab692c781eb92c3744a8ba8fe0a4f6f855fd13569ddb534830",
         "funding_output": 0
      },
      {
         "peer_id": "02058a29920854e5088ade34a0f89ca9c89464d6d6595c2942eb13047580a1192b",
         "connected": true,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "715245x568x0",
         "channel_sat": 90002,
         "our_amount_msat": "90002000msat",
         "channel_total_sat": 100000,
         "amount_msat": "100000000msat",
         "funding_txid": "d003f8b0732a351c9fea7f939ec9fbe07588613c82d6adc4a4967c94435bc251",
         "funding_output": 0
      },
      {
         "peer_id": "035ba756d909689e5d077fdb7b65f5485e1a63553b5d585b7f6ff128e66e1f26d6",
         "connected": true,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "719739x1342x0",
         "channel_sat": 336559,
         "our_amount_msat": "336559000msat",
         "channel_total_sat": 1000000,
         "amount_msat": "1000000000msat",
         "funding_txid": "fb778dcb7f247357b90653499159645ac2bb07dd9b64e1c015eff56ef978e744",
         "funding_output": 0
      },
      {
         "peer_id": "023f1fe1ac6ce509a12ef38bab072ad1685658b04edfa363de56558245ef768e9f",
         "connected": false,
         "state": "CHANNELD_NORMAL",
         "short_channel_id": "731376x1071x0",
         "channel_sat": 1200,
         "our_amount_msat": "1200000msat",
         "channel_total_sat": 60000,
         "amount_msat": "60000000msat",
         "funding_txid": "1c794362c214339d43ebc8aed15fb3184c7c9ad45e891cb5556d7d99a312b847",
         "funding_output": 0
      }
   ]
}

          """
          self.write(output + "\n")

     def call(self):
          try:
               opts, args = getopt.gnu_getopt(self.args, "h", ["help",  "newaddr", "sendpay", "getinfo", "listfunds" ] )
               #self.write("debug: %s %s \n\n" % (opts, args))
          except getopt.GetoptError:
               self.help()
               return

          if not opts and not args:
               self.help(1)
               return

          if "help" in args:
               self.help()
          
          if "newaddr" in args:
               self.newaddr()
          
          if "sendpay" in args:
               self.sendpay()
          
          if "getinfo" in args:
               self.getinfo()
          
          if "listfunds" in args:
               self.listfunds()


          for o, a in opts:
               if o in ("--help") or o in ("-h") or o in ("help"):
                    self.help()
                    return
     

commands["/usr/local/bin/lightning-cli"] = Command_lightning_cli
commands["lightning-cli"] = Command_lightning_cli
