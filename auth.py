from db import get_connection
import insert_data_Manually  # Import the module

def register():
    conn = get_connection()
    cur = conn.cursor()
    username = input("Enter new username: ")
    password = input("Enter password: ")

    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, password))
        conn.commit()
        print("✅ Registered successfully.")
    except Exception as e:
        print("❌ Error during registration:", e)
    finally:
        cur.close()
        conn.close()

def login():
    conn = get_connection()
    cur = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")

    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s;", (username, password))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        print("✅ Login successful.")
        return True
    else:
        print("❌ Invalid credentials.")
        return False

if __name__ == "__main__":
    while True:
        choice = input("Choose option: [1] Register  [2] Login  [3] Exit: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                print("🔧 Redirecting to Data Insertion...")
                insert_data_Manually.insert_data()  # Call the function directly
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")
