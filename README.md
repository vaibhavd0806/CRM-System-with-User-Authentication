---

# 📘 CRM System with User Authentication (Interactive CLI App)

Welcome to your very own **CRM System**, built using **Python** and **PostgreSQL**!
This app runs in the terminal and helps you **manage customers, products, and orders** — all after a secure login or registration.

---

## 🚀 What Can You Do?

👉 **Register/Login as a User**
👉 **Insert Customer Data**
👉 **Insert Product Info**
👉 **Place Orders** (and add multiple products per order!)
👉 **Track Total Amounts Automatically**

---

## 🧰 What You’ll Need

🔸 Python (3.8 or above recommended)
🔸 PostgreSQL installed and running
🔸 psycopg2 Python library (`pip install psycopg2`)
🔸 A PostgreSQL database named `crm_system`
🔸 Required tables: `users`, `customers`, `products`, `orders`, `order_items`

---

## 🧑‍💻 Let’s Get Started!

### 1. 🔧 Setup

* Clone or download the project.
* Update your PostgreSQL username and password in `db.py`.
* Make sure the required tables exist in your database.

### 2. 🟢 Run the App

Open your terminal and run:

```bash
python auth.py
```

### 3. 🎭 Choose Your Path:

You'll see:

```
Choose option: [1] Register  [2] Login  [3] Exit
```

🆕 If you’re new, register yourself first.
🔐 Already registered? Login and start managing your CRM data.

---

## 📝 After Login – Data Insertion Time!

You’ll be taken to a new menu:

```
Choose the table you want to insert data into:
1. Insert Customer
2. Insert Product
3. Insert Order
4. Exit
```

Every option gives you step-by-step prompts to add data easily.

Example:

* While inserting an order, you’ll be asked to add items with quantity, and the system will calculate the total price for you!

---

## 💡 Highlights

* Fully interactive command-line menus
* Secure user authentication
* PostgreSQL-powered backend
* Modular code: separate files for DB, Auth, and Data

---

## 🙋 Author Info
💻**Vaibhav Dhotre**
Python | SQL | PostgreSQL Enthusiast
[Connect with me on LinkedIn](https://www.linkedin.com/in/vaibhavd08/)


---

