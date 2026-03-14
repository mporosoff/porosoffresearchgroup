# Porosoff Research Group Website

**Live site:** [porosoffresearchgroup.com](https://porosoffresearchgroup.com)  
**Hosted via:** GitHub Pages with custom domain

---

## File Structure

```
porosoff-site/
├── index.html          ← Home
├── news.html           ← News & highlights
├── people.html         ← Team members
├── research.html       ← Research areas
├── publications.html   ← Publication list
├── podcat.html         ← PodCAT podcast
├── contact.html        ← Contact & join us
├── css/
│   └── style.css       ← All shared styles
├── js/
│   └── main.js         ← Shared JS (nav, accordion)
├── images/
│   ├── people/         ← Profile photos
│   │   ├── marc-porosoff.jpg
│   │   ├── shane-michtavy.jpg
│   │   ├── hasitha-perera.jpg
│   │   └── [firstname-lastname].jpg for each person
│   ├── covers/         ← Journal cover images
│   │   ├── ees-catalysis-2026.jpg
│   │   └── langmuir-2024.jpg
│   └── group/          ← Group photos (optional)
├── CNAME               ← Custom domain config
└── README.md           ← This file
```

---

## Adding Images

### Profile photos
1. Name the file `firstname-lastname.jpg` (all lowercase, hyphenated)
2. Place it in `images/people/`
3. Recommended: square crop, face centered, 400×400px minimum, under 250KB
4. The HTML already references these filenames — photos appear automatically

### Journal covers
1. Place files at `images/covers/ees-catalysis-2026.jpg` and `images/covers/langmuir-2024.jpg`
2. Recommended: at least 280×350px, under 200KB
3. Appear automatically on the Publications page

### Compressing images
Use [Squoosh](https://squoosh.app/) (free, browser-based) to compress images before uploading. Target: under 250KB per photo.

---

## Deploying to GitHub Pages

### First-time setup

1. **Create a GitHub account** at github.com if you don't have one
2. **Create a new repository** named `porosoffresearchgroup.com` (or any name)
3. **Upload all files** — drag the entire `porosoff-site/` folder contents into the repo (not the folder itself, just the files inside it)
4. Go to **Settings → Pages**
5. Under "Source", select **Deploy from a branch**
6. Choose branch: `main`, folder: `/ (root)`
7. Click **Save**

GitHub will build and deploy your site. It may take 1–2 minutes.

---

## Connecting Your Custom Domain (porosoffresearchgroup.com)

Your domain is currently registered through Squarespace. You have two options:

### Option A: Keep domain at Squarespace, point DNS to GitHub (RECOMMENDED — easiest)

You don't need to transfer anything. Just update the DNS records in Squarespace:

1. Log into Squarespace → **Domains** → click `porosoffresearchgroup.com`
2. Click **DNS Settings** (or "Advanced DNS")
3. Delete any existing `A` records pointing to Squarespace servers
4. Add these **four A records** (pointing to GitHub Pages):

   | Type | Host | Value |
   |------|------|-------|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |

5. Add a **CNAME record**:

   | Type | Host | Value |
   |------|------|-------|
   | CNAME | www | YOUR-GITHUB-USERNAME.github.io |

   (Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username)

6. In your GitHub repo: **Settings → Pages → Custom domain** → type `porosoffresearchgroup.com` → Save
7. Check the box for **"Enforce HTTPS"** (gives you a free SSL certificate)

DNS changes take 10 minutes to 48 hours to propagate. The `CNAME` file in this repo is already configured.

### Option B: Transfer the domain to a different registrar

Only do this if you want to move away from Squarespace entirely. Transfer to Namecheap (~$12/yr) or Cloudflare (~$10/yr at cost). The process takes 5–7 days and requires an authorization code from Squarespace.

---

## Making Updates

### Updating content
Edit the relevant `.html` file directly in GitHub (click the file → pencil icon → edit → commit changes). Changes go live in ~30 seconds.

### Adding a new team member
1. Edit `people.html`
2. Add a new `<div class="ppl-card">` block in the appropriate section (Graduate Students or Undergraduates), following the same pattern as existing members
3. Add their photo to `images/people/` (optional — initials avatar shows automatically if no photo)

### Adding a new publication
1. Edit `publications.html`
2. Add a new `<div class="pub-item">` block at the top of the `pub-list` div
3. Optionally add a news item in `news.html`

---

## Questions?
Contact whoever built this site, or open an issue in the GitHub repository.
