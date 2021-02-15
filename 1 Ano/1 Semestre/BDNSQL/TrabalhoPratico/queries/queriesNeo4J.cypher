// QUERIES Neo4J

// 1 -> Retorna as Cidades com departamentos
match (d:Department) -[r:SEDIADO_EM]-> (l:Location)  
return DISTINCT l.city AS City, count(r) as Number

// 2 ->  Retorna o numero de trabalhos antigos de cada funcionário
match (e:Employee) -[r:TRABALHOU_EM]-> (a:Job_History)  
return e.firstName as Name, count(r) as NumberJobs

// 3 -> Consulta geral da BD
macth (n)  
return n

// 4 -> Empregados que iniciam com a letra J
match (e:Employee)  
WHERE e.firstName =~'J.*'  
return e

// 5 -> Retorna o Presidente 
match (n:Employee) -[:TRABALHA_EM]-> (:Job{jobTitle:"President"})  
return n.firstName as Name, n.hireDate as HireDate, n.salary as Salary  

// 6 -> Retorna top 5 dos salários mais altos por funcionarios
match (e:Employee)  
return e.firstName as Name, toInteger(e.salary) as Salary  
order by toInteger(e.salary) desc  
limit 5;

// 7 -> Retorna uma lista de departamentos por codigo postal e por país
MATCH (d:Department) -[:SEDIADO_EM]->(l:Location) -[:LOCALIZADO_EM]-> (c:Country)  
RETURN d.nameDepartmant AS NameDepartment, toInteger(l.postalCode) AS PostalCode, c.nameCountry AS Country  
order by NameDepartment

// 8 -> Top salário médio por departamento e cidade
MATCH (j:Job) <-[:TRABALHA_EM]-(E:Employee)-[:PERTENCE_AO]->(d:Department)-[:SEDIADO_EM]->(l:Location)
RETURN j.jobTitle AS Job, l.city AS City, d.nameDepartmant AS Department, 
	   (toInteger(j.maxSalary) + toInteger(j.minSalary))/2 AS Salary
order BY Salary DESC