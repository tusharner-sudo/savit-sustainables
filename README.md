# Savit Sustainables Website

Eco-friendly products website — static HTML, hosted on Netlify, domain on Spaceship.com.

## Project Structure

```
savit-sustainables/
├── index.html                         # Home page
├── about.html                         # About us
├── contact.html                       # Contact with Netlify form
├── corporate-gifting.html             # Corporate kits page
├── products/
│   ├── index.html                     # All products overview
│   ├── bamboo-drinkware.html          # Bamboo bottles & mugs
│   ├── bamboo-stationery.html         # Seed pens, pencils, diaries
│   ├── jute-bags.html                 # Jute zip bags
│   ├── compostable-bags.html          # Compostable bags
│   ├── eco-cutlery.html               # Wooden spoons, areca plates
│   ├── personal-care.html             # Neem combs, bamboo brushes
│   └── eco-goods.html                 # Amplifiers, seed balls, toys
├── css/
│   └── style.css                      # All styles
├── js/
│   └── script.js                      # Navigation, animations, forms
├── images/
│   └── favicon.svg                    # Browser tab icon
├── netlify.toml                       # Netlify config
└── README.md
```

## Setup Instructions

### 1. Add Your Images

Replace these image files (use WebP format for best performance):

| Image File | Suggested Size | Description |
|---|---|---|
| `images/logo.jpg` | 200x200px | Company logo |
| `images/hero-image.jpg` | 1040x780px | Hero section photo |
| `images/about-image.jpg` | 1040x780px | About section photo |
| `images/og-image.jpg` | 1200x630px | Social share preview |
| `images/products/bamboo-drinkware.jpg` | 640x480px | Product category |
| `images/products/bamboo-stationery.jpg` | 640x480px | Product category |
| `images/products/jute-bags.jpg` | 640x480px | Product category |
| `images/products/compostable-bags.jpg` | 640x480px | Product category |
| `images/products/eco-cutlery.jpg` | 640x480px | Product category |
| `images/products/personal-care.jpg` | 640x480px | Product category |
| `images/products/eco-goods.jpg` | 640x480px | Product category |
| `images/products/corporate-kits.jpg` | 640x480px | Product category |
| `images/favicon.ico` | 32x32px | Browser favicon |

### 2. Deploy to Netlify

1. Push this folder to a GitHub/GitLab repository
2. Log in to [Netlify](https://app.netlify.com)
3. Click **Add new site** → **Import an existing project**
4. Connect your repository
5. Deploy settings are already in `netlify.toml` — no changes needed
6. Click **Deploy site**

### 3. Connect Your Domain (Spaceship.com)

1. In Netlify: **Site settings** → **Domain management** → **Add custom domain**
2. Enter: `www.savitsustainables.com`
3. In Spaceship DNS settings, set these records:

| Type | Name | Value |
|---|---|---|
| A | @ | `75.2.60.5` |
| A | @ | `99.83.190.102` |
| CNAME | www | `your-site.netlify.app` |

(Replace `your-site.netlify.app` with your actual Netlify site URL)

4. Wait for DNS propagation (up to 48 hours, typically 1-2 hours)

### 4. Enable Netlify Forms (for Contact Form)

Netlify Forms works automatically with `data-netlify="true"` — no backend needed.
After deploying, go to **Site settings** → **Forms** to see submissions.

### 5. Enable HTTPS

Netlify automatically provisions SSL certificates via Let's Encrypt.
Go to **Domain management** → **HTTPS** and enable it.

## Customization

- **Colors**: Edit CSS variables in `css/style.css` under `:root`
- **Content**: Edit the individual HTML files
- **Phone/Email/Social**: Update across all HTML files (search for existing values)
- **WhatsApp number**: Update in all HTML files (search for `919665702738`)

## SEO Checklist

- [x] Meta descriptions per page
- [x] Open Graph tags per page
- [x] Twitter Card tags per page
- [x] JSON-LD structured data (Organization schema)
- [x] Semantic HTML headings (H1 → H2 → H3)
- [x] Descriptive image alt attributes
- [x] Sitemap.xml (create after deployment — use an online generator)
- [x] Clean URL structure
