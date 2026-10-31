[![Stars](https://img.shields.io/github/stars/javadz501/SUB0?style=flat-square)](https://github.com/javadz501/SUB0/stargazers)
[![Forks](https://img.shields.io/github/forks/javadz501/SUB0?style=flat-square)](https://github.com/javadz501/SUB0/network/members)
[![Issues](https://img.shields.io/github/issues/javadz501/SUB0?style=flat-square)](https://github.com/javadz501/SUB0/issues)
[![License](https://img.shields.io/github/license/javadz501/SUB0?style=flat-square)](https://github.com/javadz501/SUB0/blob/main/LICENSE)
[![Activity](https://img.shields.io/github/last-commit/javadz501/SUB0?style=flat-square)](https://github.com/javadz501/SUB0/commits/main)

<div dir="rtl">

# SUB0 – گردآورنده رایگان پیکربندی‌های پراکسی

[**🇺🇸 English**](README.md) | [**🇮🇷 فارسی**](README_FA.md) | [**🇨🇳 中文**](README_CN.md) | [**🇷🇺 Русский**](README_RU.md)

SUB0 یک سیستم خودکار برای جمع‌آوری، اعتبارسنجی، آزمایش، غنی‌سازی و فیلترکردن پیکربندی‌های پراکسی از منابع مختلف است. این پروژه با استفاده از پردازش موازی، آزمایش چندمرحله‌ای اتصال، اطلاعات موقعیت جغرافیایی و فیلترهای امنیتی، خروجی‌هایی با فرمت‌های مختلف برای کلاینت‌های پراکسی تولید می‌کند.

## 🌐 دسترسی به پیکربندی‌ها

فایل‌های خروجی پروژه مستقیماً از طریق مخزن GitHub قابل دسترسی هستند.

### فایل‌های اشتراک و پیکربندی

| نوع خروجی | فرمت | لینک |
|---|---|---|
| پیکربندی‌های خام | TXT | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/proxy_configs.txt) |
| پیکربندی‌های تست‌شده با Xray | TXT | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/proxy_configs_tested.txt) |
| تمام پیکربندی‌های Sing-box | JSON | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/singbox_configs_all.json) |
| پیکربندی‌های تست‌شده Sing-box | JSON | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/singbox_configs_tested.json) |
| پیکربندی‌های امن Sing-box | JSON | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/singbox_configs_secure.json) |
| تمام پیکربندی‌های Clash | YAML | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/clash_configs_all.yaml) |
| پیکربندی‌های تست‌شده Clash | YAML | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/clash_configs_tested.yaml) |
| پیکربندی‌های امن Clash | YAML | [مشاهده](https://raw.githubusercontent.com/javadz501/SUB0/main/configs/clash_configs_secure.yaml) |

> لینک‌ها به فایل‌های خروجی مخزن اشاره می‌کنند. تعداد و محتوای پیکربندی‌ها با اجرای مجدد فرایند به‌روزرسانی تغییر می‌کند.

## 📊 پایش عملکرد منابع

پروژه اطلاعات عملکرد منابع پیکربندی، شامل کانال‌های تلگرام و URLهای تعریف‌شده را جمع‌آوری می‌کند. نمودار عملکرد در جریان اجرای خودکار پروژه به‌روزرسانی می‌شود.

### نمای سریع

<div align="center">
  <a href="assets/channel_stats_chart.svg">
    <img src="assets/channel_stats_chart.svg" alt="نمودار عملکرد منابع" width="800">
  </a>
</div>

### گزارش تحلیلی

📊 [مشاهده گزارش تعاملی عملکرد منابع](assets/performance_report.html)

هر منبع بر اساس چهار شاخص اصلی ارزیابی می‌شود:

- **قابلیت اطمینان (۳۵٪):** نرخ موفقیت دریافت و به‌روزرسانی پیکربندی‌ها
- **کیفیت پیکربندی (۲۵٪):** نسبت پیکربندی‌های معتبر به کل پیکربندی‌های دریافت‌شده
- **منحصربه‌فرد بودن (۲۵٪):** سهم پیکربندی‌های یکتا
- **زمان پاسخ (۱۵٪):** زمان پاسخ‌گویی و دسترس‌پذیری منبع

منابعی که امتیاز آن‌ها کمتر از ۳۰٪ باشد، مطابق منطق مدیریت منابع پروژه به‌صورت خودکار غیرفعال می‌شوند.

## ✨ ویژگی‌های اصلی

### پشتیبانی از چند پروتکل

- **VLESS** — پروتکل سبک پراکسی با پشتیبانی از Reality و XTLS Vision
- **VMess** — پروتکل پراکسی V2Ray
- **Trojan** — پروتکل پراکسی مبتنی بر TLS
- **Shadowsocks** — پراکسی رمزنگاری‌شده با پشتیبانی از روش‌های AEAD
- **Hysteria2** — پروتکل پراکسی مبتنی بر UDP با عملکرد بالا
- **WireGuard** — پروتکل مدرن VPN؛ در وضعیت فعلی فقط در خروجی متنی خام/تست‌شده وجود دارد و به‌صورت پیش‌فرض غیرفعال است.
- **TUIC** — پروتکل پراکسی مبتنی بر UDP؛ در وضعیت فعلی محدودیت مشابه WireGuard دارد و به‌صورت پیش‌فرض غیرفعال است.

### خط لوله پردازش

1. **جمع‌آوری هوشمند**
   - پشتیبانی از کانال‌های تلگرام، لینک‌های SSCONF و URLهای دلخواه
   - رمزگشایی خودکار Base64 و تشخیص فرمت
   - حذف پیکربندی‌های تکراری بر اساس پروتکل، آدرس، پورت و اطلاعات احراز هویت
   - تلاش مجدد برای خطاهای موقتی مانند Timeout، اختلال اتصال و کدهای HTTP 408، 429 و 5xx

2. **غنی‌سازی اطلاعات جغرافیایی**
   - تشخیص موقعیت جغرافیایی سرورها
   - برچسب‌گذاری با پرچم کشور
   - پشتیبانی از چند API موقعیت‌یابی
   - استفاده از مکانیزم جایگزین در صورت عدم دسترسی API اصلی

3. **تفکیک بر اساس کشور**
   - دسته‌بندی پیکربندی‌های تست‌شده با Xray بر اساس کشور سرور
   - تولید فایل اشتراک اختصاصی برای کشورهای تعریف‌شده در تنظیمات
   - استفاده مجدد از اطلاعات جغرافیایی ذخیره‌شده برای جلوگیری از درخواست‌های غیرضروری API
   - حفظ فایل قبلی کشورهایی که در اجرای جدید پیکربندی متناظری ندارند

4. **نام‌گذاری هوشمند**
   - تولید نام‌های توصیفی بر اساس مشخصات پروتکل
   - تشخیص نوع انتقال مانند WS، GRPC و HTTP2
   - تشخیص ویژگی‌های امنیتی مانند TLS، Reality، XTLS و Vision
   - افزودن اطلاعات پورت و کشور به نام پیکربندی

5. **آزمایش چندمرحله‌ای با دو هسته**
   - آزمایش اتصال با Xray Core و Sing-box Core
   - اجرای چند دور آزمایش مستقل برای هر هسته
   - نگهداری پیکربندی‌هایی که تمام دورهای موردنیاز را با موفقیت پشت سر بگذارند
   - چرخش آدرس مقصد آزمایش بین دورها
   - بررسی دسترس‌پذیری URLهای آزمایش پیش از شروع تست
   - پشتیبانی از پردازش موازی و تنظیم تعداد Workerها و Timeout

6. **فیلتر امنیتی**
   - حذف روش‌های رمزنگاری ناامن
   - بررسی تنظیمات TLS/SSL
   - فیلترکردن پروتکل‌ها و تنظیمات منسوخ
   - تولید خروجی‌های جداگانه امن برای فرمت‌های پشتیبانی‌شده

7. **تبدیل فرمت**
   - تولید خروجی JSON برای Sing-box
   - تولید پیکربندی‌های Xray با قابلیت Load Balancing
   - پشتیبانی از نسخه Xray Fragment
   - تولید خروجی YAML برای Clash/Mihomo
   - پشتیبانی از Reality و XTLS Vision در فرمت‌های خروجی پشتیبانی‌شده

## 🚀 شروع سریع

### برای کاربران

1. فایل خروجی موردنظر را از بخش [دسترسی به پیکربندی‌ها](#-دسترسی-به-پیکربندیها) انتخاب کنید.
2. لینک فایل را کپی کنید.
3. لینک را در کلاینت پراکسی سازگار با فرمت انتخاب‌شده وارد کنید.

### برای توسعه‌دهندگان

#### Fork و سفارشی‌سازی

1. مخزن را Fork کنید.
2. فایل `settings/user_settings.py` را برای تنظیم موارد زیر ویرایش کنید:
   - URL منابع و کانال‌های تلگرام
   - پروتکل‌های فعال
   - پارامترهای آزمایش اتصال
   - اولویت APIهای موقعیت‌یابی
3. در صورت نیاز، فایل `settings/fragment_settings.py` را برای تنظیم Fragment ویرایش کنید.
4. در صورت نیاز، دیکشنری `TARGET_COUNTRIES` در فایل `src/country_splitter.py` را تغییر دهید.
5. GitHub Actions را در مخزن Forkشده فعال کنید.
6. فرایند به‌روزرسانی مطابق زمان‌بندی تعریف‌شده اجرا خواهد شد.

#### اجرای محلی

برای نصب و اجرای پروژه در محیط محلی، فایل‌های نصب و راهنماهای موجود در مخزن را بررسی کنید.

| زبان | راهنما |
|---|---|
| فارسی | [راهنمای فارسی](README_WIZARD_FA.md) |
| انگلیسی | [English Guide](README_WIZARD_EN.md) |
| چینی | [中文指南](README_WIZARD_CN.md) |
| روسی | [Руководство на русском](README_WIZARD_RU.md) |

## ⚙️ تنظیمات پروژه

### `settings/user_settings.py`

نمونه‌ای از تنظیمات اصلی:

```python
# Source URLs
SOURCE_URLS = [
    "https://t.me/s/your_channel",
    "https://raw.githubusercontent.com/user/repo/main/configs.txt",
]

# Power Mode
USE_MAXIMUM_POWER = True
SPECIFIC_CONFIG_COUNT = 0

# Protocol Filtering
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": False,
}

# Config Age Filtering
MAX_CONFIG_AGE_DAYS = 1

# Xray Testing
ENABLE_XRAY_TESTER = True
XRAY_TESTER_MAX_WORKERS = 24
XRAY_TESTER_TIMEOUT_SECONDS = 5
XRAY_TESTER_ROUNDS = 3
XRAY_TESTER_BATCH_SIZE = 200

XRAY_TESTER_URLS = [
    "https://www.youtube.com/generate_204",
    "https://www.gstatic.com/generate_204",
    "https://cp.cloudflare.com",
]

# Sing-box Testing
ENABLE_SINGBOX_TESTER = True
SINGBOX_TESTER_MAX_WORKERS = 24
SINGBOX_TESTER_TIMEOUT_SECONDS = 5
SINGBOX_TESTER_ROUNDS = 3
SINGBOX_TESTER_BATCH_SIZE = 200

SINGBOX_TESTER_URLS = [
    "https://www.youtube.com/generate_204",
    "https://www.gstatic.com/generate_204",
    "https://cp.cloudflare.com",
]

# Geolocation APIs
LOCATION_APIS = [
    "api.iplocation.net",
    "freeipapi.com",
    "ip-api.com",
    "ipapi.co",
]
```

غیرفعال‌کردن هرکدام از تسترها، مرحله مربوط به آن را در اجرای جاری نادیده می‌گیرد و فایل مرحله قبلی را بدون تغییر به مرحله بعد منتقل می‌کند.

توجه داشته باشید که خروجی‌های Sing-box، Clash و Xray Secure به مرحله آزمایش Sing-box وابسته‌اند. غیرفعال‌کردن این تستر می‌تواند قابلیت اطمینان این خروجی‌ها را کاهش دهد.

### `settings/fragment_settings.py`

```python
FRAGMENT_ENABLED = True

FRAGMENT_STAGE_1 = {
    "packets": "tlshello",
    "lengths": ["5", "94", "1"],
    "delays": ["0"],
    "max_split": "0",
}

FRAGMENT_STAGE_2_ENABLED = True

FRAGMENT_STAGE_2 = {
    "packets": "1-1",
    "lengths": ["109", "1"],
    "delays": ["1"],
    "max_split": "355",
}

FRAGMENT_TLS_FINGERPRINT = "unsafe"
FRAGMENT_TLS_CIPHER_SUITES = "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:..."
```

این فایل تنظیمات Fragment دومرحله‌ای TLS ClientHello را برای خروجی `xray_fragment_loadbalanced_config.json` کنترل می‌کند.

پارامترهای هر مرحله، TLS Fingerprint و Cipher Suites از همین فایل قابل تنظیم هستند.

## 📁 فایل‌های خروجی

| فایل | توضیحات |
|---|---|
| `configs/proxy_configs.txt` | پیکربندی‌های خام دریافت‌شده |
| `configs/proxy_configs_tested.txt` | پیکربندی‌های آزمایش‌شده با Xray |
| `configs/location/<CC>/proxy_configs.txt` | پیکربندی‌های Xray دسته‌بندی‌شده بر اساس کشور |
| `configs/singbox_configs_all.json` | تمام پیکربندی‌ها در فرمت Sing-box |
| `configs/singbox_configs_tested.json` | پیکربندی‌های تست‌شده Sing-box |
| `configs/singbox_configs_secure.json` | پیکربندی‌های امن Sing-box |
| `configs/xray_secure_loadbalanced_config.json` | پیکربندی امن Xray با Load Balancing |
| `configs/clash_configs_all.yaml` | تمام پیکربندی‌ها در فرمت Clash/Mihomo |
| `configs/clash_configs_tested.yaml` | پیکربندی‌های تست‌شده Clash |
| `configs/clash_configs_secure.yaml` | پیکربندی‌های امن Clash |
| `configs/xray_loadbalanced_config.json` | پیکربندی Xray با Load Balancing |
| `configs/xray_fragment_loadbalanced_config.json` | پیکربندی Xray با Fragment |
| `configs/location_cache.json` | کش اطلاعات موقعیت جغرافیایی |
| `configs/channel_stats.json` | معیارهای عملکرد منابع |

## 🔄 اتوماسیون

پروژه از GitHub Actions برای اجرای خودکار فرایند جمع‌آوری و به‌روزرسانی استفاده می‌کند.

قابلیت‌های اتوماسیون:

- اجرای زمان‌بندی‌شده مطابق Cron تعریف‌شده در Workflow
- اجرای دستی از طریق `workflow_dispatch`
- به‌روزرسانی خودکار فایل‌های خروجی
- تولید نمودارها و گزارش‌های عملکرد
- ثبت خلاصه اجرای Pipeline

### مراحل اصلی Workflow

1. دریافت پیکربندی‌ها از منابع
2. غنی‌سازی اطلاعات جغرافیایی
3. نام‌گذاری پیکربندی‌ها
4. آزمایش با Xray Core
5. تفکیک پیکربندی‌ها بر اساس کشور
6. تبدیل به فرمت Sing-box
7. آزمایش با Sing-box Core
8. فیلتر امنیتی و تولید خروجی‌های امن
9. تولید فایل‌های Clash/Mihomo
10. تولید پیکربندی Xray Load Balanced
11. تولید پیکربندی Xray Fragment
12. به‌روزرسانی نمودارها و گزارش‌ها
13. تولید خلاصه اجرای Pipeline
14. ثبت تغییرات در مخزن

## 🛡️ امنیت

### فیلتر امنیتی خودکار

سیستم بر اساس قواعد امنیتی تعریف‌شده، مواردی مانند زیر را فیلتر می‌کند:

- روش‌های رمزنگاری ناامن Shadowsocks
- تنظیمات منسوخ VMess مانند `alter_id`
- پیکربندی‌های فاقد رمزنگاری موردنیاز
- تنظیمات نامعتبر TLS مانند `insecure=true`
- تنظیمات VMess با `security=none`

### خروجی‌های امن

خروجی‌های Secure برای نگهداری پیکربندی‌هایی طراحی شده‌اند که از فیلترهای امنیتی تعریف‌شده در پروژه عبور می‌کنند.

عبور از فیلترهای پروژه به‌معنای تضمین امنیت کامل، ناشناس‌ماندن یا قابل‌اعتمادبودن ارائه‌دهنده سرویس نیست.

## 📈 بهینه‌سازی عملکرد

- پردازش موازی برای افزایش سرعت آزمایش
- کش اطلاعات جغرافیایی برای کاهش درخواست‌های API
- استفاده از Connection Pooling در درخواست‌های HTTP
- Timeout قابل تنظیم
- Retry با Exponential Backoff برای خطاهای موقتی
- مدیریت و آزادسازی منابع برای کاهش احتمال نشت حافظه

## 🌍 موقعیت‌یابی جغرافیایی

### APIهای پشتیبانی‌شده

پروژه از APIهای زیر برای دریافت اطلاعات موقعیت جغرافیایی استفاده می‌کند:

1. `api.iplocation.net`
2. `freeipapi.com`
3. `ip-api.com`
4. `ipapi.co`

ترتیب استفاده از APIها از طریق تنظیمات پروژه قابل تغییر است.

### قابلیت‌ها

- تشخیص موقعیت جغرافیایی IP
- کش اطلاعات برای کاهش درخواست‌های تکراری
- استفاده از API جایگزین در صورت بروز خطا
- عدم نیاز به کلید API در تنظیمات پیش‌فرض

## 📊 آمار و پایش

### معیارهای عملکرد

سیستم می‌تواند معیارهای زیر را برای منابع ثبت کند:

- تعداد پیکربندی‌های دریافت‌شده
- نسبت پیکربندی‌های معتبر و نامعتبر
- تعداد پیکربندی‌های یکتا
- میانگین زمان پاسخ
- نرخ موفقیت و خطا
- امتیاز کلی سلامت منبع

### گزارش‌های تصویری

- **نمودار SVG:** نمایش سریع عملکرد منابع
- **گزارش HTML:** تحلیل منابع، توزیع پروتکل‌ها، زمان پاسخ و روندهای تاریخی
- **خلاصه Pipeline:** نمایش تعداد پیکربندی‌ها در مراحل مختلف اجرا

## 🧪 تست‌ها

پوشه `tests/` شامل تست‌های خودکار برای بررسی منطق Parsing، فیلترهای امنیتی و پردازش دسته‌ای است.

تست‌ها از طریق Workflow مجزای زیر اجرا می‌شوند:

` .github/workflows/tests.yml `

اجرای محلی:

```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```

## 🤝 مشارکت

مشارکت در توسعه پروژه آزاد است.

روش‌های مشارکت:

1. گزارش خطا از طریق Issues
2. پیشنهاد قابلیت‌های جدید
3. ارسال Pull Request
4. معرفی منابع جدید
5. بهبود مستندات

## ⚠️ سلب مسئولیت

این پروژه صرفاً با اهداف آموزشی و اطلاع‌رسانی ارائه شده است.

توسعه‌دهندگان مسئولیتی در قبال موارد زیر بر عهده نمی‌گیرند:

- استفاده نادرست از نرم‌افزار
- خسارات ناشی از استفاده از پیکربندی‌ها
- کیفیت، امنیت یا دسترس‌پذیری سرویس‌های پراکسی شخص ثالث
- نقض قوانین یا مقررات محلی

**مسئولیت کاربران:**

- رعایت قوانین و مقررات محل استفاده
- بررسی امنیت پیکربندی‌ها پیش از استفاده
- آگاهی از ریسک‌های استفاده از سرویس‌های پراکسی
- رعایت شرایط سرویس ارائه‌دهندگان

## 📜 مجوز

این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات بیشتر فایل [LICENSE](LICENSE) را مطالعه کنید.

## 🙏 قدردانی

- **Xray-core** — هسته پراکسی با عملکرد بالا
- **Sing-box** — هسته چندمنظوره شبکه و پراکسی
- **Clash/Mihomo** — پلتفرم مدیریت پیکربندی پراکسی
- **GitHub Actions** — زیرساخت اتوماسیون

---

<div align="center">

**[⬆ بازگشت به بالا](#-دسترسی-به-پیکربندیها)**

</div>
</div>
