
CREATE TABLE autor(
	"id_autor" Number(3, 0) NOT NULL ENABLE,
	"nome" VARCHAR2(200 byte) NOT NULL ENABLE,
	CONSTRAINT "autor_PK" PRIMARY KEY ("id_autor")
);


CREATE TABLE editora(
	"id_editora" Number(3, 0) NOT NULL ENABLE,
	"nome" VARCHAR2(200 byte) NOT NULL ENABLE,
	CONSTRAINT "editora_PK" PRIMARY KEY ("id_editora")
);


CREATE TABLE genero (
	"id_genero" Number(3, 0) NOT NULL ENABLE,
	"nome" VARCHAR2(200 byte) NOT NULL ENABLE,
	CONSTRAINT "genero_PK" PRIMARY KEY ("id_genero")
);


CREATE TABLE suporte (
	"id_suporte" Number(3, 0) NOT NULL ENABLE,
	"nome" VARCHAR2(200 byte) NOT NULL ENABLE,
	CONSTRAINT "suporte_PK" PRIMARY KEY ("id_suporte")
);


CREATE TABLE titulo (	
	"id_titulo" NUMBER(5,0) NOT NULL ENABLE, 
	"titulo" VARCHAR2(200 BYTE), 
	"preco" NUMBER, 
	"dta_compra" DATE, 
	"id_editora" NUMBER(3,0), 
	"id_suporte" NUMBER(3,0), 
	"id_genero" NUMBER(3,0), 
	"id_autor" NUMBER(3,0), 
	 CONSTRAINT "TITULO_PK" PRIMARY KEY ("id_titulo"),
	CONSTRAINT "TITULO_FK1" FOREIGN KEY ("id_editora")
	  REFERENCES "MUSIC"."EDITORA" ("id_editora") ENABLE, 
	 CONSTRAINT "TITULO_FK2" FOREIGN KEY ("id_suporte")
	  REFERENCES "MUSIC"."SUPORTE" ("id_suporte") ENABLE, 
	 CONSTRAINT "TITULO_FK3" FOREIGN KEY ("id_genero")
	  REFERENCES "MUSIC"."GENERO" ("id_genero") ENABLE, 
	 CONSTRAINT "TITULO_FK4" FOREIGN KEY ("id_autor")
	  REFERENCES "MUSIC"."AUTOR" ("id_autor") ENABLE
);


CREATE TABLE musica (	
	"id_musica" NUMBER(5,0) NOT NULL ENABLE, 
	"nome" VARCHAR2(20 BYTE) NOT NULL ENABLE, 
	"id_autor" NUMBER(3,0) NOT NULL ENABLE, 
	"id_titulo" NUMBER(5,0) NOT NULL ENABLE, 
	 CONSTRAINT "MUSICA_PK" PRIMARY KEY ("id_musica"),
	CONSTRAINT "MUSICA_FK1" FOREIGN KEY ("id_autor")
	  REFERENCES "MUSIC"."AUTOR" ("id_autor") ENABLE, 
	 CONSTRAINT "MUSICA_FK2" FOREIGN KEY ("id_titulo")
	  REFERENCES "MUSIC"."TITULO" ("id_titulo") ENABLE
);


CREATE TABLE review (	
	"id_review" NUMBER(5,0) NOT NULL ENABLE, 
	"id_titulo" NUMBER(5,0) NOT NULL ENABLE, 
	"dta_review" DATE NOT NULL ENABLE, 
	"conteudo" VARCHAR2(500 BYTE) NOT NULL ENABLE, 
	 CONSTRAINT "REVIEW_PK" PRIMARY KEY ("id_review"),
	CONSTRAINT "REVIEW_FK1" FOREIGN KEY ("id_titulo")
	  REFERENCES "MUSIC"."TITULO" ("id_titulo") ENABLE
);






