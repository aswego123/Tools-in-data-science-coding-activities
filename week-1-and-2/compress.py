from PIL import Image
import os

def compress_lossless_png(input_path, output_path, target_size=400):
    """
    Compress a PNG image losslessly to under target_size bytes.
    Strategies:
    1. Reduce color palette if possible
    2. Try different PNG filters and compression levels
    3. Remove metadata
    """
    
    with Image.open(input_path) as img:
        original_size = os.path.getsize(input_path)
        print(f"Original image: {img.size[0]}x{img.size[1]}, {img.mode}, {original_size} bytes")
        
        # Remove any metadata
        img_no_meta = Image.new(img.mode, img.size)
        img_no_meta.putdata(list(img.getdata()))
        
        # Strategy 1: Try converting to palette mode if possible
        if img.mode in ('RGB', 'RGBA'):
            # Count unique colors
            colors = img.getcolors(maxcolors=256)
            if colors and len(colors) <= 256:
                print(f"Image has {len(colors)} unique colors - converting to palette mode")
                img_palette = img.convert('P', palette=Image.ADAPTIVE, colors=len(colors))
                img_palette.save(output_path, 'PNG', optimize=True, compress_level=9)
                size = os.path.getsize(output_path)
                print(f"Palette PNG: {size} bytes")
                
                if size < target_size:
                    print(f"✓ Success! Compressed to {size} bytes")
                    return
        
        # Strategy 2: Maximum PNG compression
        img_no_meta.save(output_path, 'PNG', optimize=True, compress_level=9)
        size = os.path.getsize(output_path)
        print(f"Optimized PNG: {size} bytes")
        
        if size < target_size:
            print(f"✓ Success! Compressed to {size} bytes")
            return
        
        # Strategy 3: Try 1-bit mode if image is monochrome
        if img.mode in ('L', 'RGB', 'RGBA'):
            try:
                img_1bit = img.convert('1')
                img_1bit.save(output_path, 'PNG', optimize=True, compress_level=9)
                size = os.path.getsize(output_path)
                print(f"1-bit PNG: {size} bytes")
                
                if size < target_size:
                    print(f"✓ Success! Compressed to {size} bytes")
                    return
            except:
                pass
        
        print(f"\n⚠ Could not compress below {target_size} bytes.")
        print(f"Final size: {size} bytes")
        print("\nFor extreme compression, consider:")
        print("- Using command-line tools: pngcrush, optipng, advpng")
        print("- Reducing image dimensions")
        print("- Converting to a simpler format if lossless requirement allows")

if __name__ == "__main__":
    compress_lossless_png('download.png', 'compressed_output.png', target_size=400)