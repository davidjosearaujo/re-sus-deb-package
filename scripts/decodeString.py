import sys

def decode_string(encoded_str, key):
    decoded_str = ""
    for char in encoded_str:
        decoded_str += chr(ord(char) ^ key)
    return decoded_str

def main(encoded_str, key):
    decoded_str = decode_string(encoded_str, key)
    print("Decoded String:", decoded_str)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <encoded_string> <key>")
        sys.exit(1)
    
    encoded_str = sys.argv[1]
    key = int(sys.argv[2], 0)
    main(encoded_str, key)