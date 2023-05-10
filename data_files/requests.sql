CREATE TABLE IF NOT EXISTS employers (
                    employer_id INT PRIMARY KEY,
                    company_name VARCHAR(50) UNIQUE NOT NULL);


CREATE TABLE IF NOT EXISTS vacancies (
                    vacancy_id INT PRIMARY KEY,
                    title VARCHAR(255),
                    employer_id INT REFERENCES employers(employer_id) NOT NULL,
                    expierence VARCHAR(255),
                    employment VARCHAR(255),
                    description VARCHAR(255),
                    salary INT,
                    currency VARCHAR(10),
                    url VARCHAR(30)
                    );

--получает список всех компаний и количество вакансий у каждой компании
SELECT company_name, COUNT(vacancy_id) FROM employers
                    INNER JOIN vacancies using(employer_id)
                    GROUP BY company_name;

--получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
SELECT company_name, title, salary, url
                    FROM vacancies
                    INNER JOIN employers USING(employer_id);

--получает среднюю зарплату по вакансиям
SELECT AVG(salary) FROM vacancies;

--получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);

--получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
SELECT * FROM vacancies WHERE title like '%python%'
