import csv
import codecs

def process_files():
    """
    Process three files with different encodings and sum values 
    for symbols: ˆ, Ž, Š
    """
    
    # Target symbols we're looking for
    target_symbols = {'ˆ', 'Ž', 'Š'}
    
    total_sum = 0
    details = []
    
    # Process File 1: data1.csv (CP-1252 encoding)
    print("Processing data1.csv (CP-1252 encoding)...")
    try:
        with codecs.open('data1.csv', 'r', encoding='cp1252') as file:
            reader = csv.DictReader(file)
            for row in reader:
                symbol = row['symbol'].strip()
                value = int(row['value'])
                
                if symbol in target_symbols:
                    total_sum += value
                    details.append({
                        'file': 'data1.csv',
                        'symbol': symbol,
                        'value': value
                    })
                    print(f"  Found '{symbol}' with value {value}")
    except FileNotFoundError:
        print("  ERROR: data1.csv not found!")
    except Exception as e:
        print(f"  ERROR processing data1.csv: {e}")
    
    # Process File 2: data2.csv (UTF-8 encoding)
    print("\nProcessing data2.csv (UTF-8 encoding)...")
    try:
        with codecs.open('data2.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                symbol = row['symbol'].strip()
                value = int(row['value'])
                
                if symbol in target_symbols:
                    total_sum += value
                    details.append({
                        'file': 'data2.csv',
                        'symbol': symbol,
                        'value': value
                    })
                    print(f"  Found '{symbol}' with value {value}")
    except FileNotFoundError:
        print("  ERROR: data2.csv not found!")
    except Exception as e:
        print(f"  ERROR processing data2.csv: {e}")
    
    # Process File 3: data3.txt (UTF-16 encoding, tab-separated)
    print("\nProcessing data3.txt (UTF-16 encoding, tab-separated)...")
    try:
        with codecs.open('data3.txt', 'r', encoding='utf-16') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                symbol = row['symbol'].strip()
                value = int(row['value'])
                
                if symbol in target_symbols:
                    total_sum += value
                    details.append({
                        'file': 'data3.txt',
                        'symbol': symbol,
                        'value': value
                    })
                    print(f"  Found '{symbol}' with value {value}")
    except FileNotFoundError:
        print("  ERROR: data3.txt not found!")
    except Exception as e:
        print(f"  ERROR processing data3.txt: {e}")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"\nTarget symbols: {', '.join(target_symbols)}")
    print(f"Total matches found: {len(details)}")
    print(f"\n{'File':<15} {'Symbol':<10} {'Value':<10}")
    print("-" * 35)
    
    for detail in details:
        print(f"{detail['file']:<15} {detail['symbol']:<10} {detail['value']:<10}")
    
    print("\n" + "="*60)
    print(f"FINAL SUM: {total_sum}")
    print("="*60)
    
    return total_sum

if __name__ == "__main__":
    print("Multi-Encoding File Processor")
    print("="*60)
    print("Looking for symbols: ˆ (circumflex), Ž (Z-caron), Š (S-caron)")
    print("="*60 + "\n")
    
    result = process_files()
    
    print(f"\n✓ Answer: {result}")