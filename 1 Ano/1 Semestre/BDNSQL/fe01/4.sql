Ex4:
a)
select count(id_titulo) from titulo;

b)
select count(id_musica) from musica;

c)
select count(id_autor) from autor;

d)
select distinct count(*) from editora;

e)
select count(*) from titulo
join autor
on autor.id_autor = titulo.id_autor
where autor.nome = 'Max Changmin';

f)
select * from titulo
where dta_compra between #01/01/1970 and #31/12/1970;

g)
select autor.nome from titulo
join autor
on autor.id_autor = titulo.id_autor
where dta_compra = '01/02/2010' and preco = 12;

h)
select editora.nome from titulo
join autor
on editora.id_editora = titulo.id_editora
where dta_compra = '01/02/2010' and preco = 12;

i)
select review.dta_review, review.conteudo from review
join titulo
on titulo.id_titulo = review.id_titulo
where review.conteudo = 'oh whoa oh';

j)
select review.dta_review, review.conteudo from review
join titulo
on titulo.id_titulo = review.id_titulo
where review.conteudo = 'oh whoa oh'
order by review.dta_review desc;

k)
select * from autor
join titulo
on titulo.id_autor = autor.id_autor
where titulo.dta_compra = '04/04/1970' and titulo.preco = 20;

l)
select sum(preco) from titulo
join editora
on editora.id_editora = titulo.id_editora
where editora.nome = 'EMI';

m)
select * from titulo
where preco = 20
order by dta_compra
limit 1;

n)
select count(*) from titulo
where id_suporte = 5;

o)
select count(*) from titulo
where id_suporte = 5;

p)
select sum(preco) from titulo
join suport
on suport.id_suporte = titulo.id_suporte
where suport.nome = 'Blue-Ray';

q)
select sum(preco) from titulo
join suport
on suport.id_suporte = titulo.id_suporte
join editora
on editora.id_editora = titulo.id_editora
where editora.nome = 'EMI' and suport.nome = 'Blue-Ray';

r)

s)

t)

