import netaudio.dante.device


def test_command_enable_aes67():
    some_dev = netaudio.dante.device.DanteDevice()

    got = some_dev.command_enable_aes67(is_enabled=True)
    want = ('ffff002400ff22dc525400385eba0000417564696e617465073410060000006400010001', None, 8700)
    assert got == want

    got = some_dev.command_enable_aes67(is_enabled=False)
    want = ('ffff002400ff22dc525400385eba0000417564696e617465073410060000006400010000', None, 8700)
    assert got == want

def test_command_create_avio_aes67_multicast_channel():
    some_dev = netaudio.dante.device.DanteDevice()

    got = some_dev.command_create_avio_aes67_multicast_channel([1])
    want = ('2729003800ff2201000001010010000000010002000000000000000000000001000100240a00000000000000003000000000000000030000', None, 4440)
    assert got == want
    
    got = some_dev.command_create_avio_aes67_multicast_channel([2])
    want = ('2729003800ff2201000001010010000000010002000000000000000000000001000200240a00000000000000003000000000000000030000', None, 4440)
    assert got == want

    got = some_dev.command_create_avio_aes67_multicast_channel([1, 2])
    want = ('2729003c00ff220100000101001000000001000200000000000000000000000200010002002800000a00000000000000003000000000000000030000', None, 4440)
    assert got == want



