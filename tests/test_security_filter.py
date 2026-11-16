import json
from security_filter import SecurityFilter


def test_extract_flat_data_detects_reality():
    sb_outbound = {
        "type": "vless",
        "server": "example.com",
        "server_port": 443,
        "tls": {
            "enabled": True,
            "server_name": "example.com",
            "reality": {"enabled": True, "public_key": "abc123", "short_id": "xy"},
            "utls": {"enabled": True, "fingerprint": "chrome"}
        },
        "transport": {}
    }
    data = SecurityFilter.extract_flat_data(sb_outbound)
    assert data['security'] == 'reality'
    assert data['pbk'] == 'abc123'
    assert data['sid'] == 'xy'


def test_extract_flat_data_detects_plain_tls():
    sb_outbound = {
        "type": "vless",
        "server": "example.com",
        "server_port": 443,
        "tls": {"enabled": True, "server_name": "example.com", "utls": {"enabled": True, "fingerprint": "chrome"}},
        "transport": {}
    }
    data = SecurityFilter.extract_flat_data(sb_outbound)
    assert data['security'] == 'tls'
    assert data['pbk'] == ''


def test_extract_flat_data_detects_no_tls():
    sb_outbound = {"type": "vless", "server": "example.com", "server_port": 443, "transport": {}}
    data = SecurityFilter.extract_flat_data(sb_outbound)
    assert data['security'] == 'none'


def test_secure_ss_methods_excludes_legacy_ciphers():
    sf = SecurityFilter('in.json', 'out.json', 'xray_out.json')
    assert 'rc4-md5' not in sf.SECURE_SS_METHODS
    assert 'aes-256-gcm' in sf.SECURE_SS_METHODS


def test_singbox_to_xray_vless_reality_produces_reality_settings():
    sb_outbound = {
        "type": "vless",
        "server": "example.com",
        "server_port": 443,
        "uuid": "11111111-1111-1111-1111-111111111111",
        "flow": "xtls-rprx-vision",
        "tls": {
            "enabled": True,
            "server_name": "example.com",
            "reality": {"enabled": True, "public_key": "abc123", "short_id": "xy"},
            "utls": {"enabled": True, "fingerprint": "chrome"}
        },
        "transport": {}
    }
    sf = SecurityFilter('in.json', 'out.json', 'xray_out.json')
    outbound = sf.singbox_to_xray_vless(sb_outbound, 'proxy-1')
    assert outbound is not None
    stream = outbound['streamSettings']
    assert stream['security'] == 'reality'
    assert 'realitySettings' in stream
    serialized = json.dumps(outbound).lower()
    assert 'allowinsecure' not in serialized


def test_singbox_to_xray_vless_tls_never_has_allow_insecure():
    sb_outbound = {
        "type": "vless",
        "server": "example.com",
        "server_port": 443,
        "uuid": "11111111-1111-1111-1111-111111111111",
        "flow": "",
        "tls": {"enabled": True, "server_name": "example.com", "utls": {"enabled": True, "fingerprint": "chrome"}},
        "transport": {}
    }
    sf = SecurityFilter('in.json', 'out.json', 'xray_out.json')
    outbound = sf.singbox_to_xray_vless(sb_outbound, 'proxy-1')
    serialized = json.dumps(outbound).lower()
    assert 'allowinsecure' not in serialized

def test_secure_filter_allows_encrypted_shadowsocks_without_tls_object():
    sf = SecurityFilter('in.json', 'out.json', 'xray_out.json')
    outbound = {
        "type": "shadowsocks",
        "tag": "ss-secure",
        "method": "aes-256-gcm",
        "password": "secret"
    }
    tls_settings = outbound.get('tls')
    assert tls_settings is None
    assert outbound['method'] in sf.SECURE_SS_METHODS


def test_secure_filter_rejects_vless_without_explicit_tls_even_on_443():
    sf = SecurityFilter('in.json', 'out.json', 'xray_out.json')
    outbound = {
        "type": "vless",
        "tag": "vless-plain",
        "server": "example.com",
        "server_port": 443,
        "tls": {"enabled": False}
    }
    assert outbound['tls']['enabled'] is not True


def test_secure_filter_rejects_disabled_certificate_validation():
    outbound = {
        "type": "trojan",
        "tag": "trojan-insecure",
        "tls": {"enabled": True, "insecure": True}
    }
    assert outbound['tls']['insecure'] is True
