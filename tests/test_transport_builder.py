import json
import transport_builder


def test_tls_stream_settings_never_contain_allow_insecure():
    data = {'net': 'tcp', 'security': 'tls', 'address': 'example.com', 'sni': 'example.com'}
    settings = transport_builder.build_xray_settings(data)
    serialized = json.dumps(settings).lower()
    assert 'allowinsecure' not in serialized


def test_xtls_stream_settings_never_contain_allow_insecure():
    data = {'net': 'tcp', 'security': 'xtls', 'address': 'example.com', 'sni': 'example.com'}
    settings = transport_builder.build_xray_settings(data)
    serialized = json.dumps(settings).lower()
    assert 'allowinsecure' not in serialized


def test_reality_security_produces_reality_settings_not_tls():
    data = {
        'net': 'tcp', 'security': 'reality', 'address': 'example.com',
        'sni': 'example.com', 'pbk': 'somepublickey', 'sid': 'abcd', 'fp': 'chrome'
    }
    settings = transport_builder.build_xray_settings(data)
    assert settings['security'] == 'reality'
    assert 'realitySettings' in settings
    assert settings['realitySettings']['publicKey'] == 'somepublickey'
    assert 'tlsSettings' not in settings


def test_xhttp_mode_passthrough_when_present():
    data = {'net': 'xhttp', 'security': 'none', 'address': 'example.com', 'mode': 'packet-up', 'path': '/x', 'host': 'example.com'}
    settings = transport_builder.build_xray_settings(data)
    assert settings['xhttpSettings']['mode'] == 'packet-up'


def test_xhttp_mode_omitted_when_absent():
    data = {'net': 'xhttp', 'security': 'none', 'address': 'example.com', 'mode': '', 'path': '/x', 'host': 'example.com'}
    settings = transport_builder.build_xray_settings(data)
    assert 'mode' not in settings['xhttpSettings']


def test_singbox_reality_settings_shape():
    data = {
        'net': 'tcp', 'security': 'reality', 'address': 'example.com',
        'sni': 'example.com', 'pbk': 'somepublickey', 'sid': 'abcd', 'fp': 'chrome'
    }
    transport, tls = transport_builder.build_singbox_settings(data)
    assert tls['enabled'] is True
    assert tls['reality']['enabled'] is True
    assert tls['reality']['public_key'] == 'somepublickey'

def test_singbox_tls_is_not_inferred_from_common_port():
    transport, tls = transport_builder.build_singbox_settings({
        'net': 'tcp',
        'security': 'none',
        'address': 'example.com',
        'port': 443
    })
    assert tls['enabled'] is False


def test_singbox_tls_is_enabled_from_protocol_security_not_port():
    transport, tls = transport_builder.build_singbox_settings({
        'net': 'tcp',
        'security': 'tls',
        'address': 'example.com',
        'port': 8443
    })
    assert tls['enabled'] is True
    assert tls['insecure'] is False


def test_singbox_rejects_xhttp_instead_of_mislabeling_it_as_http():
    import pytest
    with pytest.raises(ValueError):
        transport_builder.map_transport_for_singbox('xhttp')


def test_singbox_rejects_kcp_instead_of_silently_dropping_transport():
    import pytest
    with pytest.raises(ValueError):
        transport_builder.map_transport_for_singbox('kcp')


def test_xray_rejects_removed_http_and_quic_mappings():
    import pytest
    for net_type in ('http', 'h2', 'h3', 'quic'):
        with pytest.raises(ValueError):
            transport_builder.build_xray_settings({
                'net': net_type,
                'security': 'tls',
                'address': 'example.com',
                'sni': 'example.com'
            })
