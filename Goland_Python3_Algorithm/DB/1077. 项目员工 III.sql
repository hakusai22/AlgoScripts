with t as
         (select a.project_id,
                 a.employee_id,
                 b.experience_years
          from project a
                   join employee b
                        using (employee_id))

select project_id, employee_id
from (select project_id,
             employee_id,
             dense_rank() over (partition by project_id order by experience_years desc) as rnk
      from t) tmp
where rnk = 1
