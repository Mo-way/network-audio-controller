import pytest
import netaudio.dante.device
import netaudio.dante.const

class TestCasesRest:
    """
    Testcases for device.command_* -> Suited for testing, because functions 
    with lots of logic and no side effects. 
    """

    dev: netaudio.dante.device.DanteDevice

    @pytest.fixture(autouse=True)
    def setup_teardown(self, request):
        self.dev = netaudio.dante.device.DanteDevice()

    def test_get_name_lengths(self):
        """ No idea what's the use, but just test it"""
        got = self.dev.get_name_lengths("test_name")
        want = (20, 22, 26)
        assert got == want

    def test_command_set_latency(self):
        got_upd_payload, got_service_type = self.dev.command_set_latency(2)
        want_st = netaudio.dante.const.SERVICE_ARC
        this_is_something_random_in_got = "1234"
        want_up = f"27ff0028{this_is_something_random_in_got}1101000005038205002002110010830100248219830183028306001e8480001e8480"
        assert got_service_type == want_st
        # Need to take it apart, bc function uses random sequence2
        assert got_upd_payload[:8] == want_up[:8]
        assert int(got_upd_payload[8:12], 16) in range(0, 65535)
        assert got_upd_payload[12:] == want_up[12:]

    def test_command_identify(self):
        got = self.dev.command_identify()
        want = ("ffff00200bc800000000000000000000417564696e6174650731006300000064", 
                None, 
                netaudio.dante.const.DEVICE_SETTINGS_PORT  )
        assert got == want

    def test_command_set_encoding(self):
        got = self.dev.command_set_encoding(16)
        want = ("ffff004003d700005254000000000000417564696e61746507270083000000640000000100000010", 
                None, 
                netaudio.dante.const.DEVICE_SETTINGS_PORT)
        assert got == want

        got = self.dev.command_set_encoding(24)
        want = ("ffff004003d700005254000000000000417564696e61746507270083000000640000000100000018", 
                None, 
                netaudio.dante.const.DEVICE_SETTINGS_PORT)
        assert got == want
