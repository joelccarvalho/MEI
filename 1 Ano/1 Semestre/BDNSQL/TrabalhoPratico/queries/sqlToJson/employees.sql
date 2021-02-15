select 
json_object (
    'employee_id' value e.employee_id, 
    'first_name' value e.first_name,
    'last_name' value e.last_name,
    'email' value e.email, 
    'phone_number' value e.phone_number,
    'hire_date' value e.hire_date,
    'salary' value e.salary,
    'commission_pct' value e.commission_pct,
    'manager_id' value e.manager_id,
    'job' value ( 
        select json_object(
              'job_id' value j.job_id,
              'job_title' value j.job_title,
              'min_salary' value j.min_salary,
              'max_salary' value j.max_salary
            )
        
        from jobs j
        where j.job_id = e.job_id
    ),
    'job_history' value ( 
        select json_arrayagg(
            json_object(
              'start_date' value jh.start_date,
              'end_date' value jh.end_date,
              'department_id' value jh.department_id,
              'jobs' value ( 
                    select json_object(
                          'job_id' value j.job_id,
                          'job_title' value j.job_title,
                          'min_salary' value j.min_salary,
                          'max_salary' value j.max_salary
                        )
                    from jobs j
                    where j.job_id = jh.job_id
                ) 
            )
        )
        from job_history jh
        where jh.employee_id = e.employee_id
    ),
    'department_id' value e.department_id
)
from employees e