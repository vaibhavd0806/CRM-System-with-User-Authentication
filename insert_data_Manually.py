from db import get_connection


def insert_data():
    def insert_customer_manual():
        conn = get_connection()
        cur = conn.cursor()
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        join_date = input("Enter join date (YYYY-MM-DD): ")

        cur.execute("""
            INSERT INTO customers (name, phone, email, join_date)
            VALUES (%s, %s, %s, %s);
        """, (name, phone, email, join_date))

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Customer inserted successfully.")

    def insert_product_manual():
        conn = get_connection()
        cur = conn.cursor()
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))

        cur.execute("""
            INSERT INTO products (name, description, price)
            VALUES (%s, %s, %s);
        """, (name, description, price))

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Product inserted successfully.")

    def insert_order_manual():
        conn = get_connection()
        cur = conn.cursor()
        customer_id = int(input("Enter customer ID (from the customers table): "))
        order_date = input("Enter order date (YYYY-MM-DD): ")

        total_amount = 0  # Initialize total_amount here

        cur.execute("""
            INSERT INTO orders (customer_id, order_date, total_amount)
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (customer_id, order_date, total_amount))

        order_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Order inserted with ID: {order_id}")
        return order_id

    def insert_order_items_manual(order_id):
        conn = get_connection()
        cur = conn.cursor()

        total_amount = 0  # Initialize total_amount here as well

        while True:
            product_id = int(input("Enter product ID (from the products table): "))
            quantity = int(input("Enter quantity: "))

            cur.execute("""
                SELECT price FROM products WHERE id = %s;
            """, (product_id,))
            result = cur.fetchone()

            if result is None:
                print("❌ Invalid product ID.")
                continue  # Ask for the product ID again if invalid

            price = result[0]
            item_total = quantity * price
            total_amount += item_total  # Add to the total amount

            cur.execute("""
                INSERT INTO order_items (order_id, product_id, quantity, price)
                VALUES (%s, %s, %s, %s);
            """, (order_id, product_id, quantity, price))

            conn.commit()
            print(f"✅ Order item added. Item total: ₹{item_total:.2f}")

            add_more = input("Do you want to add more items? (y/n): ")
            if add_more.lower() != 'y':
                break

        # After inserting all items, update the total amount in the orders table
        cur.execute("""
            UPDATE orders
            SET total_amount = %s
            WHERE id = %s;
        """, (total_amount, order_id))

        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Total amount for order {order_id} updated: ₹{total_amount:.2f}")

    print("🔧 Manual Data Insertion")

    while True:
        print("\nChoose the table you want to insert data into:")
        print("1. Insert Customer")
        print("2. Insert Product")
        print("3. Insert Order")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            insert_customer_manual()
        elif choice == '2':
            insert_product_manual()
        elif choice == '3':
            order_id = insert_order_manual()
            insert_order_items_manual(order_id)
        elif choice == '4':
            print("👋 Exiting the script.")
            break
        else:
            print("❌ Invalid choice, please choose a valid option.")
