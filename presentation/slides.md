---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: aixum
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# take snapshot for each slide in the overview
overviewSnapshots: true

fonts:
  sans: Vazirmatn

htmlAttrs:
  dir: rtl
  lang: fa
---

# Modern Django
#### with Dynamic Frontend & awesome features


<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/aixum/quix" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: fade-out
---

# Cookiecutter

**کوکی کاتر** یک ابزار متن‌باز است که برای ایجاد پروژه‌های جدید بر اساس الگوهای از پیش تعیین‌شده به کار می‌رود. این ابزار به توسعه‌دهندگان اجازه می‌دهد تا به سرعت ساختار و تنظیمات اولیه پروژه‌های خود را بدون نیاز به تکرار کارهای دستی ایجاد کنند.

### تاریخچه Cookiecutter-Django:

- 🛠 **شروع پروژه** - در سال ۲۰۱۳ توسط Daniel Roy Greenfeld به عنوان یک ابزار متن‌باز برای ایجاد سریع پروژه‌های مبتنی بر الگو توسعه یافت.
- 📈 **محبوبیت در جامعه توسعه‌دهندگان** - به‌سرعت در میان توسعه‌دهندگان Python، به‌ویژه برای فریمورک‌های مانند Django و Flask، محبوب شد.
- 🌍 **گسترش به زبان‌ها و فریمورک‌های مختلف** - پس از موفقیت اولیه، Cookiecutter برای پشتیبانی از پروژه‌های متنوع در زبان‌ها و فریمورک‌های مختلف توسعه یافت.
- 🚀 **ابزار استاندارد در توسعه پروژه‌های مدرن** - به مرور زمان، این ابزار به یکی از ابزارهای اصلی در استانداردسازی پروژه‌ها، به ویژه در محیط‌های تیمی و صنعتی، تبدیل شد.

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 88%, #146b8c 80%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}

</style>

---

### چرا؟

- **صرفه‌جویی در زمان**: بدون Cookiecutter، باید برای ساختار، ابزارها، و تنظیمات پروژه تصمیم‌گیری کنید که زمان‌بر است. 🕒
- **پایبندی به ‌Best practices**: کوکی کاتر الگوهایی با بهترین شیوه‌های توسعه ارائه می‌دهد و از مشکلات احتمالی ناشی از تنظیمات دستی جلوگیری می‌کند. 🎯

#

### محدودیت ها

- **محدودیت در شرایط خاص**: Cookiecutter ممکن است برای پروژه‌های بسیار سفارشی یا غیر معمول مناسب نباشد، زیرا الگوها بر اساس یک tech stack مشخص طراحی شده‌اند.
#
### استفاده‌های رایج

- **ایجاد پروژه‌های جدید**: شروع سریع پروژه‌های جنگو با تنظیمات آماده و بهینه.
- **توسعه در تیم‌ها**: هماهنگ‌سازی اعضای تیم با ساختارهای یکپارچه و استاندارد.
- **استفاده در محیط‌ production**: با تنظیمات Docker و CI/CD، پروژه‌ها به‌سادگی به محیط‌های تولید منتقل می‌شوند.
#


---
layout: statement
transition: slide-up
---

## ابزارهای استفاده شده در Cookiecutter-Django


---
transition: slide-up
---

# Ruff

Ruff یک ابزار linting بسیار سریع برای Python است که به بررسی و تصحیح کدهای شما کمک می‌کند. این ابزار می‌تواند انواع مشکلات کدنویسی و سبک کد را تشخیص دهد و پیشنهادهایی برای بهبود آن‌ها ارائه کند. با استفاده از Ruff، می‌توانید از کدهای تمیز و باکیفیت اطمینان حاصل کنید. 🚀

- نوشته شده با زبان راست
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Rust_programming_language_black_logo.svg" style="width: 100px;"/>
- فوق سریع
<img src="/images/ruff.png" style="max-width: 100%; height: auto;"/>

---
transition: slide-up
---

