# -*- coding: utf-8 -*-
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
LI = "https://www.linkedin.com/company/abbasmirzaa-agency/"

LI_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.35V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.55V9h3.57v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.22.79 24 1.77 24h20.45c.98 0 1.78-.78 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'

NAV = [("index.html","خانه"),("services.html","خدمات"),
       ("portfolio.html","نمونه‌کارها"),("about.html","درباره ما"),("contact.html","تماس")]

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/brand/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>'''

def header(active):
    items=""
    for href,label in NAV:
        cls=' class="active"' if href==active else ''
        items+=f'<li><a href="{href}"{cls}>{label}</a></li>'
    return f'''
<header id="header">
  <div class="container nav">
    <a href="index.html" class="logo">
      <img src="assets/brand/logo.png" alt="آژانس تبلیغاتی عباس میرزا">
      <span>عباس میرزا<small>آژانس تبلیغاتی</small></span>
    </a>
    <ul class="menu" id="menu">{items}</ul>
    <div class="nav-cta">
      <a class="li-btn" href="{LI}" target="_blank" rel="noopener">{LI_SVG}<span>لینکدین</span></a>
      <button class="burger" id="burger" aria-label="منو"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''

def footer():
    serv='\n'.join(f'<li><a href="services.html">{s}</a></li>' for s in
        ["استراتژی و برندینگ","بازاریابی دیجیتال","تولید محتوا","طراحی لندینگ پیج"])
    quick='\n'.join(f'<li><a href="{h}">{l}</a></li>' for h,l in NAV[1:])
    return f'''
<footer>
  <div class="container">
    <div class="foot-grid">
      <div>
        <a href="index.html" class="logo"><img src="assets/brand/logo.png" alt="عباس میرزا"><span>عباس میرزا<small>آژانس تبلیغاتی</small></span></a>
        <p style="max-width:300px">برند شما را با خلاقیت، استراتژی و داده به جایگاهی که شایسته‌اش هست می‌رسانیم — از طراحی لوگو تا آخرین کلیک تبلیغ.</p>
        <div class="socials">
          <a class="li" href="{LI}" target="_blank" rel="noopener" aria-label="LinkedIn">{LI_SVG}</a>
          <a href="https://www.abbasmirzaa.com" target="_blank" rel="noopener" aria-label="Website">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm6.9 6h-2.6a15.6 15.6 0 0 0-1.2-3.3A8 8 0 0 1 18.9 8zM12 4c.7 1 1.3 2.3 1.7 4h-3.4C10.7 6.3 11.3 5 12 4zM4.3 14a8 8 0 0 1 0-4h3a18 18 0 0 0 0 4zm.8 2h2.6c.3 1.2.7 2.3 1.2 3.3A8 8 0 0 1 5.1 16zm2.6-8H5.1a8 8 0 0 1 3.8-3.3C8.4 5.7 8 6.8 7.7 8zM12 20c-.7-1-1.3-2.3-1.7-4h3.4c-.4 1.7-1 3-1.7 4zm2.1-6H9.9a16 16 0 0 1 0-4h4.2a16 16 0 0 1 0 4zm.6 5.3c.5-1 .9-2.1 1.2-3.3h2.6a8 8 0 0 1-3.8 3.3zM16.7 14a18 18 0 0 0 0-4h3a8 8 0 0 1 0 4z"/></svg>
          </a>
        </div>
      </div>
      <div><h5>خدمات</h5><ul>{serv}</ul></div>
      <div><h5>دسترسی سریع</h5><ul>{quick}</ul></div>
      <div><h5>تماس</h5><ul>
        <li>📞 <a href="tel:09127296658">۰۹۱۲۷۲۹۶۶۵۸</a></li>
        <li>📧 <a href="mailto:aliakbar.abbasi9@gmail.com">aliakbar.abbasi9@gmail.com</a></li>
        <li>📍 تهران، میدان ونک</li>
        <li><a href="{LI}" target="_blank" rel="noopener">in/ لینکدین آژانس</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom">© ۱۴۰۴ آژانس تبلیغاتی عباس میرزا — تمام حقوق محفوظ است. | <a href="{LI}" target="_blank" rel="noopener">ما را در لینکدین دنبال کنید</a></div>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>'''

