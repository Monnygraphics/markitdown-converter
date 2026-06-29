# MarkItDown Web Converter

A beautiful web application to convert any file format to Markdown for use with AI chat models.

## Features

✅ **Drag & Drop Upload** - Simply drag files onto the upload area  
✅ **Real-time Preview** - See the converted markdown instantly  
✅ **Copy to Clipboard** - Paste directly into your AI chat  
✅ **Download Markdown** - Save as .md file for later use  
✅ **No Server Upload** - Conversions happen locally on your machine  
✅ **Multiple Formats** - Supports 30+ file types  

## Supported File Types

**Documents**: PDF, DOCX, PPTX, XLSX, XLS, CSV, TXT  
**Images**: PNG, JPG, JPEG, GIF, SVG, WEBP, BMP, TIFF  
**Web**: HTML, XML, JSON  
**Media**: MP3, MP4, WEBM, MOV, AVI, WAV  

## Quick Start

### 1. Install Flask (One-time setup)
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
python app.py
```

You'll see:
```
 * Running on http://localhost:5000
 * Press CTRL+C to quit
```

### 3. Open in Browser
Go to: **http://localhost:5000**

That's it! 🎉

## Usage

1. **Upload a file** - Drag & drop or click to select
2. **Wait for conversion** - Takes a few seconds
3. **Copy or Download** - Use the buttons to:
   - **Copy** - Copy markdown to clipboard and paste into ChatGPT, Claude, etc.
   - **Download** - Save as `.md` file on your computer

## Using Converted Markdown with AI Chats

### ChatGPT / Claude / Gemini
Simply paste the markdown content directly into the chat. The AI will understand the formatting.

### Example Workflow
1. Upload `document.pdf` → converts to markdown
2. Click **Copy** → markdown is on your clipboard
3. Go to ChatGPT and paste → ready to analyze
4. Ask: "Can you summarize this document?" or "Extract the key points"

## Troubleshooting

**"File type not allowed"**
- The file type isn't supported. Check the supported list above.
- Try converting via: PDF → Markdown first

**"Conversion timeout"**
- File is too large. Try splitting into smaller chunks.

**"Can't access http://localhost:5000"**
- Make sure `python app.py` is running
- Try `http://127.0.0.1:5000` instead

## Requirements

- Python 3.8+
- markitdown (already installed)
- Flask 3.0+

## Stop the Server

Press `CTRL+C` in the terminal running `python app.py`

---

**Made with ❤️ for AI enthusiasts**
