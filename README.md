# ReadView Bookstore

A classic, full-featured online bookstore web application built with Django. ReadView Bookstore allows users to browse, search, and purchase books across various categories, manage their cart, and view their order history, all within a secure and user-friendly environment.

---

## Features

- User registration, login, and account management
- Browse books by category (Action, Fictional, Comedy, Horror, Motivational, Thriller)
- Add books to cart and purchase instantly (Buy Now)
- Order confirmation and order history
- Contact and help pages
- Secure authentication and session management
- Admin interface for backend management

---

## Requirements

- Python 3.8+
- Django 3.2+

**Python packages:**
- django

> _Note: You can install all requirements using pip. See below._

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rishika03-03/Bookstore.git
   cd Bookstore
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## How It Works

- **Home Page:** Displays popular books and navigation links.
- **Categories:** Browse books by genre.
- **Authentication:** Users can register, log in, and manage their account.
- **Cart:** Add books to cart and proceed to checkout.
- **Buy Now:** Place an order directly and receive confirmation.
- **Order History:** View all previous orders (per user).
- **Contact & Help:** Reach out for support or view help topics.
- **Admin:** Django admin interface for managing books, categories, and orders.

---