def page(filename, active, title, desc, body):
    html = head(title,desc) + header(active) + body + footer()
    with open(os.path.join(ROOT,filename),"w",encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

# ---------- services data ----------
SERVICES = [
 ("🎯","استراتژی و جایگاه‌یابی برند","تدوین برنامه بازاریابی، هویت و جایگاه‌یابی برند برای متمایز شدن در ذهن مخاطب و بازار."),
 ("🎨","طراحی و هویت بصری","طراحی لوگو، لوگوتایپ، نشانه و سیستم بصری یکپارچه و ماندگار — مانند هویت برند نیلگون."),
 ("📱","مدیریت شبکه‌های اجتماعی","مدیریت و رشد اینستاگرام، تولید کاروسل و کمپین‌های کامیونیتی با نتایج قابل اندازه‌گیری."),
 ("💬","تبلیغات در پیام‌رسان‌ها","رشد و تبلیغات در بله و تلگرام؛ تبلیغ مستقیم، تب گفتگو و ارسال پیام انبوه هدفمند."),
 ("🖥️","طراحی و اجرای لندینگ پیج","صفحات فرود بهینه برای شبکه‌های اجتماعی و تبلیغات کلیکی یکتانت برای افزایش نرخ تبدیل."),
 ("📊","کمپین و گزارش‌دهی داده‌محور","طراحی و اجرای کمپین ۳۶۰ درجه همراه با گزارش شفاف عملکرد و تحلیل بازده."),
]

# ---------- case studies ----------
def imgs(prefix):
    files=sorted(glob.glob(os.path.join(ROOT,"assets/cases",prefix+"_*.png")))
    return ["assets/cases/"+os.path.basename(p) for p in files]

CASES = [
 {"id":"samar","file":"case-samar.html","prefix":"samar",
  "cat":"کمپین مارکتینگ و پذیره‌نویسی","client":"صندوق درآمد ثابت ثمر",
  "title":"کمپین پذیره‌نویسی صندوق ثمر",
  "cover":"assets/cases/samar_01.png",
  "summary":"راه‌اندازی واحد مارکتینگ، برگزاری سمینار تخصصی و اجرای کمپین کامل پذیره‌نویسی صندوق ثمر؛ از تدوین برنامه بازاریابی تا گزارش نهایی عملکرد.",
  "results":[("۴۷","میلیارد تومان لید جمع‌آوری‌شده"),("۶۲۷","هزار بازدید در تلگرام"),
             ("۴۸۱","سرمایه‌گذار جذب‌شده"),("۱۰۰+","مهمان در سمینار تخصصی")],
  "story":[
    "کار با تدوین یک برنامه بازاریابی جامع در ۶ سرفصل و ۲۴ صفحه و راه‌اندازی واحد مارکتینگ صندوق ثمر آغاز شد.",
    "در گام بعد، «سمینار چشم‌انداز نرخ بهره ۱۴۰۴» با ارسال ۶۷۶ دعوت‌نامه و حضور بیش از ۱۰۰ مهمان برگزار شد و پس از آن بیش از ۲۰۰ پک اختصاصی برای سرمایه‌گذاران بالقوه ارسال گردید.",
    "تنها یک هفته پیش از شروع پذیره‌نویسی، محدودیت نمایش درصد سود در تبلیغات اعلام شد؛ تیم با حفظ آرامش، استراتژی و تیزرها را در چند روز بازطراحی کرد و رویکرد «ایجاد حس کنجکاوی» را جایگزین کرد.",
    "نتیجه: ۴۷ میلیارد تومان لید، ۶۲۷ هزار بازدید در تلگرام و ۲۲ هزار بازدید در اینستاگرام، و سرانه خرید سرمایه‌گذاران حقیقی چند برابر صندوق‌های هزار میلیاردی رقیب.",
  ]},
 {"id":"bebye","file":"case-bebye.html","prefix":"bebye",
  "cat":"هویت بصری اینستاگرام","client":"رستوران BEBYE",
  "title":"هویت بصری اینستاگرام BEBYE",
  "cover":"assets/cases/bebye_01.png",
  "summary":"طراحی هویت بصری متمایز برای اینستاگرام رستوران BEBYE با کانسپت «Off the Menu»، تصویرسازی اختصاصی و سیستم رنگی آبی و نارنجی.",
  "results":[("۱","کانسپت خلاقانه Off the Menu"),("∞","سیستم تصویرسازی اختصاصی"),
             ("۲","رنگ اصلی برند: آبی و نارنجی")],
  "story":[
    "برای رستوران BEBYE یک کانسپت خلاقانه با عنوان «Shhh… It's off the Menu» طراحی شد تا حس کشف منوی مخفی و آیتم‌های ویژه را به مخاطب منتقل کند.",
    "سیستم بصری بر پایه تصویرسازی‌های اختصاصی سرآشپز و المان‌های غذایی، به‌همراه پالت رنگی آبی و نارنجی برند، برای پست‌ها، استوری‌ها و کاورها توسعه یافت.",
    "خروجی، یک زبان بصری یکپارچه و قابل‌گسترش بود که پیج را از رقبا متمایز کرد و حس «همراه با موسیقی زنده» و تجربه‌ای ویژه را القا می‌کند.",
  ]},
 {"id":"bale","file":"case-bale.html","prefix":"bale",
  "cat":"تبلیغات پیام‌رسان بله","client":"کانال فردانامه",
  "title":"رشد کانال فردانامه در بله",
  "cover":"assets/cases/bale_01.png",
  "summary":"رشد کانال فردانامه در پیام‌رسان بله از ۱۴۰۵ دنبال‌کننده به بیش از ۳ هزار نفر، با استفاده از سه کانال تبلیغاتی هدفمند.",
  "results":[("۳۰۰۰+","دنبال‌کننده کانال"),("۳","کانال تبلیغاتی فعال"),("۶","ماه اجرای کمپین")],
  "story":[
    "کانال فردانامه در فروردین تنها ۱۴۰۵ دنبال‌کننده داشت؛ هدف، رشد پایدار و هدفمند مخاطب در پیام‌رسان بله بود.",
    "تبلیغات از سه مسیر اجرا شد: ۱) تبلیغ مستقیم در کانال‌های مرتبط، ۲) تبلیغ در تب گفتگو، و ۳) ارسال پیام انبوه هدفمند.",
    "نتیجه این کمپین یکپارچه، رشد کانال به بیش از ۳ هزار دنبال‌کننده بود؛ رشدی چندبرابری در مدتی کوتاه.",
  ]},
 {"id":"insta","file":"case-insta.html","prefix":"insta",
  "cat":"مدیریت و رشد اینستاگرام","client":"پیج فردانامه",
  "title":"رشد اینستاگرام فردانامه",
  "cover":"assets/cases/insta_01.png",
  "summary":"خروج اینستاگرام فردانامه از درجازدن با تغییر رویه محتوایی؛ بیش از ۳۰٪ رشد و ۱۰ هزار فالوور جدید در کمتر از ۶ ماه.",
  "results":[("۳۰٪+","رشد فالوور"),("۱۰","هزار فالوور جدید"),("۶","ماه"),("∞","کمپین کامیونیتی موفق")],
  "story":[
    "پیج اینستاگرام فردانامه پس از مدت‌ها درجازدن، نیازمند یک تغییر رویکرد محتوایی اساسی بود.",
    "با طراحی قالب‌های جدید و جذاب، اجرای اسلایدر (کاروسل) و تغییر لحن و نوع محتوا، پیج جانی دوباره گرفت.",
    "در کمتر از ۶ ماه بیش از ۱۰ هزار فالوور جدید جذب شد — یعنی بیش از ۳۰٪ رشد — و کمپین‌های کامیونیتی پیج بسیار موفقیت‌آمیز بودند.",
  ]},
 {"id":"landing","file":"case-landing.html","prefix":"landing",
  "cat":"طراحی و اجرای لندینگ پیج","client":"محصولات متنوع",
  "title":"طراحی و اجرای لندینگ پیج محصولات",
  "cover":"assets/cases/landing_02.png",
  "summary":"طراحی صفحات فرود بهینه و حرفه‌ای، مناسب استفاده در شبکه‌های اجتماعی و تبلیغات کلیکی یکتانت، برای افزایش آشنایی مخاطب و نرخ خرید.",
  "results":[("↑","افزایش نرخ تبدیل"),("یکتانت","سازگار با تبلیغات کلیکی"),("∞","مناسب شبکه‌های اجتماعی")],
  "story":[
    "صفحات فرود (لندینگ پیج) طراحی‌شده توسط آژانس عباس میرزا به‌طور ویژه برای استفاده در شبکه‌های اجتماعی و تبلیغات کلیکی یکتانت بهینه شده‌اند.",
    "هر صفحه با تمرکز بر معرفی شفاف محصول، اعتمادسازی و مسیر روشن خرید طراحی می‌شود تا مخاطب را گام‌به‌گام به سمت خرید نهایی هدایت کند.",
    "این صفحات به آشنایی بیشتر مخاطب با محصول و افزایش نرخ تبدیل بازدیدکننده به مشتری کمک فراوانی می‌کنند.",
  ]},
 {"id":"nilgoon","file":"case-nilgoon.html","prefix":"nilgoon",
  "cat":"برندینگ و هویت بصری","client":"برند نیلگون",
  "title":"طراحی هویت بصری برند نیلگون",
  "cover":"assets/cases/nilgoon_09.png",
  "summary":"طراحی هویت بصری برند «نیلگون»، تولیدکننده تانکر و منابع ذخیره آب؛ با الهام از «برکه» آب‌انبارهای سنتی لار و بهره‌گیری از نسبت طلایی.",
  "results":[("۱","لوگوتایپ خوانا و قدرتمند"),("۱","نشانه الهام‌گرفته از برکه"),("φ","مبتنی بر نسبت طلایی")],
  "story":[
    "طراحی هویت برند نیلگون با تمرکز بر تعادل میان خوانایی، تمایز و ارتباط مفهومی با حوزه فعالیت (ذخیره آب) آغاز شد.",
    "ابتدا یک لوگوتایپ خوانا با الهام از حروف «نیل» طراحی شد؛ سپس برای تقویت هویت، نیاز به یک نشانه منحصربه‌فرد و ماندگار احساس شد.",
    "با توجه به ریشه برند در شهر لار استان فارس، «برکه» (آب‌انبارهای سنتی لار) به‌عنوان نماد انتخاب و فرم نشانه با الهام از آب‌انبار و بر پایه نسبت طلایی طراحی شد.",
    "خروجی، ترکیبی یکپارچه از لوگوتایپ و نشانه بود؛ هویتی که عملکرد، معنا و اصالت فرهنگی را کنار هم قرار می‌دهد. پالت رنگی: #283593 و #90CAF9.",
  ]},
]

def reveal(): return ' reveal'

# ================= INDEX =================
feat = CASES[:3]
feat_cards=""
for c in feat:
    feat_cards+=f'''<a class="work reveal" href="{c['file']}">
      <div class="thumb"><img src="{c['cover']}" alt="{c['title']}" loading="lazy"></div>
      <div class="body"><div class="cat">{c['cat']}</div><h3>{c['title']}</h3>
      <p>{c['summary'][:90]}…</p><span class="more">مشاهده نمونه‌کار ←</span></div></a>'''

serv_cards_home=""
for ic,t,d in SERVICES[:6]:
    serv_cards_home+=f'<div class="card reveal"><div class="ico">{ic}</div><h3>{t}</h3><p>{d}</p></div>'

index_body=f'''
<section class="hero" id="home">
  <div class="container">
    <div class="banner-card reveal">
      <img class="cover" src="assets/brand/linkedin_banner.jpg" alt="بنر آژانس عباس میرزا">
      <div class="badge"><img src="assets/brand/logo.png" alt="لوگو عباس میرزا"><span>ABBASMIRZAA Agency</span></div>
    </div>
    <div class="hero-grid">
      <div>
        <span class="eyebrow">تبلیغاتی که واقعاً می‌فروشد</span>
        <h1>برند شما را به <span class="hl">داستانی که می‌فروشد</span> تبدیل می‌کنیم</h1>
        <p class="sub">آژانس تبلیغاتی عباس میرزا از اولین خط طراحی لوگوی شما تا آخرین کلیک روی تبلیغ، کل مسیر را در اختیار می‌گیرد؛ با تمرکز بر بازده واقعی، نه آمار تزئینی.</p>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-primary">شروع همکاری ←</a>
          <a href="portfolio.html" class="btn btn-ghost">مشاهده نمونه‌کارها</a>
        </div>
      </div>
      <div class="hero-side">
        <div class="hstat reveal"><div class="n"><span data-count="47" data-suffix=" میلیارد">۰</span></div><div class="l">تومان لید در کمپین ثمر</div></div>
        <div class="hstat reveal"><div class="n"><span data-count="10" data-suffix="K+">۰</span></div><div class="l">فالوور جدید برای فردانامه</div></div>
        <div class="hstat reveal"><div class="n"><span data-count="6" data-suffix="+">۰</span></div><div class="l">پروژه و کمپین موفق</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center reveal"><span class="eyebrow">خدمات ما</span>
      <h2 class="title">هر آنچه برای رشد برند نیاز دارید</h2>
      <p class="lead">از استراتژی و برندینگ تا تبلیغات دیجیتال و گزارش‌دهی داده‌محور.</p></div>
    <div class="grid g3" style="margin-top:46px">{serv_cards_home}</div>
    <div class="center" style="margin-top:36px"><a href="services.html" class="btn btn-outline">همه خدمات</a></div>
  </div>
</section>

<section class="band">
  <div class="container grid g4 center">
    <div class="stat reveal"><div class="n"><span data-count="47" data-suffix="+">۰</span></div><div class="l">میلیارد تومان لید</div></div>
    <div class="stat reveal"><div class="n"><span data-count="627" data-suffix="K">۰</span></div><div class="l">بازدید کمپین تلگرام</div></div>
    <div class="stat reveal"><div class="n"><span data-count="481" data-suffix="+">۰</span></div><div class="l">سرمایه‌گذار جذب‌شده</div></div>
    <div class="stat reveal"><div class="n"><span data-count="6" data-suffix="+">۰</span></div><div class="l">پروژه شاخص</div></div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center reveal"><span class="eyebrow">نمونه‌کارها</span>
      <h2 class="title">پروژه‌هایی که به آن‌ها افتخار می‌کنیم</h2>
      <p class="lead">گوشه‌ای از کمپین‌ها و برندهایی که با هم ساختیم.</p></div>
    <div class="grid g3" style="margin-top:46px">{feat_cards}</div>
    <div class="center" style="margin-top:36px"><a href="portfolio.html" class="btn btn-outline">مشاهده همه نمونه‌کارها</a></div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="cta reveal">
      <h2>آماده‌اید برند خود را متحول کنید؟</h2>
      <p>بیایید درباره ایده‌ها و اهداف شما گفتگو کنیم. اولین جلسه مشاوره رایگان است.</p>
      <div class="cta-actions">
        <a href="contact.html" class="btn btn-blue">درخواست مشاوره رایگان</a>
        <a class="btn" style="background:#0a66c2;color:#fff" href="{LI}" target="_blank" rel="noopener">{LI_SVG} ما را در لینکدین دنبال کنید</a>
      </div>
    </div>
  </div>
</section>'''
page("index.html","index.html","آژانس تبلیغاتی عباس میرزا | تبلیغاتی که واقعاً می‌فروشد",
     "آژانس تبلیغاتی عباس میرزا؛ برندینگ، بازاریابی دیجیتال، تولید محتوا و کمپین‌های داده‌محور برای رشد واقعی کسب‌وکار شما.",
     index_body)

# ================= SERVICES =================
serv_cards=""
for ic,t,d in SERVICES:
    serv_cards+=f'<div class="card reveal"><div class="ico">{ic}</div><h3>{t}</h3><p>{d}</p></div>'
steps=[("کشف و تحلیل","شناخت عمیق کسب‌وکار، مخاطب و بازار شما."),
       ("استراتژی","تدوین برنامه بازاریابی و ایده خلاقانه متناسب با هدف."),
       ("اجرا","تولید و راه‌اندازی کمپین با بالاترین کیفیت."),
       ("سنجش و بهبود","گزارش شفاف نتایج و بهینه‌سازی مستمر برای رشد بیشتر.")]
steps_html=""
for t,d in steps:
    steps_html+=f'<div class="step reveal"><div class="num"></div><h4>{t}</h4><p>{d}</p></div>'
services_body=f'''
<section class="page-hero">
  <h1>خدمات ما</h1>
  <p>مجموعه‌ای کامل و یکپارچه از خدمات تبلیغاتی و بازاریابی — هدفمند، خلاقانه و داده‌محور.</p>
  <div class="crumb"><a href="index.html">خانه</a> / خدمات</div>
</section>
<section>
  <div class="container"><div class="grid g3">{serv_cards}</div></div>
</section>
<section class="band">
  <div class="container">
    <div class="center reveal" style="color:#fff"><span class="eyebrow">فرآیند کار</span>
      <h2 class="title" style="color:#fff">از ایده تا نتیجه، در ۴ گام</h2></div>
    <div class="grid g4 steps" style="margin-top:44px">{steps_html}</div>
  </div>
</section>
<section style="padding-top:60px">
  <div class="container"><div class="cta reveal">
    <h2>برای کدام خدمت به مشاوره نیاز دارید؟</h2>
    <p>تیم ما آماده است تا بهترین راهکار را برای رشد برند شما پیشنهاد دهد.</p>
    <div class="cta-actions"><a href="contact.html" class="btn btn-blue">درخواست مشاوره</a>
    <a class="btn" style="background:#0a66c2;color:#fff" href="{LI}" target="_blank" rel="noopener">{LI_SVG} لینکدین</a></div>
  </div></div>
</section>'''
page("services.html","services.html","خدمات | آژانس تبلیغاتی عباس میرزا",
     "خدمات آژانس عباس میرزا: استراتژی و برندینگ، مدیریت شبکه‌های اجتماعی، تبلیغات بله و تلگرام، لندینگ پیج و کمپین داده‌محور.",
     services_body)

# ================= PORTFOLIO =================
work_cards=""
for c in CASES:
    work_cards+=f'''<a class="work reveal" href="{c['file']}">
      <div class="thumb"><img src="{c['cover']}" alt="{c['title']}" loading="lazy"></div>
      <div class="body"><div class="cat">{c['cat']}</div><h3>{c['title']}</h3>
      <p>{c['summary'][:100]}…</p><span class="more">مشاهده جزئیات ←</span></div></a>'''
portfolio_body=f'''
<section class="page-hero">
  <h1>نمونه‌کارها</h1>
  <p>کمپین‌ها، برندها و پروژه‌هایی که با خلاقیت و داده ساختیم — از پذیره‌نویسی صندوق ثمر تا برندینگ نیلگون.</p>
  <div class="crumb"><a href="index.html">خانه</a> / نمونه‌کارها</div>
</section>
<section>
  <div class="container"><div class="grid g3">{work_cards}</div></div>
</section>
<section style="padding-top:0"><div class="container"><div class="cta reveal">
  <h2>پروژه بعدی، برند شماست</h2>
  <p>بیایید نمونه‌کار بعدی‌مان را با هم بسازیم.</p>
  <div class="cta-actions"><a href="contact.html" class="btn btn-blue">شروع پروژه</a></div>
</div></div></section>'''
page("portfolio.html","portfolio.html","نمونه‌کارها | آژانس تبلیغاتی عباس میرزا",
     "نمونه‌کارهای آژانس عباس میرزا: کمپین ثمر، هویت بصری BEBYE و نیلگون، رشد فردانامه در بله و اینستاگرام، و طراحی لندینگ پیج.",
     portfolio_body)

# ================= ABOUT =================
about_body=f'''
<section class="page-hero">
  <h1>درباره عباس میرزا</h1>
  <p>آژانسی که برند را زندگی می‌کند — تبلیغاتی که واقعاً می‌فروشد.</p>
  <div class="crumb"><a href="index.html">خانه</a> / درباره ما</div>
</section>
<section>
  <div class="container about-cols" style="display:grid;grid-template-columns:1fr 1fr;gap:54px;align-items:center">
    <div class="about-visual reveal"><img src="assets/brand/logo.png" alt="لوگو عباس میرزا"></div>
    <div class="reveal">
      <span class="eyebrow">داستان ما</span>
      <h2 class="title">از اولین خط لوگو تا آخرین کلیک تبلیغ</h2>
      <p class="lead" style="margin-bottom:6px">ما تیمی از استراتژیست‌ها، طراحان و بازاریابان خلاق هستیم که باور داریم هر برند داستانی برای گفتن دارد. مأموریت ما تبدیل این داستان به فروش بیشتر و نتیجه‌ای ملموس برای کسب‌وکار شماست — با تمرکز بر بازده واقعی، نه آمار تزئینی.</p>
      <ul class="check-list">
        <li><span class="tick">✓</span> رویکرد داده‌محور و خلاقیت بدون مرز</li>
        <li><span class="tick">✓</span> تسلط بر کل مسیر: از برندینگ تا اجرای کمپین و گزارش</li>
        <li><span class="tick">✓</span> گزارش‌دهی شفاف و قابل اندازه‌گیری</li>
        <li><span class="tick">✓</span> همراهی واقعی، نه فقط ارائه سرویس</li>
      </ul>
      <a href="contact.html" class="btn btn-primary" style="margin-top:26px">گفتگو با ما</a>
    </div>
  </div>
</section>
<section class="band">
  <div class="container grid g4 center">
    <div class="stat reveal"><div class="n"><span data-count="47" data-suffix="+">۰</span></div><div class="l">میلیارد تومان لید</div></div>
    <div class="stat reveal"><div class="n"><span data-count="481" data-suffix="+">۰</span></div><div class="l">سرمایه‌گذار جذب‌شده</div></div>
    <div class="stat reveal"><div class="n"><span data-count="10" data-suffix="K+">۰</span></div><div class="l">فالوور جدید فردانامه</div></div>
    <div class="stat reveal"><div class="n"><span data-count="6" data-suffix="+">۰</span></div><div class="l">پروژه شاخص</div></div>
  </div>
</section>
<section>
  <div class="container">
    <div class="center reveal"><span class="eyebrow">نظر مشتریان</span><h2 class="title">آن‌ها به ما اعتماد کردند</h2></div>
    <div class="grid g3" style="margin-top:44px">
      <div class="quote reveal"><div class="stars">★★★★★</div><p>«تیم عباس میرزا واقعاً برند ما را متحول کرد. حتی با محدودیت‌های لحظه‌آخری، کمپین را نجات دادند و به نتیجه رساندند.»</p><div class="who"><span class="ava">ر</span><div><b>رضا کاظمی</b><small>مدیر سرمایه‌گذاری</small></div></div></div>
      <div class="quote reveal"><div class="stars">★★★★★</div><p>«پیج اینستاگرام ما ماه‌ها درجا می‌زد؛ با تغییر رویکرد محتوایی، در کمتر از ۶ ماه بیش از ۳۰٪ رشد کردیم.»</p><div class="who"><span class="ava">س</span><div><b>سارا محمدی</b><small>مدیر برند فردانامه</small></div></div></div>
      <div class="quote reveal"><div class="stars">★★★★★</div><p>«هویت بصری نیلگون دقیقاً همان چیزی شد که می‌خواستیم؛ ریشه‌دار، خوانا و ماندگار.»</p><div class="who"><span class="ava">م</span><div><b>مهدی نوری</b><small>بنیان‌گذار نیلگون</small></div></div></div>
    </div>
  </div>
</section>'''
page("about.html","about.html","درباره ما | آژانس تبلیغاتی عباس میرزا",
     "درباره آژانس تبلیغاتی عباس میرزا؛ تیمی خلاق و داده‌محور که کل مسیر برند شما را از طراحی تا اجرای کمپین در اختیار می‌گیرد.",
     about_body)

# ================= CONTACT =================
contact_body=f'''
<section class="page-hero">
  <h1>تماس با ما</h1>
  <p>بیایید چیزی بزرگ بسازیم. پیام خود را بفرستید یا از طریق راه‌های زیر در ارتباط باشید.</p>
  <div class="crumb"><a href="index.html">خانه</a> / تماس</div>
</section>
<section>
  <div class="container contact-grid">
    <div class="reveal">
      <span class="eyebrow">راه‌های ارتباطی</span>
      <h2 class="title">در دسترس شما هستیم</h2>
      <p class="lead" style="margin-bottom:26px">تیم ما در سریع‌ترین زمان پاسخگوست. اولین جلسه مشاوره رایگان است.</p>
      <a class="info-card" href="tel:09127296658"><div class="ic">📞</div><div><b>تلفن تماس</b><span>۰۹۱۲۷۲۹۶۶۵۸</span></div></a>
      <a class="info-card" href="mailto:aliakbar.abbasi9@gmail.com"><div class="ic">📧</div><div><b>ایمیل</b><span>aliakbar.abbasi9@gmail.com</span></div></a>
      <div class="info-card"><div class="ic">📍</div><div><b>آدرس</b><span>تهران، میدان ونک</span></div></div>
      <a class="info-card" href="{LI}" target="_blank" rel="noopener">
        <div class="ic" style="background:#0a66c2;color:#fff">{LI_SVG}</div>
        <div><b>لینکدین</b><span>linkedin.com/company/abbasmirzaa-agency</span></div>
      </a>
    </div>
    <form onsubmit="return submitForm(event)">
      <div class="field"><label>نام و نام خانوادگی</label><input type="text" required placeholder="نام شما"></div>
      <div class="field"><label>ایمیل</label><input type="email" required placeholder="email@example.com"></div>
      <div class="field"><label>موضوع</label><input type="text" placeholder="درباره چه خدمتی صحبت کنیم؟"></div>
      <div class="field"><label>پیام</label><textarea rows="4" required placeholder="پیام خود را بنویسید..."></textarea></div>
      <button class="btn btn-primary" type="submit">ارسال پیام ←</button>
      <p class="form-note" id="formNote">پاسخ معمولاً در کمتر از ۲۴ ساعت ارسال می‌شود.</p>
    </form>
  </div>
</section>'''
page("contact.html","contact.html","تماس با ما | آژانس تبلیغاتی عباس میرزا",
     "با آژانس تبلیغاتی عباس میرزا در تماس باشید — ایمیل، وب‌سایت و لینکدین. اولین جلسه مشاوره رایگان است.",
     contact_body)

# ================= CASE PAGES =================
for i,c in enumerate(CASES):
    gallery="".join(f'<img src="{src}" alt="{c["title"]} - {n+1}" loading="lazy">'
                    for n,src in enumerate(imgs(c["prefix"])))
    results="".join(f'<div class="result reveal"><div class="n">{n}</div><div class="l">{l}</div></div>'
                    for n,l in c["results"])
    story="".join(f'<p>{p}</p>' for p in c["story"])
    prev_c=CASES[i-1] if i>0 else CASES[-1]
    next_c=CASES[i+1] if i<len(CASES)-1 else CASES[0]
    meta=f'<span>🏷️ {c["cat"]}</span><span>👤 {c["client"]}</span>'
    body=f'''
<section class="page-hero">
  <h1>{c['title']}</h1>
  <p>{c['summary']}</p>
  <div class="case-meta">{meta}</div>
  <div class="crumb"><a href="index.html">خانه</a> / <a href="portfolio.html">نمونه‌کارها</a> / {c['title']}</div>
</section>

<section style="padding-bottom:40px">
  <div class="container"><div class="case-results">{results}</div></div>
</section>

<section style="padding-top:20px">
  <div class="container case-body reveal">
    <span class="eyebrow">شرح پروژه</span>
    <h2 class="title" style="margin-bottom:18px">چه کاری انجام دادیم</h2>
    {story}
  </div>
</section>

<section style="padding-top:20px">
  <div class="container">
    <div class="center reveal" style="margin-bottom:36px"><span class="eyebrow">گالری</span>
      <h2 class="title">نمایی از خروجی پروژه</h2></div>
    <div class="gallery">{gallery}</div>
  </div>
</section>

<section style="padding-top:20px">
  <div class="container">
    <div class="case-nav">
      <a href="{prev_c['file']}" class="btn btn-outline">→ {prev_c['title']}</a>
      <a href="portfolio.html" class="btn btn-blue">همه نمونه‌کارها</a>
      <a href="{next_c['file']}" class="btn btn-outline">{next_c['title']} ←</a>
    </div>
  </div>
</section>

<section style="padding-top:40px"><div class="container"><div class="cta reveal">
  <h2>پروژه‌ای مشابه دارید؟</h2>
  <p>بیایید نتیجه‌ای مشابه برای برند شما بسازیم.</p>
  <div class="cta-actions"><a href="contact.html" class="btn btn-blue">شروع گفتگو</a>
  <a class="btn" style="background:#0a66c2;color:#fff" href="{LI}" target="_blank" rel="noopener">{LI_SVG} لینکدین</a></div>
</div></div></section>

<div class="lightbox" id="lightbox"><img src="" alt=""></div>'''
    page(c["file"],"portfolio.html",f"{c['title']} | نمونه‌کار آژانس عباس میرزا",c["summary"],body)

print("ALL DONE")
