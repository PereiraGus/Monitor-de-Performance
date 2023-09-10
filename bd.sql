drop database if exists monitorBilhete;
create database monitorBilhete;
use monitorBilhete;

create user if not exists "acessoProducao" identified by "urubu100";
grant INSERT,SELECT on monitorBilhete.* to "acessoProducao";
flush privileges;

create table maquina(
    idMaquina int auto_increment primary key
);

create table dados ( 
    idMaquina int,
    idDado int,
    percCPU decimal,
    percMem decimal,
    percDisc decimal,
    dataHora datetime,
    primary key(idMaquina,idDado),
    foreign key(idMaquina) references maquina(idMaquina)
);

insert into maquina values(1),(2),(3);
select * from dados;

select idDado from dados where idMaquina = 1 order by idDado desc;