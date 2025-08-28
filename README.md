# Beehive Backend
Backend for **Beehive**, a real-time personal expense tracking system built with **FastAPI** (SQLAlchemy, RESTful APIs), **Python**, and **SQLite**.  
The idea behind Beehive is to replace the traditional monthly budget notebook and allow users (starting with myself) to track expenses efficiently.

## Project Overview
Beehive is designed to help users:
- Track daily expenses in real-time  
- Categorize spending for better insights  
- Manage financial data efficiently  
This repository contains the **backend code**, including RESTful APIs and business logic. The frontend is under active development.

## Tech Stack
- **Backend Framework:** FastAPI  
- **Database:** SQLite  
- **Language:** Python 3.x  
- **ORM / Database Layer:** SQLAlchemy 

## API Endpoints
1. GET /expenses/  - List all expenses
<img width="1802" height="969" alt="beehive-get" src="https://github.com/user-attachments/assets/098b2ba5-1846-4dc9-a36d-88a031d4b948" />

2. POST /expenses/  - Add a new expense
<img width="1790" height="880" alt="beehive-post" src="https://github.com/user-attachments/assets/dfd6f720-fd4a-46c2-a30c-de4842964476" />

3. PUT /expenses/{expense_id}  - Update an exisitng expense
<img width="1793" height="786" alt="beehive-edit" src="https://github.com/user-attachments/assets/8aa7cad6-ec07-4bee-889e-9f7997c6ebee" />

4. DELETE /expenses/{expense_id}  - Delete an expense
<img width="1798" height="778" alt="beehive-delete" src="https://github.com/user-attachments/assets/49b223ac-7996-4f82-a2c2-034493d593a0" />

5. GET /summary/{year}/{month}  - Get monthly Summary
<img width="1785" height="962" alt="beehive-monthly-summary" src="https://github.com/user-attachments/assets/0f4e1248-9a11-4bbe-bae6-7f6bc69e34b0" />

## Features
- CRUD operations for expenses  
- RESTful API endpoints for managing expenses  
- Input validation and schema management with Pydantic  
- Modular structure: routes, models, schemas, CRUD logic, and utilities  


