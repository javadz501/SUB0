import json

from config_to_singbox import ConfigToSingbox


def test_mixed_inbound_binds_to_loopback_and_udp_is_not_globally_rejected(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    configs = tmp_path / "configs"
    configs.mkdir()
    (configs / "proxy_configs_tested.txt").write_text(
        "vless://11111111-1111-1111-1111-111111111111@example.com:443?security=tls&type=ws&path=%2Fedge&host=example.com&sni=example.com#test\n",
        encoding="utf-8",
    )

    ConfigToSingbox().process_configs()

    generated = json.loads((configs / "singbox_configs_all.json").read_text(encoding="utf-8"))
    mixed = next(item for item in generated["inbounds"] if item["tag"] == "mixed-in")
    assert mixed["listen"] == "127.0.0.1"
    assert not any(
        rule.get("network") == "udp" and rule.get("action") == "reject"
        for rule in generated["route"]["rules"]
    )


def test_clash_rules_do_not_block_all_udp_traffic():
    from singbox_to_clash import create_clash_config

    config = create_clash_config([], [])
    assert "NETWORK,udp,REJECT" not in config["rules"]
    assert config["allow-lan"] is False
