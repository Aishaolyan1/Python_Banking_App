#Python Banking Project
# 💳 Online Banking System - Python Project

Welcome to my **Beginner Banking System Project**!  
This is a simple command-line banking application written in **Python**, designed as a practice project for learning object-oriented programming (OOP), file handling, and testing using `unittest`. 🚀

You can create a bank account, login, deposit, withdraw, transfer money, and even get charged for overdrafts—just like real banking, but in a fun and beginner-friendly way! 😄

---

## 📋 App Functionality (User Stories)

| Feature                                         | Description                                                                 |
|------------------------------------------------|-----------------------------------------------------------------------------|
| ✅ Create Account                               | New users can register with ID, name, password, and initial balances.       |
| ✅ Login                                        | Secure login using account ID and password.                                |
| ✅ View Balance                                 | Display balances for Checking and Savings accounts.                         |
| ✅ Deposit                                      | Add money to Checking or Savings accounts.                                 |
| ✅ Withdraw                                     | Withdraw money with limits and overdraft fee applied if needed.            |
| ✅ Transfer Money (Same Customer)               | Move money between Checking and Savings accounts.                          |
| ✅ Transfer Money (Different Customer)          | Transfer to another customer's account using their ID.                     |
| ✅ Overdraft Fee                                | If balance goes below 0, $35 fee is charged.                               |
| ✅ Account Deactivation                         | Account deactivates after 2 overdrafts.                                    |
| ✅ Reactivation on Positive Balance             | Account reactivates if balance becomes positive.                           |
| ✅ Transaction History                          | All transactions saved in `transactions.csv` with timestamp and type.      |
| ✅ Transaction Filtering                        | View a single transaction or filter transactions by date/type.             |

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **CSV File Handling**
- **Object-Oriented Programming (OOP)**
- **Unit Testing with `unittest`**
- **Command Line Interface (CLI)**

---

## ❄️ Icebox Features (Future Ideas)

✨ Some cool features I'd love to add later:
- Password encryption (instead of plain text).
- Admin dashboard to view all customer data.
- Export transaction summary to PDF.
- Monthly interest calculator for savings account.
- GUI version using Tkinter or PyQt.
- Email notifications for large withdrawals or overdrafts.
- ATM simulation with card authentication.

---

## 🤯 Challenges Faced

- Designing the right structure for classes and keeping the logic clean.
- Handling overdraft logic while keeping the account rules simple.
- Learning how to write **unit tests** and apply **TDD**.
- Using CSV files to store data persistently.
- Keeping the code **beginner-friendly** while still covering **real banking logic**.

---

## 📚 Key Learning Takeaways

✅ Object-Oriented Design  
✅ Static methods and how to use them properly  
✅ Writing unit tests using `unittest`  
✅ File reading/writing with CSV  
✅ User-friendly CLI interactions  
✅ Error handling and edge case scenarios  

---

## 🔗 Resources I Used

- 📺 [YouTube: Simple Banking System in Python](https://youtu.be/E6NO0rgFub4?si=iL47NePr5VrqpboS)  
- 📚 [W3Schools - Python Tutorials](https://www.w3schools.com/)  
- 🛠️ [Pretty Print Table Library](https://pypi.org/project/prettytable/)  
- 🧠 [Static Methods in Python - DigitalOcean](https://www.digitalocean.com/community/tutorials/python-static-method)

---

Thanks for checking out my project 💖  
Feel free to fork, modify, or just get inspired!

> _“Code is like humor. When you have to explain it, it’s bad.” – Cory House_
