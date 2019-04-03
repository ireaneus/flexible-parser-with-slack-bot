import pytest
from pytest_mock import mocker

from lighthouse.downtime_commands import DowntimeCommands
from lighthouse.format import FormatFor


class TestDowntimeCommands():
    def setup(self):
        self.api = 'NOT THE ACTUAL API INTERFACE'
        self.parser = DowntimeCommands(self.api)

    def test_ping(self):
        assert self.parser._ping(
        ) == "This is a journey into Check Mk's downtime API commands."

    def test_calling_ping(self):
        assert self.parser.handle_command(
            'ping'
        ) == "This is a journey into Check Mk's downtime API commands."

    @pytest.mark.skip('Mock to prevent exit from local')
    def test_return_of_all_downtime(self):
        """
        `downtime all`
        should be passed to checkmk and return successfully
        """
        block = self.parser.handle_command('all')
        result = [[
            "host", "service_description", "downtime_origin",
            "downtime_author", "downtime_entry_time", "downtime_start_time",
            "downtime_end_time", "downtime_fixed", "downtime_duration",
            "downtime_recurring", "downtime_comment"
        ]]
        assert block == FormatFor.slack_json_as_code_blob(result)

    @pytest.mark.skip('Need to mock call to server, prevent exit from class')
    def test_set_downtime(self):
        block = self.parser.handle_command(
            'set sewrndb26.mgmt.taketwo.online "down me!" 120')
        """
        `downtime set <hostname> <message> <hours>`

        should be passed to checkmk and set downtime on the server
        """
        assert False

    @pytest.mark.skip(reason='Not Implemented yet get_downtime')
    def test_get_downtime(self):
        assert False

    @pytest.mark.skip(reason='Not Implemented yet get_downtime')
    def test_get_historical_downtimes(self):
        assert False

    @pytest.mark.skip(reason='Not Implemented yet get_downtime')
    def test_get_comments(self, mocker):
        with mocker.patch(
                'lighthouse.downtime_commands.DowntimeCommands.get_comments'):
            block = self.parser.handle_command('')
            assert block == False
