
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
CONFIGS = ROOT / "configs"

START_MARKER = "<!-- SUB0_COUNTS_START -->"
END_MARKER = "<!-- SUB0_COUNTS_END -->"

EXCLUDED_SINGBOX_TYPES = {
    "selector",
    "urltest",
    "direct",
    "block",
    "dns",
}

def count_xray():
    path = CONFIGS / "proxy_configs_tested.txt"
    lines = path.read_text(encoding="utf-8").splitlines()

    return sum(
        1 for line in lines
        if line.strip()
        and not line.lstrip().startswith("#")
        and not line.lstrip().startswith("//")
    )

def count_singbox(filename):
    path = CONFIGS / filename
    data = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        raise ValueError(f"Invalid sing-box structure: {filename}")

    outbounds = data.get("outbounds")

    if not isinstance(outbounds, list):
        raise ValueError(f"Missing outbounds list: {filename}")

    proxies = [
        item for item in outbounds
        if isinstance(item, dict)
        and item.get("type") not in EXCLUDED_SINGBOX_TYPES
    ]

    if not proxies:
        raise ValueError(f"No proxy outbounds found: {filename}")

    return len(proxies)

def count_clash(filename):
    path = CONFIGS / filename

    # Current generated Clash files use JSON-compatible YAML.
    data = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        raise ValueError(f"Invalid Clash structure: {filename}")

    proxies = data.get("proxies")

    if not isinstance(proxies, list):
        raise ValueError(f"Missing proxies list: {filename}")

    return len(proxies)

def main():
    counts = {
        "xray": count_xray(),
        "singbox_tested": count_singbox(
            "singbox_configs_tested.json"
        ),
        "singbox_secure": count_singbox(
            "singbox_configs_secure.json"
        ),
        "clash_tested": count_clash(
            "clash_configs_tested.yaml"
        ),
        "clash_secure": count_clash(
            "clash_configs_secure.yaml"
        ),
    }

    rows = [
        f"| **Xray Tested** | `TXT` | {counts['xray']} | [↗ Open Subscription](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/proxy_configs_tested.txt) |",
        f"| **sing-box Tested** | `JSON` | {counts['singbox_tested']} | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/singbox_configs_tested.json) |",
        f"| **sing-box Secure** | `JSON` | {counts['singbox_secure']} | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/singbox_configs_secure.json) |",
        f"| **Clash Tested** | `YAML` | {counts['clash_tested']} | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/clash_configs_tested.yaml) |",
        f"| **Clash Secure** | `YAML` | {counts['clash_secure']} | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/clash_configs_secure.yaml) |",
    ]

    content = README.read_text(encoding="utf-8")

    if content.count(START_MARKER) != 1:
        raise ValueError("README must contain exactly one start marker.")

    if content.count(END_MARKER) != 1:
        raise ValueError("README must contain exactly one end marker.")

    pattern = re.compile(
        re.escape(START_MARKER)
        + r".*?"
        + re.escape(END_MARKER),
        re.DOTALL,
    )

    replacement = (
        START_MARKER
        + "\n"
        + "\n".join(rows)
        + "\n"
        + END_MARKER
    )

    updated = pattern.sub(replacement, content)

    if updated == content:
        print("Subscription counts are already up to date.")
        return

    README.write_text(updated, encoding="utf-8")

    print("Updated subscription configuration counts:")
    for name, value in counts.items():
        print(f"{name}: {value}")

if __name__ == "__main__":
    main()
