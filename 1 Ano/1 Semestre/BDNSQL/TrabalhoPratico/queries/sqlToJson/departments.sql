select 
json_object (
    'department_id' value d.department_id,
    'department_name' value d.department_name,
    'manager_id' value d.manager_id,
    'location' value (
        select 
            json_object(
              'location_id' value l.location_id,
              'street_adresss' value l.street_address,
              'postal_code' value l.postal_code,
              'city' value l.city,
              'state_province' value l.state_province,
              'country' value ( 
                    select json_object(
                          'country_id' value c.country_id,
                          'country_name' value c.country_name,
                          'region' value ( 
                                select json_object(
                                      'region_id' value r.region_id,
                                      'region_name' value r.region_name
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