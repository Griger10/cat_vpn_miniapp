# 🐾 Кот VPN Бот

> Мини-приложение для Telegram, предоставляющее удобный интерфейс для ручной выдачи VPN-ключей.

---

## 📦 Технологический стек
- **Backend:** Python · FastAPI · Dishka · aiogram · SQLAlchemy · PostgreSQL · ruff 
- **Frontend:** JavaScript · Vue 3 · axios  
- **Инфраструктура:** Docker · пакетный менеджер `uv`

---

## 🚀 Запуск проекта

### 1. Настройка окружения
Перед запуском необходимо создать и заполнить файлы окружения по образцу:
```bash
# Backend
cp .env.example .env

# Frontend
cd src/frontend
cp .env.example .env