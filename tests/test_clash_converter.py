import singbox_to_clash


def test_hysteria2_clash_conversion_verifies_certificates_by_default():
    proxy = singbox_to_clash.singbox_outbound_to_clash_proxy({
        "type": "hysteria2",
        "tag": "hy2-test",
        "server": "example.com",
        "server_port": 443,
        "password": "secret",
        "tls": {"enabled": True, "server_name": "example.com"}
    })
    assert proxy is not None
    assert proxy["skip-cert-verify"] is False


def test_clash_conversion_preserves_explicit_insecure_flag():
    proxy = singbox_to_clash.singbox_outbound_to_clash_proxy({
        "type": "hysteria2",
        "tag": "hy2-test",
        "server": "example.com",
        "server_port": 443,
        "password": "secret",
        "tls": {"enabled": True, "insecure": True}
    })
    assert proxy is not None
    assert proxy["skip-cert-verify"] is True


def test_clash_skips_transports_without_a_lossless_mapping():
    for transport in ('xhttp', 'splithttp', 'kcp', 'quic'):
        proxy = singbox_to_clash.singbox_outbound_to_clash_proxy({
            "type": "vless",
            "tag": "test",
            "server": "example.com",
            "server_port": 443,
            "uuid": "11111111-1111-1111-1111-111111111111",
            "transport": {"type": transport},
            "tls": {"enabled": True, "server_name": "example.com"}
        })
        assert proxy is None


def test_trojan_httpupgrade_transport_is_preserved():
    proxy = singbox_to_clash.singbox_outbound_to_clash_proxy({
        "type": "trojan",
        "tag": "trojan-httpupgrade",
        "server": "example.com",
        "server_port": 443,
        "password": "secret",
        "transport": {"type": "httpupgrade", "path": "/edge", "host": "example.com"},
        "tls": {"enabled": True, "server_name": "example.com"}
    })
    assert proxy["network"] == "httpupgrade"
    assert proxy["httpupgrade-opts"]["path"] == "/edge"
