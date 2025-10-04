from pathlib import Path
from PIL import Image

def compress_image(input_path: Path, output_path: Path, quality: int = 85) -> None:
    """Compress an image while maintaining reasonable quality."""
    with Image.open(input_path) as img:
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(output_path, 'WEBP', quality=quality, optimize=True)

# Batch process images
for p in Path('input').glob('*.png'):
    compress_image(p, p.with_suffix('.webp'))