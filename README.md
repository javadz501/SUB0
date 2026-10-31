 <p align="center">
  <img src="https://github.com/javadz501/SUB0/blob/main/SUB0.jpg" alt="SUB0 Logo" width="220">
</p>

<h1 align="center">「SUB0」- Free Proxy Configuration Collector</h1>

<p align="center">
  <strong>Collect. Test. Publish.</strong>
  <br>
  Automated Public Proxy Collection, Protocol Testing, and Subscription Publishing.
</p>

<p align="center">
  <a href="https://github.com/javadz501/SUB-Independent/actions">
    <img src="https://img.shields.io/badge/GitHub%20Actions-Automated-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
  </a>
  <img src="https://img.shields.io/badge/Xray-Supported-6366F1?style=for-the-badge" alt="Xray">
  <img src="https://img.shields.io/badge/sing--box-Supported-00BFA5?style=for-the-badge" alt="sing-box">
  <img src="https://img.shields.io/badge/Clash-Supported-8B5CF6?style=for-the-badge" alt="Clash">
  <img src="https://img.shields.io/badge/Cost-Free-22C55E?style=for-the-badge" alt="Free">
</p>

---

## ⚡ Overview

**「SUB0」** Is an Automated Pipeline That Collects Publicly Available Proxy Configurations, Tests Supported Protocols, Filters Results, and Publishes Organized Configuration Files.

The goal is simple: **Collect Useful Configurations, Validate What Can Be Tested, and Make The Results Easy to Access.**

| Capability | Description |
|---|---|
| Automated Collection | Retrieves Configurations from Public Sources |
| Protocol Testing | Tests Supported Configurations Using Available Tools |
| Duplicate Filtering | Reduces Duplicate Entries in Generated Outputs |
| Multiple Formats | Publishes Outputs for Xray, Sing-box, and Clash |
| Scheduled Processing | Runs Through GitHub Actions |
| Public Subscriptions | Provides Direct Raw Links to Generated Files |

## 🔗 Configuration Subscriptions

Choose the output compatible with your client and import the corresponding URL.

| Configuration | Format | Subscription |
|:--|:--:|:--|
| **Xray Tested** | `TXT` | [↗ Open Subscription](https://raw.githubusercontent.com/javadz501/SUB-Independent/main/configs/proxy_configs_tested.txt) |
| **sing-box Tested** | `JSON` | [↗ Open Configurations](https://raw.githubusercontent.com/javadz501/SUB-Independent/main/configs/singbox_configs_tested.json) |
| **sing-box Secure** | `JSON` | [↗ Open Configurations](https://raw.githubusercontent.com/javadz501/SUB-Independent/main/configs/singbox_configs_secure.json) |
| **Clash Tested** | `YAML` | [↗ Open Configurations](https://raw.githubusercontent.com/javadz501/SUB-Independent/main/configs/clash_configs_tested.yaml) |
| **Clash Secure** | `YAML` | [↗ Open Configurations](https://raw.githubusercontent.com/javadz501/SUB-Independent/main/configs/clash_configs_secure.yaml) |

> **Note:** Subscription links depend on the corresponding files being present and up to date on the `main` branch. Available configurations and client compatibility may change between runs.

## 🧭 Quick Start

**01 — Choose your client**

Select a compatible client, such as Xray, sing-box, or Clash.

**02 — Select a subscription**

Choose the appropriate format from the table above.

**03 — Import the URL**

Paste the raw subscription URL into your client's subscription manager. If remote subscriptions are unsupported, download the file and import it manually.

**04 — Refresh when needed**

Refresh the subscription periodically to retrieve the latest published configurations.

## ⚙️ Automated Pipeline

「SUB0」 uses GitHub Actions to automate configuration processing.

```text
Public Sources
      │
      ▼
Configuration Collection
      │
      ▼
Parsing & Duplicate Filtering
      │
      ▼
Protocol Testing
      │
      ▼
Format Conversion & Filtering
      │
      ▼
Published Configuration Files
```

### 📡 Workflow Status

[![Update Configs](https://img.shields.io/badge/Workflow-Update%20Configs-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/javadz501/SUB-Independent/actions)

- **Workflow:** `Update Configs`
- **Automation:** GitHub Actions
- **Schedule:** Configured in `.github/workflows/update-configs.yml`
- **Manual runs:** Available through the Actions interface when enabled

[↗ View workflow runs and logs](https://github.com/javadz501/SUB-Independent/actions)

## 📂 Repository Structure

```text
SUB-Independent/
├── .github/
│   └── workflows/
│       └── update-configs.yml
├── configs/
│   ├── proxy_configs_tested.txt
│   ├── singbox_configs_tested.json
│   ├── singbox_configs_secure.json
│   ├── clash_configs_tested.yaml
│   └── clash_configs_secure.yaml
├── src/
├── settings/
├── tests/
├── assets/
├── requirements.txt
├── LICENSE
├── SUB-Independent.png
└── README.md
```

*This is a simplified overview of the main project components. Additional files may exist in the repository.*

## ⚠️ Security & Reliability

Public proxy configurations are provided on an **as-is** basis.

- **Availability:** Configurations can stop working or become unavailable at any time.
- **Testing limitations:** A successful test does not guarantee long-term availability, privacy, or security.
- **Traffic privacy:** Proxy operators may observe connection metadata and any traffic that is not properly encrypted.
- **Sensitive information:** Do not use untrusted public proxies for banking, account recovery, confidential communications, or other sensitive activities.
- **Compatibility:** Not every configuration works with every client, network, or protocol implementation.

Use trusted services and appropriate end-to-end encryption whenever possible.

## 🙏 Acknowledgments

「SUB0」 builds upon the work started by the original [Multi Proxy Config Fetcher](https://github.com/4n0nymou3/multi-proxy-config-fetcher) project by [@4n0nymou3](https://github.com/4n0nymou3).

This repository is maintained independently, with its own configuration, automation, and project-specific changes.

Full credit goes to the original author for the foundational work. Please refer to the original repository and its license for the upstream project's terms.

## 📜 License & Attribution

「SUB0」 is based on an upstream project. Original license conditions, copyright notices, and required attribution must be preserved.

See the [`LICENSE`](https://github.com/javadz501/SUB-Independent/blob/main/LICENSE) file for the applicable terms.

## 🔗 Project Links

<p align="center">
  <a href="https://github.com/javadz501/SUB-Independent">Repository</a>
  &nbsp; • &nbsp;
  <a href="https://github.com/javadz501/SUB-Independent/actions">Actions</a>
  &nbsp; • &nbsp;
  <a href="https://github.com/javadz501/SUB-Independent/issues">Issues</a>
</p>

---

<p align="center">
  <strong>「SUB0」</strong>
  <br>
  <sub>Collect. Test. Publish.</sub>
  <br><br>
  <sub>Automated public proxy configuration collection and testing.</sub>
</p>
