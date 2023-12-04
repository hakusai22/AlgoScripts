# 给定一个Days表，请你编写SQL查询语句，将Days表中的每一个日期转化为"day_name, month_name day, year"格式的字符串。

SELECT
    DATE_FORMAT(day, '%W, %M %e, %Y') AS day
FROM
    days