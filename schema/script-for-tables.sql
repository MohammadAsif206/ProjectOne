
-- Project one schema ---

drop table if exists employee;
create table employee (
	employee_id int primary key generated always as identity,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(50)
);

insert into employee values (default, 'Mohammad', 'Asif', 'mohammad.asif@hotmail.com');
insert into employee values (default, 'Erick', 'Jonson', 'erick.jonson@hotmail.com');
insert into employee values (default, 'Adams', 'Smith', 'adams.smith@hotmail.com');
insert into employee values (default, 'Rashid', 'Jan', 'rashid.jan@hotmail.com');
insert into employee values (default, 'Maria', 'Carlos', 'maria.carlos@hotmail.com');
insert into employee values (default, 'Barbara', 'Brown', 'barbar.brown@hotmail.com');
insert into employee values (default, 'Mark', 'Taylor', 'mark.taylor@hotmail.com');
insert into employee values (default, 'William', 'Chan', 'william.chan@hotmail.com');
insert into employee values (default, 'Kieron', 'Chew','kieron.chew@hotmail.com');

update employee set first_name ='Tom', last_name ='Hill', email='tom.hill@hotmail.com' where employee_id = 1;

--table manager

drop table if exists manager;
create table manager (
	manager_id int primary key generated always as identity,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(50)
);

insert into manager values (default, 'Peanut', 'Butter', 'peanut.butter@gmail.com');
insert into manager values (default, 'Olive', 'Oil', 'olive.oil@gmail.com');
insert into manager values (default, 'Car', 'Wash', 'car.wash@hotmail.com');

-- end manager table

-- table request --

drop table if exists erequest;
create table erequest(
	erequest_id int primary key generated always as identity not null,
	amount int ,
	reason varchar(500),
	rstatus varchar (50),
	message varchar(500),
	employee_id int,
	foreign key(employee_id)
		references employee(employee_id)
		on update cascade	
		on delete cascade
);
insert into erequest values(default, 5500, 'office', 'pending', 'nc', 
	(select employee_id from employee where employee_id = 3))
	
insert into erequest (amount, reason, rstatus,message ,employee_id)
         values(1100,'relocation', 'pending', 'nc', 3);
 
 -- end of table request --


select * from  erequest;
delete from erequest where erequest_id > 10;
select * from  employee 
select * from manager
delete from  employee where employee_id > 15;

select round(avg(amount), 2) avg_expens from erequest; 
select sum(amount) from erequest where employee_id =2;

select * from employee as e where e.first_name ='Mohammad' and e.email ='mohammad.asif@hotmail.com'

update erequest set rstatus = 'approved' where erequest_id = 56;

update erequest set amount = 50, reason ='none', rstatus ='approved' where erequest_id =1

select sum(amount) sum_of_employee_expense from erequest on er where er.employee_id = 1
left join 
select * from employee ep where ep.employee_id = er.employee_id 

alter table erequest add column message varchar(500)


-- for statistics page --
select employee.employee_id , employee.first_name , SUM(erequest.amount) as tex_pemp,
  (select sum(erequest.amount) from erequest)as total_sum, 
  (select count(erequest.erequest_id) from erequest where erequest.employee_id = employee.employee_id ) as total_request,
  (select count(erequest_id) from erequest) as total_request
from employee
inner join erequest
on employee.employee_id = erequest.employee_id 
group by employee.employee_id, employee.first_name 

-- end of statistics script ---



update erequest set employee_id = message , message = employee_id 

delete from erequest where erequest_id > 11












