(https://roadmap.sh/projects/expense-tracker-api)


##Features:
- CRUD operations for the api (GET, POST, PUT, PATCH, DELETE)
- JWT authentication system
- Custom categories and date filtering

---

##Authentication:
- Register: POST /users/register/ <pre> { "username": "user1", "password": "mypassword"} </pre>
- Login: POST /users/login/ <pre> {"username": "user1", "password": "mypassword"} </pre>
- Refresh: POST /users/refresh/ <pre> {"usernaame": "user1", "password": "mypassword", "refresh": "**the refresh token you got when you logged in**"} </pre>
- Delete an user: once logged in in the user you want to delete: DELETE /users/delete/   (**this will also delete all the expenses linked to that user**)

#CRUD operations:
- **Create** a new expense: POST /api/expenses/ <pre> {"title": "eggs", "category": "Groceries", "amount": "13", "date": "(*optional, default = current date*)", "user": *user primary key*} </pre>
- **Read** all the expenses: GET /api/expenses
- **Update** an expense: PATCH /api/expense/*expense id*/ and then adding in the body of the request the values you want to modify <pre> {"amount": 18} </pre>
- **Delete** an expense: DELETE /api/expenses/*expense id*/

##Filtering
- By category: add a param with 'Category' and the category you want to filter by ("Groceries", "Leisure", "Electronics", "Utilities", "Clothing", "Health", "Others"): GET /api/expenses?category=Groceries

- By date: add a param with "date" and then the date you want to go to, the request should be like this: GET /api/expenses?date=2025-05-27

- By custom date range: add two params, one with "start_date" and then the starting date and the other with "end_date" and then the ending date: GET /api/expenses?end_date=2025-05-30&start_date=2025-05-10

- By a preset selection: add a param "date_preset" and then one of these three options ("past_week", "past_month", "past_3_months"): GET /api/expenses?date_preset=past_week
