drop database if exists monitorDeDados;
create database monitorDeDados;
use monitorDeDados;

create user "acessoProducao" identified by "urubu100";
grant INSERT,SELECT on monitorDeDados.* to "acessoProducao";
flush privileges;

create table dados ( idDado int auto_increment not null primary key,
                     procFisico int,
                     procLogico int,
                     freqCPU double,
                     percUso double,
                     particoes int,
                     totalDisco double,
                     usoAtualDisco double,
                     percUsoDisco double,
                     ramTotal double,
                     usoAtualRam double,
                     percUsoRam double,
                     dataHora datetime
                   );
                   
select * from dados;