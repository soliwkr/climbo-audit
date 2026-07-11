# Review Requests

> **One-line summary:** Review requests are the messages you send to customers asking them to leave a review — the fuel that starts the entire flywheel.

---
tags: [features, review-collection, core]
sources: [BRocA7husPU]
last_updated: 2026-07-11
---

## Overview

Getting more reviews starts with asking for them. Most businesses don't ask, so they don't get them. Climbo gives your clients three ways to ask — choose the one that fits the business type.

This is the most important part of the setup. Giacomo's training states: "The review collection process is 90% of the sales. If you set it up correctly, they will get results during the free trial. If not, nothing else matters."

## How it works

### Method 1 — QR Code / Kiosk Mode

Best for: high-traffic physical locations (restaurants, salons, gyms, retail)

Print the Climbo-generated kiosk page and place it at your client's reception, counter, or checkout area. Customers scan the QR code and land on the review link.

Setup:
1. Go to client account → **Review Link** → customize with client's logo and message
2. Go to **Kiosk Mode** → print the page (or download as PDF)
3. Laminate it. Place it where customers will see it after their experience.
4. Train the staff to say: "If you enjoyed your visit, scan the code — takes 30 seconds."

### Method 2 — Manual Quick Request

Best for: low-volume professional services (lawyers, dentists, accountants, consultants)

After each appointment, the client sends a one-tap review request directly to that customer.

Setup:
1. Create a WhatsApp or SMS template in `Request → Templates`
2. Example template: "Hi [Name], thank you for visiting us today. If you have a moment, we'd love your feedback: [Review Link]"
3. After each appointment: `Request → Send → Quick Request` → select contact → send

The platform shows open rates and click rates so you can see if the message is reaching people.

### Method 3 — Auto-Send (CRM Integration)

Best for: businesses with a CRM or contact list, or those willing to use Climbo as their CRM

When a new contact is added (manually or via automation), the platform automatically sends a review request after a configurable delay (e.g., 15 minutes after the service date).

Setup:
1. Go to **Auto Send** and enable the automation
2. Set the trigger: "Send request X hours after service date"
3. Select the template to use
4. Connect a CRM via Zapier, or have the client add contacts manually (or upload CSV)

Google Sheets integration: If the client tracks customers in a Google Sheet, Zapier can push new rows to Climbo automatically. Every new row = new review request sent. Zero manual work after setup.

## The review link

All three methods point to the same place: the **review link**. This is the unique URL Climbo generates for each client.

When a customer opens the link, they see:
- The client's logo and name
- A simple rating prompt (1–5 stars)
- 1–3 stars → option to leave private feedback to the business (not public)
- 4–5 stars → directed to leave a public review on Google (or other connected platforms)

This is compliant. Both paths are available to every customer. See [[compliance/google-review-policy-2026]].

Clients can also enable **video testimonials** from the review link — customers can record a short video review directly.

## Key details / Tips

- **Train the staff, not just the system.** The QR code sitting on the counter does nothing if the employee never mentions it. Build a verbal habit: "Would you mind scanning the QR code for us?"
- **Send within 24 hours of the experience.** Review request open rates drop sharply after 48 hours.
- **Multiple platforms.** The review link can offer choices beyond Google — Yelp, Tripadvisor, Booking.com, etc. Focus on Google first unless the industry has a dominant niche platform.
- **Reminders.** If a customer doesn't click the link, a follow-up reminder can be scheduled automatically. Enable this in template settings.
- **Complaint Link.** Climbo also offers a dedicated complaint link — a separate URL you can share with customers who had a bad experience, giving them a private channel. This reduces public negative reviews without gating.

## Related

- [[features/nfc-cards]] — physical NFC alternative to QR codes
- [[features/google-sheets]] — auto-sync contacts from a spreadsheet
- [[ai-agents/seo-agent]] — what happens after a review arrives
- [[compliance/google-review-policy-2026]] — what's allowed and what's not

## Sources

- YouTube: [Start a $3k/mo Reputation Management Business](BRocA7husPU) — complete setup walkthrough of all three methods
