insert into grade(enroll, midterm, finalterm) select id, ceil(rand()*100), ceil(rand()*100) from Enroll order by id asc limit 9999;

update grade 
	SET midterm = midterm + 30 + ceil(rand()*10) where midterm between 0 and 30;
update grade 
    SET finalterm = finalterm + 30 + ceil(rand()*10) where finalterm between 0 and 30;
		    
            
select i.name, sbj.subject, g.midterm, g.finalterm, g.midterm + g.finalterm as total, (g.midterm + g.finalterm)/2  as avg,
	(CASE WHEN (g.midterm + g.finalterm)/2 >= 90 THEN 'A'
		WHEN (g.midterm + g.finalterm)/2 >= 80 and (g.midterm + g.finalterm)/2 < 90 THEN 'B' 
        WHEN (g.midterm + g.finalterm)/2 >= 70 and (g.midterm + g.finalterm)/2 < 80 THEN 'C'
        WHEN (g.midterm + g.finalterm)/2 >= 60 and (g.midterm + g.finalterm)/2 < 70 THEN 'D'
        ELSE 'F'
        END) as '학점'
	from Enroll e inner join info i on e.student = i.id 
    inner join Subjectname sbj on e.subjectname=sbj.id 
    inner join grade g on e.id=g.id;
    

select sbj.subject, (g.midterm + g.finalterm)/2  as avg, MAX((g.midterm + g.finalterm)/2) 
	from Enroll e inner join info i on e.student = i.id 
    inner join Subjectname sbj on e.subjectname=sbj.id 
    inner join grade g on e.id=g.id;
	

select e.subjectname, AVG((g.midterm + g.finalterm)/2) as '과목당 평균', MAX((g.midterm + g.finalterm)/2) , count(*) 
	from grade g inner join Enroll e on e.id = g.id 
where g.id > 0 group by e.subjectname;
    
select e.id, MAX((g.midterm + g.finalterm)/2)
	from grade g inner join Enroll e on e.id = g.id 
	where g.id > 0 group by e.subjectname 


    




select count(*) from grade;
select * from grade;
select * from Enroll;
