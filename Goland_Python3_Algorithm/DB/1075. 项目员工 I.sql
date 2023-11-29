select project_id,
       ROUND(avg(experience_years), 2) as average_years
from Project a
         join Employee b using (employee_id)
group by project_id