import pytest
import netaudio.dante.device
import netaudio.dante.const

class TestCasesConfig:
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
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff0028xxxx1101000005038205002002110010830100248219830183028306001e8480001e8480",
            got=self.dev.command_set_latency(2)
        )

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

    def test_command_set_gain_level(self):
        # Use function (and e.g. dict for values), if adding more tests
        got = self.dev.command_set_gain_level(channel_number=1, gain_level=1, device_type="input")
        want = ("ffff0034034400005254000000000000417564696e6174650727100a0000000000010001000c0010010200000000000100000001", 
                None, 
                netaudio.dante.const.DEVICE_SETTINGS_PORT)
        assert got == want

        got = self.dev.command_set_gain_level(channel_number=2, gain_level=6, device_type="output")
        want = ("ffff0034032600005254000000000000417564696e6174650727100a0000000000010001000c0010020100000000000200000006", 
                None, 
                netaudio.dante.const.DEVICE_SETTINGS_PORT)
        assert got == want

    def test_command_set_sample_rate(self):
        got = self.dev.command_set_sample_rate(44100)
        want = ("ffff002803d400005254000000000000417564696e6174650727008100000064000000010000ac44",
                None, 
                netaudio.dante.const.DEVICE_SETTINGS_PORT)
        assert got == want

        got = self.dev.command_set_sample_rate(192000)
        want = ("ffff002803d400005254000000000000417564696e6174650727008100000064000000010002ee00",
                None, 
                netaudio.dante.const.DEVICE_SETTINGS_PORT)
        assert got == want

    def test_command_add_subscription(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff003dxxxx30100000020100010034003800000000000000000000000000000000000000000000000000000000000000000000636831006176696f00",
            got=self.dev.command_add_subscription(rx_channel_number=1, tx_channel_name="ch1", tx_device_name="avio")
        )

    def test_command_remove_subscription(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff0010xxxx30140000000100000001",
            got=self.dev.command_remove_subscription(rx_channel=1)
        )

    def test_command_device_info(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff000axxxx10030000",
            got=self.dev.command_device_info()
        )

    def test_command_devic_name(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff000axxxx10020000",
            got=self.dev.command_device_name()        )

    def test_command_channel_count(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff000axxxx10000000",
            got=self.dev.command_channel_count()
        )

    def test_command_set_name(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff0010xxxx100100004d6f72747900",
            got=self.dev.command_set_name("Morty")
        )

        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff0010xxxx10010000616263646500",
            got=self.dev.command_set_name("abcde")
        )

    def test_command_reset_name(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff000axxxx10010000",
            got=self.dev.command_reset_name()
        )

    def test_command_reset_channel_name(self):
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff0015xxxx300100000201000500140000000000",
            got=self.dev.command_reset_channel_name(
                channel_type="rx",
                channel_number=5
            )
        )
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff0015xxxx300100000201000200140000000000",
            got=self.dev.command_reset_channel_name(
                channel_type="rx",
                channel_number=2
            )
        )
        self.__command_string_helper(
            want_service=netaudio.dante.const.SERVICE_ARC,
            want_payload="27ff0019xxxx20130000020100000002001800000000000000",
            got=self.dev.command_reset_channel_name(
                channel_type="tx",
                channel_number=2
            )
        )

    # def test_command_(self):
    #     self.__command_string_helper(
    #         want_service=netaudio.dante.const.SERVICE_ARC,
    #         want_payload="27ff0010xxxx30140000000100000001",
    #         got=self.dev.
    #     )

    # def test_command_(self):
    #     self.__command_string_helper(
    #         want_service=netaudio.dante.const.SERVICE_ARC,
    #         want_payload="27ff0010xxxx30140000000100000001",
    #         got=self.dev.
    #     )

    def __command_string_helper(self, want_service: str, want_payload: str, got: tuple):
        got_payload, got_service = got
        assert got_service == want_service
        assert got_payload[:8] == want_payload[:8]
        # Command_string uses a random sequence2 value on every call
        assert int(got_payload[8:12], 16) in range(0, 65535)
        assert got_payload[12:] == want_payload[12:]