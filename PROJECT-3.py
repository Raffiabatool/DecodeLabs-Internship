
import math
import secrets
import string
def calculate_entropy(length:int,pool_size:int) -> float:
    if pool_size<=0 or length<=0:
        return 0.0
    else:
        return length * math.log2(pool_size)
    
def generate_enterprise_password(length: int = 16) -> tuple[str, float]:

    # 1. Pool setup
    character_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pool_size = len(character_pool)

    # 2. Pick characters safely
    password_chars = [secrets.choice(character_pool) for _ in range(length)]
    
    # 3. Fast join
    password = "".join(password_chars)

    # 4. Calculate strength
    entropy = calculate_entropy(length, pool_size)

    return password, entropy
def main():
    
    print("🔒 DECODELABS - ENTERPRISE RANDOM PASSWORD GENERATOR 🔒")
    
    
    while True:
        try:
            length_input = input(
                "👉 Enter desired password length (Default 16): "
            ).strip()
            length = int(length_input) if length_input else 16

            if length < 8:
                print("⚠️ Warning: Password length under 8 is not secure!")

            
            password, entropy = generate_enterprise_password(length=length)

            
            print(f"🔑 Generated Password : {password}")
            print(f"📊 Information Entropy : {entropy:.2f} bits")

         
            if entropy < 50:
                strength = "🔴 Weak"
            elif entropy < 80:
                strength = "🟡 Moderate"
            else:
                strength = "🟢 Enterprise Strong (NIST Compliant)"

            print(f"🛡️  Security Assessment : {strength}")
            print("-" * 50 + "\n")

        except ValueError:
            print(
                "❌ Error: Invalid input! Please enter a valid integer length.\n"
            )
            continue
        
        user_choice = (
            input(
                "🔄 Do you want to generate another password? (yes/no): "
            )
            .strip()
            .lower()
        )

        if user_choice in ["no", "n"]:
            print("\n👋 Thank you for using Enterprise Password Generator!")
            break
        else:
            print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
