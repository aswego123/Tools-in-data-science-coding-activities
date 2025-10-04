from PIL import Image
import os

def compress_to_lossless_webp(input_path, output_path, target_size=400):
    """
    Compress image to lossless WebP format.
    WebP lossless can achieve better compression than PNG.
    """
    
    with Image.open(input_path) as img:
        original_size = os.path.getsize(input_path)
        print(f"Original PNG: {img.size[0]}x{img.size[1]}, {original_size} bytes")
        print(f"Mode: {img.mode}, Colors: {len(set(img.getdata()))}\n")
        
        # Crop to actual content if RGBA
        if img.mode == 'RGBA':
            bbox = img.getbbox()
            if bbox:
                img = img.crop(bbox)
                print(f"Cropped to: {img.size}")
        
        # Method 1: Lossless WebP with maximum compression
        print("\nTrying lossless WebP compression...")
        img.save(output_path, 'WEBP', lossless=True, quality=100, method=6)
        size = os.path.getsize(output_path)
        print(f"Lossless WebP: {size} bytes")
        
        if size < target_size:
            print(f"\n✓ SUCCESS! Compressed to {size} bytes (under {target_size} bytes)")
            print(f"Savings: {original_size - size} bytes ({((original_size-size)/original_size*100):.1f}%)")
            
            # Verify losslessness
            with Image.open(input_path) as orig:
                with Image.open(output_path) as compressed:
                    orig_pixels = list(orig.getdata())
                    comp_pixels = list(compressed.getdata())
                    if orig_pixels == comp_pixels:
                        print("✓ Verified: Compression is truly lossless!")
                    else:
                        print("⚠ Warning: Pixels differ (may be color space conversion)")
            
            return True
        else:
            print(f"\n✗ Still {size - target_size} bytes over target")
            
            # Try converting to RGB if RGBA (sometimes smaller)
            if img.mode == 'RGBA':
                print("\nTrying RGB conversion...")
                # Check if alpha channel is needed
                has_transparency = any(p[3] < 255 for p in img.getdata())
                if not has_transparency:
                    img_rgb = img.convert('RGB')
                    img_rgb.save('output_rgb.webp', 'WEBP', lossless=True, quality=100, method=6)
                    size_rgb = os.path.getsize('output_rgb.webp')
                    print(f"RGB WebP: {size_rgb} bytes")
                    
                    if size_rgb < size:
                        os.rename('output_rgb.webp', output_path)
                        size = size_rgb
                    else:
                        os.remove('output_rgb.webp')
            
            if size < target_size:
                print(f"\n✓ SUCCESS with RGB! {size} bytes")
                return True
        
        print("\nWebP lossless compression complete.")
        print(f"Final size: {size} bytes")
        
        if size >= target_size:
            print(f"\nTo get under {target_size} bytes losslessly:")
            print("1. The image content needs to be simpler or smaller")
            print("2. Or install cwebp for better compression:")
            print(f"   sudo apt install webp")
            print(f"   cwebp -lossless -z 9 {input_path} -o {output_path}")
        
        return size < target_size

if __name__ == "__main__":
    print("="*70)
    print("LOSSLESS WEBP COMPRESSION")
    print("="*70 + "\n")
    
    success = compress_to_lossless_webp('download.png', 'compressed_output.webp', target_size=400)
    
    if success:
        print("\n" + "="*70)
        print("✓ Task completed successfully!")
        print("="*70)
        print("\nYour compressed image: compressed_output.webp")