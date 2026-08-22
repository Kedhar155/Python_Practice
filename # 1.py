import urllib.request
import urllib.error
import json
import sys

# --- SETUP ---
TOKEN = "eyJyIjoiMjZCQ0U1MDI3IiwidCI6MTc4NzIzNDAxODYxNX0.E5i_K6MzwmypYjmx8ZIz-Lh9VrphKnyRf8b1ZZMln5g"  # Paste your token here! Make sure it doesn't contain the word "Bearer"
URL = "https://mic-ctf.pages.dev/api/mirror"

# We add a User-Agent to pretend we are Google Chrome so Cloudflare doesn't block us
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_guesses(addr, guesses):
    programs = []
    for g in guesses:
        # 0200[addr] 0101[guess] 050001 060003 07fd00 000000
        prog = f"0200{addr:02x}0101{g:02x}05000106000307fd00000000"
        programs.append(prog)
    
    data = json.dumps({"programs": programs}).encode("utf-8")
    req = urllib.request.Request(URL, data=data, headers=HEADERS)
    
    try:
        with urllib.request.urlopen(req) as response:
            resp_data = json.loads(response.read().decode("utf-8"))
            results = resp_data.get("results", [])
            
            for i, res in enumerate(results):
                if res == "BUDGET":
                    return guesses[i]
            return None
            
    except urllib.error.URLError as e:
        print(f"\n[!] API Error: {e}")
        if hasattr(e, 'read'):
            print(e.read().decode('utf-8'))
        sys.exit(1)

def main():
    if TOKEN == "YOUR_TOKEN_HERE":
        print("[!] Please edit the script and insert your Bearer token!")
        sys.exit(1)
        
    key = []
    print("[*] Starting extraction of MIRROR-8 vault key...")
    
    for addr in range(16):
        found = -1
        for chunk_start in range(0, 256, 16):
            guesses = list(range(chunk_start, chunk_start + 16))
            match = check_guesses(addr, guesses)
            
            if match is not None:
                found = match
                break
                
        if found == -1:
            print(f"\n[!] Failed to find byte at mem[{addr}]. Double-check your token!")
            sys.exit(1)
            
        key.append(found)
        print(f" [+] mem[{addr:02d}] = {found:02x}")
        
    key_hex = "".join(f"{b:02x}" for b in key)
    print(f"\n[*] Extracted Full Vault Key: {key_hex}")
    
    print("[*] Submitting key to the oracle...")
    data = json.dumps({"key": key_hex}).encode("utf-8")
    req = urllib.request.Request(URL, data=data, headers=HEADERS)
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            print("\n[+] Response from server:")
            print(result)
    except urllib.error.URLError as e:
        print(f"\n[!] Submission Error: {e}")
        if hasattr(e, 'read'):
            print(e.read().decode('utf-8'))

if __name__ == "__main__":
    main()