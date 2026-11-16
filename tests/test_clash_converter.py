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
