"""App configuration: paths, model, and search defaults."""

from pathlib import Path

# Project root (parent of backend/)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Model
MODEL_NAME = "clip-ViT-B-32"  # SentenceTransformer model for text + image

# Paths
INDEX_PATH = ROOT_DIR / "data" / "index.faiss"
DB_PATH = ROOT_DIR / "data" / "archive.db"
ASSET_PATH = ROOT_DIR / "assets"

# Search
TOP_K_DEFAULT = 10
