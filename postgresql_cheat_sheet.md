# 📘 PostgreSQL Command Line (`psql`) Cheat Sheet

## 🔌 Connect to `psql`

### Locally
```sh
psql -U postgres
```

### Inside Docker
```sh
docker exec -it postgres psql -U postgres
```

### Common Options
- `-U`: Specify the **user** (e.g., `postgres`)
- `-d`: Specify the **database** name (optional, defaults to the user name)

---

## ❓ Help & Info

### Show general help
```sql
\?
```

### Show connection info
```sql
\conninfo
```

---

## 🗂️ Database Operations

### List all databases
```sql
\l
```

### Connect to a database
```sql
\c database_name
```

---

## 📄 Table Operations

### List tables in the current schema (typically `public`)
```sql
\dt
```

### List tables in all schemas
```sql
\dt *.*
```

### Show a table’s schema (columns and types)
```sql
\d table_name
```

### List all schemas
```sql
\dn
```

### List all tables using SQL
```sql
SELECT * FROM pg_catalog.pg_tables;
```

### Create database
```sql
CREATE DATABASE my_app_db;
```
---

## 👥 Role & User Management

### List all users (roles)
```sql
\du
```

---

## 🧭 Miscellaneous

### Show current database
```sql
SELECT current_database();
```

### List all databases with sizes
```sql
SELECT pg_database.datname, pg_size_pretty(pg_database_size(pg_database.datname)) AS size
FROM pg_database;
```

---

## 🚪 Exit `psql`
```sql
\q
```