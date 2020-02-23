create database if not exists task_db;

# task 1

CREATE TABLE IF NOT EXISTS task_db.positions (
    pos_id INT NOT NULL,
    position VARCHAR(45) NOT NULL,
    PRIMARY KEY (pos_id)
);

CREATE TABLE IF NOT EXISTS task_db.employees (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    pos_id int NOT NULL,
    salary int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (pos_id) REFERENCES task_db.positions (pos_id)
);


INSERT INTO task_db.positions (pos_id, position) VALUES (300, "teamleader");
INSERT INTO task_db.positions (pos_id, position) VALUES (200, "programmer");
INSERT INTO task_db.positions (pos_id, position) VALUES (100, "tester");

INSERT INTO task_db.employees (first_name, last_name, pos_id, salary) VALUES ("Ivan", "Ivanov", 100, 20000);
INSERT INTO task_db.employees (first_name, last_name, pos_id, salary) VALUES ("Petr", "Petrov", 200, 50000);
INSERT INTO task_db.employees (first_name, last_name, pos_id, salary) VALUES ("Maria", "Minogarova", 100, 30000);
INSERT INTO task_db.employees (first_name, last_name, pos_id, salary) VALUES ("Jeff", "Bezos", 300, 100000);
INSERT INTO task_db.employees (first_name, last_name, pos_id, salary) VALUES ("Ilon", "Mask", 200, 60000);

# task 2

SELECT task_db.employees.first_name, task_db.employees.last_name, task_db.employees.salary,
       task_db.positions.position
FROM task_db.employees
INNER JOIN task_db.positions USING (pos_id)
WHERE task_db.employees.salary < 30000;

SELECT task_db.employees.first_name, task_db.employees.last_name, task_db.employees.salary,
       task_db.positions.position
FROM task_db.employees
INNER JOIN task_db.positions USING (pos_id)
WHERE task_db.employees.salary < 30000 AND task_db.positions.position = 'tester';

# task 3

CREATE TABLE IF NOT EXISTS task_db.relations (
    sup_id INT UNSIGNED NOT NULL,
    sub_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (sup_id, sub_id),
    FOREIGN KEY (sup_id) REFERENCES task_db.employees (id),
    FOREIGN KEY (sub_id) REFERENCES task_db.employees (id)
);

INSERT INTO task_db.relations (sup_id, sub_id) VALUES (4, 1);
INSERT INTO task_db.relations (sup_id, sub_id) VALUES (4, 2);
INSERT INTO task_db.relations (sup_id, sub_id) VALUES (4, 3);
INSERT INTO task_db.relations (sup_id, sub_id) VALUES (4, 5);

INSERT INTO task_db.relations (sup_id, sub_id) VALUES (2, 1);
INSERT INTO task_db.relations (sup_id, sub_id) VALUES (2, 3);

INSERT INTO task_db.relations (sup_id, sub_id) VALUES (5, 1);
INSERT INTO task_db.relations (sup_id, sub_id) VALUES (5, 2);
INSERT INTO task_db.relations (sup_id, sub_id) VALUES (5, 3);

SELECT task_db.employees.first_name, task_db.employees.last_name, task_db.employees.salary,
       task_db.positions.position
FROM task_db.employees
INNER JOIN task_db.positions USING (pos_id)
INNER JOIN task_db.relations ON task_db.employees.id = task_db.relations.sub_id
WHERE task_db.relations.sup_id = 4;

