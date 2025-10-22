import re
from datetime import datetime

def slugify(text):
    """
    Mengubah string menjadi format 'slug' yang ramah URL.
    Contoh: "Hello World!" -> "hello-world"
    """
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text) # Hapus karakter non-alphanumeric
    text = re.sub(r'[\s_]+', '-', text)     # Ganti spasi/underscore dengan dash
    text = re.sub(r'^-+|-+$', '', text)     # Hapus dash di awal/akhir
    return text

def format_timestamp(timestamp, fmt="%Y-%m-%d %H:%M:%S"):
    """
    Mengubah timestamp (float atau int) menjadi string tanggal/waktu yang diformat.
    """
    if isinstance(timestamp, (int, float)):
        dt_object = datetime.fromtimestamp(timestamp)
        return dt_object.strftime(fmt)
    return None

if __name__ == "__main__":
    print("--- Contoh Penggunaan Utilitas ---")
    
    # Contoh slugify
    print(f"Slugify 'Proyek Baru Saya': {slugify('Proyek Baru Saya')}")
    print(f"Slugify 'Artikel Hebat #1': {slugify('Artikel Hebat #1')}")
    
    # Contoh format_timestamp
    current_time_stamp = datetime.now().timestamp()
    print(f"Format timestamp sekarang: {format_timestamp(current_time_stamp)}")
    print(f"Format timestamp kustom: {format_timestamp(current_time_stamp, '%d/%m/%Y')}")
    
    print("\nUtilitas ini dibuat untuk membantu pengembangan proyek-proyek kecil.")
