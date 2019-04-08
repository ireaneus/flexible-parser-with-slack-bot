from unittest.mock import Mock

import pytest

from lighthouse.host_commands import HostCommands


class TestHostsCommands():
    def setup(self):
        self.api = Mock()
        self.parser = HostCommands(self.api)

    def test_ping(self):
        assert self.parser._ping(
        ) == "This is a journey into Check Mk's host API commands."

    def test_calling_ping(self):
        assert self.parser.handle_command(
            'ping') == "This is a journey into Check Mk's host API commands."

    @pytest.mark.skip()
    def test_command_block(self):
        assert [*self.parser._commands] == ['ping', 'help', 'add', 'edit']

    def test_add_host_with_folder(self):
        """
        `host add my-host folder-name`
        should be passed to checkmk and return successfully
        """

        self.parser.handle_command('add my-host folder-name')
        self.api.add_host.assert_called_with(
            ('my-host', 'folder-name', None, None, None), )
        # self.api.add_host.assert_called_with(['my-host', 'folder-name'])

    def test_edit_host_with_ipaddress(self):
        """
        `` should be passed to checkmk and return the get all hosts
        from GetCommands processor
        """

        self.parser.handle_command('edit my-host-name ipaddress')
        self.api.edit_host.assert_called_with('my-host-name', 'ipaddress')
