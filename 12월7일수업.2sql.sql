
select sbj.subject, i.addr, count(*)
	from Enroll e inner join info i on e.student = i.id 
    inner join Subjectname sbj on e.subjectname=sbj.id 
    where i.addr = '서울' group by sbj.id;

select * from ((select group_concat(sbj.subject)
	from Enroll e inner join info i on e.student = i.id 
	inner join Subjectname sbj on e.subjectname=sbj.id 
	where i.addr = '서울') as tempTable); 

select group_concat(sbj.subject, i.name order by sbj.subject, i.name asc)
	from Enroll e inner join info i on e.student = i.id 
	inner join Subjectname sbj on e.subjectname=sbj.id 
	where i.addr = '서울'; 

select group_concat(subject order by subject asc)
	from Subjectname;

--이름정렬 임시테이블을 생성해서...
create temporary table t_aaa(nm varchar(31));
insert into t_aaa(nm) select subject from Subjectname order by subject;
select group_concat(nm) from t_aaa;

Truncate TABLE t_aaa;




DELETE from Enroll where id not in (SELECT * from (select min(id) from Enroll GROUP BY student, subjectname) as tempTable);



select sbj.subject, i.addr, count(*)
	from Enroll e inner join info i on e.student = i.id 
    inner join Subjectname sbj on e.subjectname=sbj.id 
    where sbj.subject = '영어' group by i.addr;

    

select i.addr, i.gender, sbj.subject,  count(*)
	from Enroll e inner join info i on e.student = i.id 
    inner join Subjectname sbj on e.subjectname=sbj.id 
    where i.addr = '서울' group by i.gender, sbj.id;



