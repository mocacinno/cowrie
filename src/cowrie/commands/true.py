from __future__ import annotations

from cowrie.shell.command import HoneyPotCommand

commands = {}

class Command_true(HoneyPotCommand):
    def call(self):
        self.exit()


commands["/bin/true"] = Command_true
commands["true"] = Command_true
