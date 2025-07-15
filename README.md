# 🛠️ Django Project: [Ordering System]

A Django-based application where each company manages its own orders and products.

---

## 🚀 Features

- User Authentication
- Product Management
- Company-Based Access Control
- Order Placement
- Soft Deletion
- Custom Admin Panel

## 📚 Models and Views
### Company Model
name
### User Model
extends User Belongs to exactly one Company
Role: operator | viewer
### Product Model
- company, name, price, stock(quantity)
- created_by, created_at (immutable)
- last_updated_at
- is_active
### Order Model
- company (inferred via user)
- created_by, created_at (immutable)
- status (pending, success, failed)

### Views
- ProductListView(all roles but only active products)
- AddProduct(operator role only, company-specific, with validation, product  created by operator automatically)
- OrderListView(all roles, if action = 'created' which means the order was created by the user now so show it above the page, then show all orders anyway)
- AddOrder(operator role only and company belongs to selected product by default, - also quantity must be <= stock) using django-forms
- DeleteProduct(soft deletion, operator role only)
### Admin Panel
- Products Admin:
- # permission to add products for operator user only.
- Bulk action: mark selected products inactive
- Orders Admin:
- # permission to add orders for operator user only.
- Action: export orders as CSV with appropriate details
---

## 🧰 Tech Stack

- Python 3.13
- Django 5.2.4
- SQLite 
- CSS (for styling)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/yourproject.git
cd 

2. Create a virtual environment and activate it
open-bash:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
open-bash:
pip install -r requirements.txt

4. Apply migrations
open-bash:
python manage.py makemigrations
python manage.py migrate

5. Collect static files
open-bash:
python manage.py collectstatic

▶️ Run the Development Server
open-bash:
python manage.py runserver
Visit: http://127.0.0.1:8000

🔐 Admin Access
Log in at: http://127.0.0.1:8000/admin

📁 Directory Structure
│   PoultryTask/
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   ...
├── static/
│   └── css
│   │      └──style.css
│   └── ...
│
├── ordering/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── basse.html
│   └── ...
│
├── static/
│   └── css
│   │      └──style.css
├── └── ...
│
├── fixtures/
│   └── demo_data.json
│
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt

🧑‍💻 Author
Muhammed-Ibrahim
Email: mibrahimmangement@gmail.com
