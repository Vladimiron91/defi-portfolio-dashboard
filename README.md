# DeFi Portfolio Dashboard

Учебный проект для отслеживания балансов в блокчейне Ethereum с использованием FastAPI и Web3.py.
---
### 🇺🇸 English
**Project Goal:** Creating a dashboard for tracking DeFi assets.  
**Technologies:** Python, FastAPI, Web3.py.  
**Progress:** Environment configured, project initialized.
-----
### 🇷🇺 Русский
**Цель проекта:** Создание дашборда для отслеживания DeFi активов.  
**Технологии:** Python, FastAPI, Web3.py.  
**Что сделано:** Настроено окружение, инициализирован проект.
---
### 🇩🇪 Deutsch
**Projektziel:** Erstellung eines Dashboards zur Verfolgung von DeFi-Assets.  
**Technologien:** Python, FastAPI, Web3.py.  
**Bisher erledigt:** Umgebung konfiguriert, Projekt initialisiert.


----------------------------------------------------------------------------------------------------
Step-by-step instructions that I have already managed to implement: 
Постепенная инструкция что я уже успел реализовать:
Schrittweise Anleitung, die ich bereits umgesetzt habe:
---
### 🇷🇺 Русский
**Что реализовано (Шаги 1-9):**
1. **Инфраструктура:** Настроено виртуальное окружение и Git-репозиторий.
2. **Backend:** Запущен сервер на FastAPI для обработки API-запросов.
3. **Безопасность:** Реализовано скрытие ключей через `.env` (python-dotenv).
4. **Web3 Интеграция:** Подключен RPC-провайдер через MetaMask Developer (Infura).
5. **Функционал:** Создан эндпоинт `/balance/{address}`, который получает живые данные из сети Ethereum (баланс ETH и номер текущего блока).
----
### 🇺🇸 English
**Implemented Features (Steps 1-9):**
1. **Infrastructure:** Virtual environment and Git repository configured.
2. **Backend:** FastAPI server launched to handle API requests.
3. **Security:** Implemented environment variables for API keys via `.env`.
4. **Web3 Integration:** Connected to Ethereum via MetaMask Developer (Infura) RPC.
5. **Features:** Created `/balance/{address}` endpoint to fetch real-time Ethereum data (ETH balance & current block number).
-----
### 🇩🇪 Deutsch
**Implementierte Funktionen (Schritte 1-9):**
1. **Infrastruktur:** Virtuelle Umgebung und Git-Repository konfiguriert.
2. **Backend:** FastAPI-Server gestartet, um API-Anfragen zu verarbeiten.
3. **Sicherheit:** Umgebungsvariablen für API-Keys über `.env` implementiert.
4. **Web3-Integration:** Verbindung zu Ethereum über MetaMask Developer (Infura) RPC hergestellt.
5. **Funktionen:** Endpunkt `/balance/{address}` erstellt, um Echtzeitdaten abzurufen (ETH-Guthaben & aktuelle Blocknummer).
