# Ví Dụ: tạo bảng SQL:

```
CREATE TABLE todos (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    completed BOOLEAN DEFAULT FALSE
);
```

# các câu lệnh truy vấn SQL:

## Insert into:

```
INSERT INTO todos (id, title, description, due_date, completed) VALUES
(1, 'Sinh viên Ptit', ' học SQL cơ bản', '2024-11-10', FALSE),
(2, 'UDU PTIT', 'học lập trình', '2024-11-06', TRUE),
(3, 'udu report', 'Hoàn thiện báo cáo tuần', '2024-11-08', FALSE),
(4, 'học cơ sở dữ liệu', 'SQL', '2024-11-05', FALSE),
(5, 'Đọc sách', 'Đọc sách SQL', '2024-11-07', TRUE);
```

## Select:

- ví dụ select các công việc chưa hoàn thành:

```
SELECT * FROM todos WHERE completed = FALSE;
```

- ví dụ select các công việc đã hoàn thành:

```
SELECT * FROM todos WHERE completed = TRUE;
```

## Update:

```
UPDATE todos
SET title = 'Đi học', description = 'chuân bị bài tập'
WHERE id = 2;
```

## Delete:

```
DELETE FROM todos WHERE id = 5;
```
