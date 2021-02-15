select 
JSON_OBJECT (
    'department_id' VALUE d.department_id,
    'department_name' VALUE d.department_name,
    'manager_id' VALUE d.manager_id,
    'location' VALUE (
        SELECT 
            JSON_OBJECT(
              'location_id' VALUE l.location_id,
              'street_adresss' VALUE l.street_address,
              'postal_code' VALUE l.postal_code,
              'city' VALUE l.city,
              'state_province' VALUE l.state_province,
              'country' VALUE ( 
                    SELECT JSON_OBJECT(
                          'country_id' VALUE c.country_id,
                          'country_name' VALUE c.country_name,
                          'region' VALUE ( 
                                SELECT JSON_OBJECT(
                                      'region_id' VALUE r.region_id,
                                      'region_name' VALUE r.region_name
                                    )
                                from regions r
                                where r.region_id = c.region_id
                            ) 
                        )
                    from countries c
                    where c.country_id = l.country_id
                ) 
            )
        
        from locations l
        where l.location_id = d.location_id
    )
)
from departments d;