# DjLint

DjLint یک ابزار linting مخصوص Django است که به بررسی کدهای تمپلیت Django و HTML می‌پردازد. این ابزار به طور خاص برای توسعه‌دهندگان Django طراحی شده است تا اطمینان حاصل شود که تمپلیت‌ها و ساختار HTML پروژه با استانداردهای کدنویسی مطابقت دارند. 📋

- جلوگیری از اشکالات تمپلیت
- خوانا شدن تمپلیت
- رعایت best practice


---
transition: slide-up
---

# Pre-commit

Pre-commit به شما اجازه می‌دهد تا قبل از هر commit، اسکریپت‌های خاصی را اجرا کنید. این اسکریپت‌ها می‌توانند برای بررسی کیفیت کد، اجرای تست‌ها، یا هر اقدام دیگری استفاده شوند. با Pre-commit، می‌توانید از ورود کدهای مشکل‌دار به مخزن کد جلوگیری کنید. ⚙️

- اجرای اسکریپت‌های خاص
- اجرای تست‌ها
- اجرای فرمت‌بندی کد
- اطمینان از کیفیت کد برای تمام تیم
```bash {1|2-3|4-5} twoslash
$ cd my_project
# install in venv
$ python3 -m pip install pre-commit
# make sure git is already initialized
$ pre-commit install

```

<style>
pre {
  direction: ltr;
}
</style>

---
transition: slide-up
---

# Docker

Docker ابزاری است که به شما اجازه می‌دهد پروژه‌های خود را در کانتینرهای جداگانه توسعه دهید و اجرا کنید. این کانتینرها تضمین می‌کنند که محیط توسعه شما مستقل از سیستم عامل و سایر پروژه‌ها باشد. با Docker، می‌توانید پروژه‌های خود را به راحتی بین توسعه‌دهندگان مختلف به اشتراک بگذارید و به محیط production انتقال دهید. 🛠️

- ابزار و استاندارد جهانی




---
layout: statement
transition: slide-up
---

## ابزارهای پیشنهادی ما


---
transition: slide-up
---

# Justfile

Justfile به شما امکان می‌دهد که دستورات متداول و پیچیده را در قالب ساده ذخیره کنید. با استفاده از Justfile، می‌توانید وظایف متداول مانند ساخت پروژه، اجرای تست‌ها، یا شروع سرور را تنها با یک دستور اجرا کنید. این ابزار بهره‌وری شما را افزایش می‌دهد و کارها را ساده‌تر می‌کند. ✨

```bash twoslash

# Build the Docker images
build:
    docker compose -f docker-compose.local.yml build

migrations:
    docker compose -f docker-compose.local.yml run --rm django python manage.py makemigrations

# Run the Docker containers
run:
    docker compose -f docker-compose.local.yml up

```
<style>
pre {
  direction: ltr;
}
</style>

---
transition: fade-out
---

# htmx (Dynamic frontend)

-
-

---
transition: slide-up
---

## مزایا و معایب نسبت به vue.js


---
layout: image-left
image: images/minimal.jpg
---

# نصب و استفاده


```bash {1|3|all} twoslash
$ pip install "cookiecutter>=1.7.0"

$ cookiecutter https://github.com/cookiecutter/cookiecutter-django
```

پس از این مرحله درباره پروژه سوالاتی پرسیده میشود که میتوانید پاسخ دهید و یا از مقادیر پیشفرض استفاده کنید.

[گیتهاب پروژه cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)

<!-- Inline style -->
<style>

pre {
  direction: ltr;
}
</style>


---
image: images/philo.jpg
layout: image-right

---
#
#

# ساخت یک  پروژه برای تست
1. تعریف نیازمندی های پروژه
2. طراحی نسبی سیستم
3. ایجاد پروژه با Cookiecutter

---
transition: slide-up
layout: statement
---
با تشکر از توجه شما

<div style="direction: ltr">
<PoweredBySlidev mt-10 />
</div>
