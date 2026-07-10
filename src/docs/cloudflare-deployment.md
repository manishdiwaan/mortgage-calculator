# Cloudflare Pages Deployment — URMortgage.online

## Step 1: Push to GitHub

On your Mac:
```bash
cd ~/Documents/mortgage-calculator
tar xzf ~/Downloads/urmortgage-deploy.tar.gz
git add .
git commit -m "feat: astro SEO platform with calculator migration"
git push origin main
```

## Step 2: Create Cloudflare Pages Project

1. Log in to **dash.cloudflare.com**
2. Go to **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
3. Select your GitHub account → select **manishdiwaan/mortgage-calculator**
4. Configure build settings:

| Setting | Value |
|---------|-------|
| Production branch | `main` |
| Build command | `cd src && npm install --legacy-peer-deps && npm run build` |
| Build output directory | `src/dist` |
| Node.js version | `22` (set in Environment Variables: `NODE_VERSION` = `22`) |

5. Click **Save and Deploy**

## Step 3: Add Custom Domain

1. After first deploy succeeds, go to **Custom domains**
2. Add `urmortgage.online`
3. Add `www.urmortgage.online`
4. Cloudflare will show you DNS records to update

## Step 4: Update DNS at GoDaddy

### Remove old GitHub Pages records:
- Delete A records: 185.199.108.153, .109, .110, .111
- Delete CNAME www → manishdiwaan.github.io

### Add new Cloudflare Pages records:
- CNAME `@` → `urmortgage-online.pages.dev`
- CNAME `www` → `urmortgage-online.pages.dev`

(The exact `.pages.dev` subdomain will be shown in your Cloudflare dashboard)

## Step 5: Verify

After DNS propagates (5-30 minutes):
- https://urmortgage.online/ → new home page with country hubs
- https://urmortgage.online/calculator/ → your calculator (unchanged)
- https://urmortgage.online/australia/ → Australia country hub
- https://urmortgage.online/australia/property-buying-guide/ → pillar guide
- https://urmortgage.online/australia/blog/first-home-buyer-guide/ → blog post
- https://urmortgage.online/australia/faqs/ → 50 FAQs
- https://urmortgage.online/privacy/ → privacy policy
- https://urmortgage.online/terms/ → terms of use
- SSL should auto-provision via Cloudflare

## Step 6: Disable GitHub Pages

1. Go to github.com/manishdiwaan/mortgage-calculator → Settings → Pages
2. Set source to "None"
3. Delete the CNAME file from the repo (Cloudflare handles the domain now)

```bash
cd ~/Documents/mortgage-calculator
rm CNAME
git add . && git commit -m "chore: remove CNAME, using Cloudflare Pages" && git push
```

## Ongoing: Auto-Deploy

Every `git push` to `main` triggers a Cloudflare Pages build. This means:
- n8n commits a new blog post → Cloudflare auto-deploys → live in ~2 minutes
- You edit content locally → push → live in ~2 minutes
- No manual deploys needed

## Rollback

If anything goes wrong, Cloudflare Pages keeps all previous deployments. Go to your project → Deployments → click any previous build → "Rollback to this deployment."
