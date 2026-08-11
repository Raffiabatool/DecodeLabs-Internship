def expense_tracker():
    total_spent = 0.0
    expenses = []
    
    print("==========================================")
    print("      WELCOME TO EXPENSE TRACKER          ")
    print("==========================================")
    print("Enter your expenses one by one.")
    print("Type  'stop' when you are done.\n")
    
    # 2. Continuous Audit Loop
    while True:
        user_input = input("Enter expense amount (or 'stop'): ").strip().lower()
        
        # 3. Sentinel Value / Kill Switch Check
        if user_input in ['stop', 'exit']:
            print("\nShutting down tracker...")
            break
            
        # 4. Type Safety & Error Handling (Poka-Yoke)
        try:
            expense = float(user_input)
            
            # Defensive check for negative values
            if expense < 0:
                print("⚠️ Expense cannot be negative. Please enter a valid amount.\n")
                continue
                
            # 5. Accumulator Pattern (State update)
            total_spent += expense
            expenses.append(expense)
            print(f"✅ Added: ${expense:.2f} | Current Total: ${total_spent:.2f}\n")
            print(f"Current Expenses List: {expenses}\n")
        except ValueError:
            print("❌ Invalid Data! Please enter a valid number or 'quit'.\n")

    # 6. Final Output Stream & Display
    print("==========================================")
    print(f"  FINAL TOTAL SPENT: ${total_spent:.2f}")
    print("==========================================")

# Program Execution
if __name__ == "__main__":
    expense_tracker()