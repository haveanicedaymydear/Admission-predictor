from pathlib import Path
import gzip
import shutil

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "data" / "diabetes.csv.gz",
    ROOT / "workflow" / "diabetes_prediction.ows.gz",
]

for source in FILES:
    target = source.with_suffix("")
    with gzip.open(source, "rb") as src, target.open("wb") as dst:
        shutil.copyfileobj(src, dst)
    print(f"Created {target.relative_to(ROOT)}")
