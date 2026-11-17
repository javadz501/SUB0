import argparse
import copy
import json
from pathlib import Path

from config import ProxyConfig
from fetch_configs import ConfigFetcher

EXCLUDED_TYPES = {"selector", "urltest", "direct", "block", "dns"}
UTILITY_TYPES = {"direct", "block", "dns"}


def split_xray(input_path: str, maximum_path: str, standard_path: str, limit: int) -> None:
    candidate_lines = Path(input_path).read_text(encoding="utf-8").splitlines()
    candidate_configs = [
        line.strip() for line in candidate_lines
        if line.strip() and not line.lstrip().startswith("//") and not line.lstrip().startswith("#")
    ]

    maximum_lines = Path(maximum_path).read_text(encoding="utf-8").splitlines()
    headers = []
    maximum_configs = []
    for line in maximum_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("//") or stripped.startswith("#"):
            if not maximum_configs:
                headers.append(line)
            continue
        maximum_configs.append(line)

    if not maximum_configs:
        raise ValueError("Xray tester produced no working configurations.")

    # Reapply the normal-mode protocol caps to the already-fetched candidate pool.
    # This keeps the standard feed's selection policy separate from the max feed.
    normal_config = ProxyConfig()
    normal_fetcher = ConfigFetcher(normal_config)
    standard_candidates = normal_fetcher.balance_protocols(sorted(set(candidate_configs)))
    standard_candidates = standard_candidates[:limit]
    maximum_set = set(maximum_configs)
    standard_configs = [item for item in standard_candidates if item in maximum_set]

    if not standard_configs:
        raise ValueError("No standard-mode candidates survived the maximum Xray test pass.")

    Path(maximum_path).write_text("\n".join(headers + ([""] if headers else []) + maximum_configs) + "\n", encoding="utf-8")
    Path(standard_path).write_text("\n".join(headers + ([""] if headers else []) + standard_configs) + "\n", encoding="utf-8")
    print(f"Maximum Xray set: {len(maximum_configs)} configs")
    print(f"Standard Xray set: {len(standard_configs)} configs (target: {limit})")


def subset_singbox(maximum_tested_path: str, standard_source_path: str, standard_output_path: str) -> None:
    maximum = json.loads(Path(maximum_tested_path).read_text(encoding="utf-8"))
    standard_source = json.loads(Path(standard_source_path).read_text(encoding="utf-8"))

    maximum_outbounds = maximum.get("outbounds")
    standard_outbounds = standard_source.get("outbounds")
    if not isinstance(maximum_outbounds, list) or not isinstance(standard_outbounds, list):
        raise ValueError("Invalid sing-box outbounds structure.")

    standard_tags = {
        item.get("tag")
        for item in standard_outbounds
        if isinstance(item, dict)
        and item.get("type") not in EXCLUDED_TYPES
        and item.get("tag")
    }
    tested_tags = {
        item.get("tag")
        for item in maximum_outbounds
        if isinstance(item, dict)
        and item.get("type") not in EXCLUDED_TYPES
        and item.get("tag")
    }
    selected_tags = standard_tags & tested_tags
    if not selected_tags:
        raise ValueError("No standard sing-box proxies survived the maximum-mode test.")

    group_tags = {
        item.get("tag")
        for item in maximum_outbounds
        if isinstance(item, dict) and item.get("type") in {"selector", "urltest"} and item.get("tag")
    }
    standard = copy.deepcopy(maximum)
    filtered = []

    for outbound in maximum_outbounds:
        if not isinstance(outbound, dict):
            continue
        kind = outbound.get("type")
        tag = outbound.get("tag")

        if kind == "selector":
            item = copy.deepcopy(outbound)
            item["outbounds"] = [
                target for target in item.get("outbounds", [])
                if target in selected_tags or target in group_tags or target in UTILITY_TYPES
            ]
            if item["outbounds"]:
                filtered.append(item)
        elif kind == "urltest":
            item = copy.deepcopy(outbound)
            item["outbounds"] = [
                target for target in item.get("outbounds", [])
                if target in selected_tags
            ]
            if item["outbounds"]:
                filtered.append(item)
        elif kind in UTILITY_TYPES:
            filtered.append(outbound)
        elif tag in selected_tags:
            filtered.append(outbound)

    actual_tags = {
        item.get("tag") for item in filtered
        if isinstance(item, dict) and item.get("type") not in EXCLUDED_TYPES
    }
    if not actual_tags:
        raise ValueError("Filtered standard sing-box output contains no proxy outbounds.")

    standard["outbounds"] = filtered
    Path(standard_output_path).write_text(
        json.dumps(standard, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Standard sing-box set: {len(actual_tags)} tested proxies")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build standard and maximum proxy output sets.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    split_parser = subparsers.add_parser("split-xray")
    split_parser.add_argument("--input", required=True)
    split_parser.add_argument("--maximum", required=True)
    split_parser.add_argument("--standard", required=True)
    split_parser.add_argument("--limit", required=True, type=int)

    subset_parser = subparsers.add_parser("subset-singbox")
    subset_parser.add_argument("--maximum-tested", required=True)
    subset_parser.add_argument("--standard-source", required=True)
    subset_parser.add_argument("--standard-output", required=True)

    args = parser.parse_args()
    if args.command == "split-xray":
        if args.limit < 1:
            raise ValueError("The standard configuration limit must be positive.")
        split_xray(args.input, args.maximum, args.standard, args.limit)
    elif args.command == "subset-singbox":
        subset_singbox(args.maximum_tested, args.standard_source, args.standard_output)


if __name__ == "__main__":
    main()
