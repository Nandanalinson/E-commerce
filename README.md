# 🛒 Django eCommerce Website

This is a fully functional eCommerce website built using the Django web framework. It includes features like user registration, product display, shopping cart, order management, and more.

## 🚀 Features

* User authentication (signup/login/logout)
* Product listings with details
* Add to cart functionality
* Checkout and order placement
* Responsive design using HTML templates and includes
* Admin panel for managing products, orders, and users

## 🛠️ Tech Stack

* **Backend**: Django (Python)
* **Frontend**: HTML, CSS, Bootstrap (templating using Django templates)
* **Database**: SQLite (default for development)
* **Templates used**:

  * `index.html` (extends `blank_layout.html`)
  * `banner.html` and `content.html` included as modular blocks

## 📂 Project Structure (Simplified)

```
project/
│
├── ecommerce_app/
│   ├── templates/
│   │   ├── index.html
│   │   ├── banner.html
│   │   ├── content.html
│   │   └── blank_layout.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
│
├── static/
│   └── (CSS/JS/Images)
│
├── manage.py
└── requirements.txt
```

## ▶️ How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the server**

   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   Visit `http://127.0.0.1:8000/` in your browser.

## 📸 Screenshots

<img width="687" height="1065" alt="Screenshot 2025-07-31 213954" src="https://github.com/user-attachments/assets/e2b60469-4066-456d-8980-57c04283253b" />
<img width="2993" height="1640" alt="Screenshot 2025-07-31 213926" src="https://github.com/user-attachments/assets/34b92694-49c2-4c68-b6a2-cb57320ae8f3" />
<img width="3109" height="1572" alt="Screenshot 2025-07-31 213751" src="https://github.com/user-attachments/assets/b9186ca3-f80a-4933-8ee5-8a4f6065d462" />
<img width="2910" height="1355" alt="Screenshot 2025-07-31 213912" src="https://github.com/user-attachments/assets/f0dd64ec-5b94-4226-923c-7c68313cd490" />
<img width="2901" height="1446" alt="Screenshot 2025-07-31 213837" src="https://github.com/user-attachments/assets/f24e694f-21c9-4665-93c5-ed576519d1d6" />
<img width="3098" height="1620" alt="Screenshot 2025-07-31 213814" src="https://github.com/user-attachments/assets/fd4187be-4905-4de8-88c8-f93bf7898884" />


## 👤 Author

* **NandanaLinson** — [@nandanalinson]() https://github.com/Nandanalinson
