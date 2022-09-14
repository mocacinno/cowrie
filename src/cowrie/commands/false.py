from __future__ import annotations

from cowrie.shell.command import HoneyPotCommand

commands = {}

class Command_false(HoneyPotCommand):
    def start(self):
        self.exit()


commands["/bin/false"] = Command_false
commands["false"] = Command_false
