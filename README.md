 <p align="center">
  <img src="https://github.com/javadz501/SUB0/blob/main/SUB0.jpg" alt="SUB0 Logo" width="220">
</p>

<h1 align="center">「SUB0」 – Free Proxy Configuration Collector</h1>

<p align="center">
  <strong>Collect. Test. Publish.</strong>
  <br>
  Automated collection of public proxy configurations, protocol testing, and subscription publishing.
</p>

<p align="center">
  <a href="https://github.com/javadz501/SUB0/actions">
    <img src="https://img.shields.io/badge/GitHub%20Actions-Automated-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
  </a>
  <img src="https://img.shields.io/badge/Xray-Supported-6366F1?style=for-the-badge" alt="Xray">
  <img src="https://img.shields.io/badge/sing--box-Supported-00BFA5?style=for-the-badge" alt="sing-box">
  <img src="https://img.shields.io/badge/Clash-Supported-8B5CF6?style=for-the-badge" alt="Clash">
  <img src="https://img.shields.io/badge/Cost-Free-22C55E?style=for-the-badge" alt="Free">
</p>

---

## ⚡ Overview

**「SUB0」** is an automated pipeline that collects publicly available proxy configurations, tests supported protocols, filters the results, and publishes organized configuration files.

The goal is simple: **collect useful configurations, validate what can be tested, and make the results easy to access.**

| Capability | Description |
|---|---|
| Automated Collection | Retrieves configurations from public sources |
| Protocol Testing | Tests supported configurations using available tools |
| Duplicate Filtering | Reduces duplicate entries in generated outputs |
| Multiple Formats | Publishes configurations for Xray, sing-box, and Clash |
| Scheduled Processing | Runs automatically through GitHub Actions |
| Public Subscriptions | Provides direct raw links to generated files |

## 🔗 Configuration Subscriptions

Choose the output compatible with your client and import the corresponding subscription URL. Server counts are automatically updated after each successful pipeline run.

| Configuration | Format | Servers | Subscription |
|:--|:--:|--:|:--|
<!-- SUB0_COUNTS_START -->
| **Xray Tested** | `TXT` | 165 | [↗ Open Subscription](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/proxy_configs_tested.txt) |

| **sing-box Tested** | `JSON` | 114 | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/singbox_configs_tested.json) |

| **sing-box Secure** | `JSON` | 103 | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/singbox_configs_secure.json) |

| **Clash Tested** | `YAML` | 114 | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/clash_configs_tested.yaml) |

| **Clash Secure** | `YAML` | 103 | [↗ Open Configuration](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/clash_configs_secure.yaml) |
<!-- SUB0_COUNTS_END -->

> **Note:** Subscription links depend on the corresponding files being present and up to date on the `main` branch. Configuration availability and client compatibility may change between runs.

## 🧭 Quick Start

**01 — Choose a Client**

Select a compatible client, such as Xray, sing-box, or Clash.

**02 — Select a Subscription**

Choose the appropriate format from the table above.

**03 — Import the URL**

Paste the raw subscription URL into your client's subscription manager. If your client does not support remote subscriptions, download the file and import it manually.

**04 — Refresh When Needed**

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

[![Update Configs](https://img.shields.io/badge/Workflow-Run%20Config--Updater-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/javadz501/SUB0/actions)

- **Workflow:** `Run Config-Updater`
- **Automation:** GitHub Actions
- **Schedule:** Defined in `.github/workflows/update-configs.yml`
- **Manual Runs:** Available through the Actions interface when enabled

[↗ View Workflow Runs and Logs](https://github.com/javadz501/SUB0/actions)

## 📂 Repository Structure

```text
SUB0/
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
├── SUB0.jpg
└── README.md
```

*This is a simplified overview of the main project components. Additional files may be present in the repository.*

## ⚠️ Security & Reliability

Public proxy configurations are provided on an **as-is** basis.

- **Availability:** Configurations may stop working or become unavailable at any time.
- **Testing Limitations:** A successful test does not guarantee long-term availability, privacy, or security.
- **Traffic Privacy:** Proxy operators may observe connection metadata and any traffic that is not properly encrypted.
- **Sensitive Information:** Do not use untrusted public proxies for banking, account recovery, confidential communications, or other sensitive activities.
- **Compatibility:** Not every configuration is compatible with every client, network, or protocol implementation.

Use trusted services and appropriate end-to-end encryption whenever possible.

## 🙏 Acknowledgments

「SUB0」 builds upon the work of the original [Multi Proxy Config Fetcher](https://github.com/4n0nymou3/multi-proxy-config-fetcher) project by [@4n0nymou3](https://github.com/4n0nymou3).

This repository is maintained independently, with its own configuration, automation, and project-specific modifications.

Full credit goes to the original author for the foundational work. Please refer to the original repository and its license for the applicable terms.

## 📜 License & Attribution

「SUB0」 is based on an upstream project. The original license conditions, copyright notices, and required attribution must be preserved.

See the [`LICENSE`](https://github.com/javadz501/SUB0/blob/main/LICENSE) file for the applicable license terms.

## 🔗 Project Links

<p align="center">
  <a href="https://github.com/javadz501/SUB0">Repository</a>
  &nbsp; • &nbsp;
  <a href="https://github.com/javadz501/SUB0/actions">Actions</a>
  &nbsp; • &nbsp;
  <a href="https://github.com/javadz501/SUB0/issues">Issues</a>
</p>

---

<p align="center">
  <strong>「SUB0」</strong>
  <br>
  <sub>Collect. Test. Publish.</sub>
  <br><br>
  <sub>Automated collection and testing of public proxy configurations.</sub>
</p>
