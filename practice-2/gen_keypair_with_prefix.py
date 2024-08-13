from multiprocessing import Pool, cpu_count
from solders.keypair import Keypair
from datetime import datetime

prefix = "elva".lower()

def generate_key_with_prefix(_):
    while True:
        keypair = Keypair()
        public_key = str(keypair.pubkey())
        public_key_lower = public_key.lower()
        if public_key_lower.startswith(prefix):
            secret_key = keypair.secret().hex()
            return (public_key, secret_key)

if __name__ == "__main__":
    start_time = datetime.now()
    print(f"🔄 Operation started at: {start_time}")

    with Pool(cpu_count()) as pool:
        result = pool.map(generate_key_with_prefix, [None] * cpu_count())
        for public_key, secret_key in result:
            if public_key:
                end_time = datetime.now()
                print(f"The public key is: {public_key}")
                print(f"The secret key is: {secret_key}")
                print(f"✅ Finished at: {end_time}")
                print(f"⏱️ Time taken: {end_time - start_time}")
                break
