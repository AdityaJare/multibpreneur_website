# Multibpreneur Website

A comprehensive business and blog platform built with Django.

## Features

- Blog system with categories and tags
- Business inquiry system with file upload
- Contact form with email notifications
- RESTful API endpoints
- Admin dashboard
- Responsive design

## Prerequisites

- Python 3.12+
- Django 5.2+
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd multibpreneur_website
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/

## API Endpoints

- `/api/posts/` - Blog posts
- `/api/categories/` - Blog categories
- `/api/tags/` - Blog tags
- `/api/business-inquiries/` - Business inquiries
- `/api/contact-inquiries/` - Contact form submissions

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
