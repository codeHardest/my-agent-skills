#!/bin/bash
# Install all dependencies for video-summarizer skill

set -e

echo "=========================================="
echo "Video Summarizer - Dependency Installer"
echo "=========================================="
echo ""

# ==========================================
# 1. uv (Python package manager)
# ==========================================
echo "[1/6] Checking uv..."
if ! command -v uv &> /dev/null; then
    echo "  Installing uv..."
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        # Add uv to PATH for current session
        export PATH="$HOME/.local/bin:$PATH"
    else
        echo "  Error: Unsupported OS. Please install uv manually:"
        echo "    https://docs.astral.sh/uv/getting-started/installation/"
        exit 1
    fi
    echo "  uv installed"
else
    echo "  uv: OK"
fi

# ==========================================
# 2. ffmpeg (required for audio processing)
# ==========================================
echo ""
echo "[2/6] Checking ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "  Installing ffmpeg..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if command -v brew &> /dev/null; then
            brew install ffmpeg
        else
            echo "  Error: Homebrew not found. Please install ffmpeg manually:"
            echo "    brew install ffmpeg"
            exit 1
        fi
    elif [[ -f /etc/debian_version ]]; then
        sudo apt-get update && sudo apt-get install -y ffmpeg
    elif [[ -f /etc/redhat-release ]]; then
        sudo dnf install -y ffmpeg
    else
        echo "  Error: Please install ffmpeg manually"
        exit 1
    fi
    echo "  ffmpeg installed"
else
    echo "  ffmpeg: OK"
fi

# Check ffprobe (included with ffmpeg)
if ! command -v ffprobe &> /dev/null; then
    echo "  Error: ffprobe not found (should be included with ffmpeg)"
    exit 1
else
    echo "  ffprobe: OK"
fi

# ==========================================
# 3. yt-dlp (required for video downloading)
# ==========================================
echo ""
echo "[3/6] Checking yt-dlp..."
if ! command -v yt-dlp &> /dev/null; then
    echo "  Installing yt-dlp with uv..."
    uvx --from yt-dlp yt-dlp --version > /dev/null 2>&1 || uv tool install yt-dlp
    echo "  yt-dlp installed"
else
    echo "  yt-dlp: OK"
fi

# ==========================================
# 4. browser-cookie3 (for Bilibili subtitle access)
# ==========================================
echo ""
echo "[4/6] Checking browser-cookie3..."
if python3 -c "import browser_cookie3" 2>/dev/null; then
    echo "  browser-cookie3: OK"
else
    echo "  Installing browser-cookie3..."
    pip install browser-cookie3
    echo "  browser-cookie3 installed"
fi

# ==========================================
# 5. faster-whisper (managed by uv)
# ==========================================
echo ""
echo "[5/6] Checking faster-whisper..."
echo "  faster-whisper will be automatically managed by uv"
echo "  (installed on-demand when running transcription scripts)"

# ==========================================
# 6. Python (check version)
# ==========================================
echo ""
echo "[6/6] Checking Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo "  Python: $PYTHON_VERSION"

    # Check if version >= 3.8
    MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    if [[ $MAJOR -lt 3 ]] || [[ $MAJOR -eq 3 && $MINOR -lt 8 ]]; then
        echo "  Warning: Python 3.8+ recommended (current: $PYTHON_VERSION)"
    fi
else
    echo "  Error: Python 3 not found"
    exit 1
fi

# ==========================================
# Summary
# ==========================================
echo ""
echo "=========================================="
echo "All dependencies installed successfully!"
echo "=========================================="
echo ""
echo "Installed tools:"
echo "  - uv: $(uv --version 2>&1)"
echo "  - ffmpeg: $(ffmpeg -version 2>&1 | head -1 | cut -d' ' -f3)"
echo "  - yt-dlp: $(yt-dlp --version 2>&1 || echo 'will be installed on first use')"
echo "  - browser-cookie3: for Bilibili subtitle access"
echo "  - faster-whisper: managed by uv (auto-installed)"
echo "  - Python: $PYTHON_VERSION"
echo ""
echo "You can now use the video-summarizer skill!"
echo "Python dependencies will be automatically managed by uv."
