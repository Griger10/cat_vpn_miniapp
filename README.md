# 🐾 Кот VPN Бот

> Мини-приложение для Telegram, предоставляющее удобный интерфейс для ручной выдачи VPN-ключей.

---

## 📦 Технологический стек
- **Backend:** Python · FastAPI · Dishka · aiogram · SQLAlchemy · PostgreSQL · ruff · taskiq 
- **Frontend:** JavaScript · Vue 3 · axios  
- **Инфраструктура:** Docker · пакетный менеджер `uv`
- **Мониторинг:** Prometheus · Grafana  

---

## 🚀 Запуск проекта

### 1. Настройка окружения
Перед запуском необходимо создать и заполнить файлы окружения по образцу:
```bash
# Project
cp .env.example .env
```
### 2. Запустить проект в Docker
```bash
# Docker
docker compose up -d --build
```
### 3. Выполнить миграции alembic
```bash
# Alembic
docker compose exec cat_vpn_miniapp alembic upgrade head
```