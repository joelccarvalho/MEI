-- Query 1 - Cidades com departamentos
select distinct city from departments
join locations
on locations.location_id = departments.location_id;

-- Query 2 - Empregados com mudanças de empregos
select employees.first_name, count(*) as ocorrencias from job_history
join employees
on employees.employee_id = job_history.employee_id
group by employees.first_name
order by ocorrencias desc;

-- Query 3 - Conteudo geral da BD
select *  from employees 
join departments on departments.department_id = employees.department_id 
join job_history on job_history.job_id = employees.job_id 
join jobs on jobs.job_id = employees.job_id 
join locations on locations.location_id = departments.location_id 
join countries on countries.country_id = locations.country_id 
join regions on regions.region_id = countries.region_id;

-- Query 4 - Empregados que iniciam com a letra J
select * from employees
where first_name like 'J%';

-- Query 5 - Listar os presidentes
select employees.first_name as "Name", employees.hire_date as "HireDate", employees.salary as "Salary" from employees
join jobs
on jobs.job_id = employees.job_id 
where jobs.job_title = 'President';

-- Query 6 - Top 5 bem pagos
select * from employees
order by salary desc
fetch first 5 rows only;

-- Query 7 - Nome dos departamentos por País e Código Postal
select distinct d.department_name, l.postal_code, c.country_name
from departments d
        inner join locations l on l.location_id = d.location_id
        inner join countries c ON c.country_id = l.country_id
order by department_name;

-- Query 8 - Salário Médio por Departemento e Cidade
select distinct d.department_name, l.city ,((j.max_salary + j.min_salary)/2) as salario_medio
from departments d
        inner join employees e on e.department_id = d.department_id
        inner join jobs j on j.job_id = e.job_id 
        inner join locations l on l.location_id = d.location_id
order by salario_medio desc;