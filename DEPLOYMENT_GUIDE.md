# Deploy to Render.com (5 Minutes)

## Step 1: Create GitHub Repository

1. Go to **https://github.com/new**
2. Create a new repository named: `markitdown-converter`
3. Click "Create repository"
4. Copy the repository URL (it will look like: `https://github.com/YOUR_USERNAME/markitdown-converter.git`)

## Step 2: Push Your Code to GitHub

After creating the repo, you'll see instructions. Run these commands in PowerShell:

```powershell
cd 'C:\Users\monny\markitdown-converter'
git remote add origin https://github.com/YOUR_USERNAME/markitdown-converter.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy to Render

1. Go to **https://render.com**
2. Sign up (or log in) with your GitHub account
3. Click **"New +"** → **"Web Service"**
4. Select **"Connect a repository"**
5. Find and select `markitdown-converter`
6. Fill in the settings:
   - **Name:** markitdown-converter
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
7. Click **"Create Web Service"**

## Step 4: Wait for Deployment

- Render will build and deploy your app
- You'll get a live URL like: `https://markitdown-converter.onrender.com`
- Share this URL with anyone to use your converter!

---

**That's it!** Your app is now live on the internet. 🚀
