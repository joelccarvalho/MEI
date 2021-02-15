select 
JSON_OBJECT (
    'employee_id' VALUE e.employee_id, 
    'first_name' VALUE e.first_name,
    'last_name' VALUE e.last_name,
    'email' VALUE e.email, 
    'phone_number' VALUE e.phone_number,
    'hire_date' VALUE e.hire_date,
    'salary' VALUE e.salary,
    'commission_pct' VALUE e.commission_pct,
    'manager_id' VALUE e.manager_id,
    'job' VALUE ( 
        SELECT JSON_OBJECT(
              'job_id' VALUE j.job_id,
              'job_title' VALUE j.job_title,
              'min_salary' VALUE j.min_salary,
              'max_salary' VALUE j.max_salary
            )
        
        from jobs j
        where j.job_id = e.job_id
    ),
    'job_history' VALUE ( 
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT(
              'start_date' VALUE jh.start_date,
              'end_date' VALUE jh.end_date,
              'department_id' VALUE jh.department_id,
              'jobs' VALUE ( 
                    SELECT JSON_OBJECT(
                          'job_id' VALUE j.job_id,
                          'job_title' VALUE j.job_title,
                          'min_salary' VALUE j.min_salary,
                          'max_salary' VALUE j.max_salary
                        )
                    
                    from jobs j
                    where j.job_id = jh.job_id
                ) 
            )
        )
        from job_history jh
        where jh.employee_id = e.employee_id
    ),
    'department_id' VALUE e.department_id
)
from employees e