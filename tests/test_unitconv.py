from core.unitconv import to_bytes

def test_kb_to_bytes():
    assert to_bytes("10 kB") == 10240

