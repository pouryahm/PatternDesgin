# 🎯 تمرین Abstract Factory — سیستم نوتیفیکیشن

## سناریو

می‌خواهیم یک سیستم نوتیفیکیشن طراحی کنیم که بتونه پیام‌ها رو به روش‌های مختلف بفرسته:

* Email
* SMS
* Push Notification (مثلاً اپلیکیشن موبایل)

هر نوع نوتیفیکیشن باید سه بخش داشته باشه:

* Message Content (جزئیات پیام)
* Sender Info (چه کسی فرستاده)
* Delivery Method (روش ارسال، مثل سرور ایمیل، سیم‌کارت، یا سرویس پوش)

## قرارداد (Abstractها)

NotificationBase → هر نوتیفیکیشن باید سه property داشته باشه:

* content (برگردونه یک شیء Content)
* sender (برگردونه یک شیء Sender)
* delivery (برگردونه یک شیء Delivery)

ContentBase, SenderBase, DeliveryBase → هر کدوم یک show() داشته باشن.

خواسته‌ها

سه خانواده مختلف درست کن:

EmailNotification (با EmailContent, EmailSender, EmailDelivery)

SMSNotification (با کلاس‌های خودش)

PushNotification (با کلاس‌های خودش)

در حلقهٔ اصلی، یه لیست از نوتیفیکیشن‌های مختلف بساز و مثل تمرین قبل، برای هرکدوم content.show(), sender.show(), delivery.show() رو چاپ کن.

مطمئن شو که هیچ if/else برای تشخیص نوع نوتیفیکیشن توی حلقهٔ اصلی وجود نداشته باشه.

👉 این تمرین سطح متوسطه چون:

شبیه همون الگو هست، پس آشناست.

سه خانواده داری (چالش بیشتر از دو تا).

باید فکر کنی چه داده‌ای برای هرکدوم معنی‌دار باشه (مثلاً EmailSender = آدرس ایمیل، SMSSender = شماره تلفن، PushSender = نام اپلیکیشن).