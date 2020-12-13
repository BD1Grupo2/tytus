
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftMAYORIGUALQUEMENORIGUALQUEMAYORQUEMENORQUEleftSIGNO_MASSIGNO_MENOSleftSIGNO_PORSIGNO_DIVISIONleftSIGNO_POTENCIASIGNO_MODULOACTION ADD ALL ALTER AND ANY AS ASC AVG BETWEEN BIGINT BOOLEAN BY CADENA CASCADE CASE CHAR CHARACTER CHECK COLUMN COMA CONSTRAINT CORCHETEABRE CORCHETECIERRE COUNT CREATE DATABASE DATABASES DATE DAY DECIMAL DEFAULT DELETE DESC DISTINCT DOBLE DOBLE_DOSPUNTOS DROP ELSE END ENUM EXCEPT EXIST EXISTS FALSE FECHA_HORA FIRST FOREIGN FROM FULL GREATEST GROUP HAVING HOUR ID IF ILIKE IN INNER INSERT INTEGER INTERSECT INTERVAL INTO IS ISNULL JOIN KEY LAST LEAST LEFT LIKE LIMIT LLAVEABRE LLAVECIERRE MAX MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MIN MINUTE MODE MONEY MONTH NATURAL NO NOT NOTNULL NULL NULLS NUMERIC NUMERO NUM_DECIMAL OFFSET ON OR ORDER OUTER OWNER PARABRE PARCIERRE PRECISION PRIMARY PUNTO PUNTO_COMA REAL REFERENCES RENAME REPLACE RETURNING RIGTH SECOND SELECT SET SHOW SIGNO_DIVISION SIGNO_IGUAL SIGNO_MAS SIGNO_MENOS SIGNO_MODULO SIGNO_POR SIGNO_POTENCIA SIMILAR SMALLINT SOME SUBSTRING SUM SYMMETRIC TABLE TEXT THEN TIME TIMESTAMP TO TRUE TYPE UNION UNIQUE UNKNOWN UPDATE USE USING VALUES VARCHAR VARYING WHEN WHERE YEARinicio : instrucciones instrucciones : instrucciones instruccion \n                     | instruccion instruccion : ins_use\n                   | ins_show\n                   | ins_alter\n                   | ins_drop\n                   | ins_create\n                   | ins_insert\n                   | ins_selectins_use : USE IDins_show : SHOW DATABASESins_create : CREATE tipo_createtipo_create : ins_replace DATABASE if_exist ID create_opciones puntocoma\n                   | TABLE ID PARABRE definicion_columna PARCIERRE PUNTO_COMAdefinicion_columna : definicion_columna COMA columna \n                          | columna columna : ID tipo_dato definicion_valor_defecto ins_constrainttipo_dato : VARCHAR\n                 | INTEGER\n                 | CHAR\n                 | TEXT\n                 | BIGINT\n                 | DECIMAL\n                 | NUMERIC\n                 | REAL definicion_valor_defecto : DEFAULT tipo_default \n                                | ins_constraint : CONSTRAINT ID restriccion_columna \n                                | restriccion_columna : NOT NULL\n                           | NULL\n                           | PRIMARY KEY\n                           | UNIQUE\n                           | FOREIGN KEY ID PARABRE ID PARCIERRE ins_referencesins_references : ON DELETE accion\n                      | ON UPDATE accionaccion : CASCADE\n              | SET NULL\n              | SET DEFAULT\n              | NO ACTIONtipo_default : NUMERIC\n                    | DECIMAL\n                    | NULLins_replace : OR REPLACE puntocoma\n               | if_exist :  IF NOT EXIST puntocoma\n                |  IF EXIST\n                | create_opciones : OWNER SIGNO_IGUAL ID\n                       | MODE SIGNO_IGUAL NUMEROpuntocoma : PUNTO_COMA\n                 | ins_alter : ALTER tipo_alter tipo_alter : DATABASE ID alter_database PUNTO_COMA\n                  | TABLE ID alteracion_tabla PUNTO_COMAalteracion_tabla : alteracion_tabla COMA alterar_tabla\n                        | alterar_tablaalterar_tabla : ADD COLUMN columna\n                     | ALTER COLUMN columna\n                     | DROP COLUMN ID\n                     | DROP CONSTRAINT IDalter_database : RENAME TO ID\n                      | OWNER TO IDins_drop : DROP tipo_droptipo_drop : DATABASE if_exist ID PUNTO_COMA\n                 | TABLE ID PUNTO_COMAins_insert : INSERT INTO ID VALUES PARABRE list_vls PARCIERRE PUNTO_COMA list_vls : list_vls COMA val_value\n                | val_value val_value : CADENA\n                |   NUMERO\n                |   NUM_DECIMAL\n                |   FECHA_HORA\n                |   TRUE\n                |   FALSE ins_select : ins_select UNION option_all ins_select\n                    |    ins_select INTERSECT option_all ins_select\n                    |    ins_select EXCEPT option_all ins_select\n                    |   SELECT arg_distict colum_list FROM list_expressions option_all   :   ALL\n                    |    arg_distict :    DISTINCT\n                    |    colum_list   : colum_list COMA columns as_id\n                        |   columns as_id\n                        |   SIGNO_POR columns   : ID dot_table\n                    |   aggregates dot_table    :   PUNTO ID\n                    |    as_id    :   AS ID\n                    |   AS CADENA\n                    |   CADENA\n                    |   aggregates   :   COUNT PARABRE param PARCIERRE\n                    |   SUM PARABRE param PARCIERRE\n                    |   AVG PARABRE param PARCIERRE\n                    |   MAX PARABRE param PARCIERRE\n                    |   MIN PARABRE param PARCIERRE param    :   ID\n                |   SIGNO_POR list_expressions    :   AS ID\n                    |    '
    
_lr_action_items = {'USE':([0,2,3,4,5,6,7,8,9,10,18,22,23,24,27,30,60,61,62,74,78,80,92,95,101,108,129,151,158,163,167,168,175,],[11,11,-3,-4,-5,-6,-7,-8,-9,-10,-2,-11,-12,-54,-65,-13,-77,-78,-79,-67,-52,-104,-55,-56,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'SHOW':([0,2,3,4,5,6,7,8,9,10,18,22,23,24,27,30,60,61,62,74,78,80,92,95,101,108,129,151,158,163,167,168,175,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-2,-11,-12,-54,-65,-13,-77,-78,-79,-67,-52,-104,-55,-56,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'ALTER':([0,2,3,4,5,6,7,8,9,10,18,22,23,24,27,30,42,60,61,62,74,78,80,92,95,96,101,108,129,151,158,163,167,168,175,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-2,-11,-12,-54,-65,-13,69,-77,-78,-79,-67,-52,-104,-55,-56,69,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'DROP':([0,2,3,4,5,6,7,8,9,10,18,22,23,24,27,30,42,60,61,62,74,78,80,92,95,96,101,108,129,151,158,163,167,168,175,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-2,-11,-12,-54,-65,-13,70,-77,-78,-79,-67,-52,-104,-55,-56,70,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'CREATE':([0,2,3,4,5,6,7,8,9,10,18,22,23,24,27,30,60,61,62,74,78,80,92,95,101,108,129,151,158,163,167,168,175,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-2,-11,-12,-54,-65,-13,-77,-78,-79,-67,-52,-104,-55,-56,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'INSERT':([0,2,3,4,5,6,7,8,9,10,18,22,23,24,27,30,60,61,62,74,78,80,92,95,101,108,129,151,158,163,167,168,175,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-2,-11,-12,-54,-65,-13,-77,-78,-79,-67,-52,-104,-55,-56,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'SELECT':([0,2,3,4,5,6,7,8,9,10,18,19,20,21,22,23,24,27,30,37,38,39,40,60,61,62,74,78,80,92,95,101,108,129,151,158,163,167,168,175,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-2,-82,-82,-82,-11,-12,-54,-65,-13,17,-81,17,17,-77,-78,-79,-67,-52,-104,-55,-56,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'$end':([1,2,3,4,5,6,7,8,9,10,18,22,23,24,27,30,60,61,62,74,78,80,92,95,101,108,129,151,158,163,167,168,175,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-11,-12,-54,-65,-13,-77,-78,-79,-67,-52,-104,-55,-56,-66,-80,-53,-103,-14,-15,-50,-51,-68,]),'UNION':([10,60,61,62,80,108,151,],[19,19,19,19,-104,-80,-103,]),'INTERSECT':([10,60,61,62,80,108,151,],[20,20,20,20,-104,-80,-103,]),'EXCEPT':([10,60,61,62,80,108,151,],[21,21,21,21,-104,-80,-103,]),'ID':([11,17,25,26,28,29,32,34,35,36,43,46,73,75,76,78,81,83,86,87,88,89,90,91,93,94,97,98,99,100,102,109,128,142,159,170,186,188,],[22,-84,41,42,-49,45,47,49,53,-83,71,-49,-48,103,104,-52,53,111,113,115,115,115,115,115,121,122,104,104,126,127,-53,151,-47,104,167,177,187,189,]),'DATABASES':([12,],[23,]),'DATABASE':([13,14,15,31,48,77,78,],[25,28,-46,46,-53,-45,-52,]),'TABLE':([13,14,15,],[26,29,32,]),'OR':([15,],[33,]),'INTO':([16,],[34,]),'DISTINCT':([17,],[36,]),'SIGNO_POR':([17,35,36,87,88,89,90,91,],[-84,52,-83,116,116,116,116,116,]),'COUNT':([17,35,36,81,],[-84,55,-83,55,]),'SUM':([17,35,36,81,],[-84,56,-83,56,]),'AVG':([17,35,36,81,],[-84,57,-83,57,]),'MAX':([17,35,36,81,],[-84,58,-83,58,]),'MIN':([17,35,36,81,],[-84,59,-83,59,]),'ALL':([19,20,21,],[38,38,38,]),'IF':([28,46,],[44,44,]),'REPLACE':([33,],[48,]),'RENAME':([41,],[64,]),'OWNER':([41,103,],[65,130,]),'ADD':([42,96,],[68,68,]),'NOT':([44,177,],[72,179,]),'EXIST':([44,72,],[73,102,]),'PUNTO_COMA':([45,48,63,66,67,71,102,121,122,123,124,125,126,127,129,132,133,134,135,136,137,138,139,140,141,161,165,167,168,169,171,172,173,174,178,180,182,184,185,191,195,196,199,200,201,202,],[74,78,92,95,-58,101,78,-63,-64,-57,-59,-60,-61,-62,78,-28,-19,-20,-21,-22,-23,-24,-25,-26,163,-30,175,-50,-51,-18,-27,-42,-43,-44,-29,-32,-34,-31,-33,-35,-36,-38,-37,-39,-40,-41,]),'PARABRE':([47,55,56,57,58,59,79,187,],[76,87,88,89,90,91,107,188,]),'VALUES':([49,],[79,]),'FROM':([50,51,52,53,54,82,84,85,110,111,112,113,152,153,154,155,156,157,],[80,-95,-87,-91,-89,-86,-94,-88,-95,-92,-93,-90,-85,-96,-97,-98,-99,-100,]),'COMA':([50,51,52,53,54,66,67,82,84,85,105,106,110,111,112,113,123,124,125,126,127,132,133,134,135,136,137,138,139,140,143,144,145,146,147,148,149,150,152,153,154,155,156,157,161,164,169,171,172,173,174,176,178,180,182,184,185,191,195,196,199,200,201,202,],[81,-95,-87,-91,-89,96,-58,-86,-94,-88,142,-17,-95,-92,-93,-90,-57,-59,-60,-61,-62,-28,-19,-20,-21,-22,-23,-24,-25,-26,166,-70,-71,-72,-73,-74,-75,-76,-85,-96,-97,-98,-99,-100,-30,-16,-18,-27,-42,-43,-44,-69,-29,-32,-34,-31,-33,-35,-36,-38,-37,-39,-40,-41,]),'AS':([51,53,54,80,85,110,113,153,154,155,156,157,],[83,-91,-89,109,-88,83,-90,-96,-97,-98,-99,-100,]),'CADENA':([51,53,54,83,85,107,110,113,153,154,155,156,157,166,],[84,-91,-89,112,-88,145,84,-90,-96,-97,-98,-99,-100,145,]),'PUNTO':([53,],[86,]),'TO':([64,65,],[93,94,]),'COLUMN':([68,69,70,],[97,98,99,]),'CONSTRAINT':([70,132,133,134,135,136,137,138,139,140,161,171,172,173,174,],[100,-28,-19,-20,-21,-22,-23,-24,-25,-26,170,-27,-42,-43,-44,]),'MODE':([103,],[131,]),'VARCHAR':([104,],[133,]),'INTEGER':([104,],[134,]),'CHAR':([104,],[135,]),'TEXT':([104,],[136,]),'BIGINT':([104,],[137,]),'DECIMAL':([104,162,],[138,173,]),'NUMERIC':([104,162,],[139,172,]),'REAL':([104,],[140,]),'PARCIERRE':([105,106,114,115,116,117,118,119,120,132,133,134,135,136,137,138,139,140,143,144,145,146,147,148,149,150,161,164,169,171,172,173,174,176,178,180,182,184,185,189,191,195,196,199,200,201,202,],[141,-17,153,-101,-102,154,155,156,157,-28,-19,-20,-21,-22,-23,-24,-25,-26,165,-70,-71,-72,-73,-74,-75,-76,-30,-16,-18,-27,-42,-43,-44,-69,-29,-32,-34,-31,-33,190,-35,-36,-38,-37,-39,-40,-41,]),'NUMERO':([107,160,166,],[146,168,146,]),'NUM_DECIMAL':([107,166,],[147,147,]),'FECHA_HORA':([107,166,],[148,148,]),'TRUE':([107,166,],[149,149,]),'FALSE':([107,166,],[150,150,]),'SIGNO_IGUAL':([130,131,],[159,160,]),'DEFAULT':([132,133,134,135,136,137,138,139,140,197,],[162,-19,-20,-21,-22,-23,-24,-25,-26,201,]),'NULL':([162,177,179,197,],[174,180,184,200,]),'PRIMARY':([177,],[181,]),'UNIQUE':([177,],[182,]),'FOREIGN':([177,],[183,]),'KEY':([181,183,],[185,186,]),'ON':([190,],[192,]),'DELETE':([192,],[193,]),'UPDATE':([192,],[194,]),'CASCADE':([193,194,],[196,196,]),'SET':([193,194,],[197,197,]),'NO':([193,194,],[198,198,]),'ACTION':([198,],[202,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,18,]),'ins_use':([0,2,],[4,4,]),'ins_show':([0,2,],[5,5,]),'ins_alter':([0,2,],[6,6,]),'ins_drop':([0,2,],[7,7,]),'ins_create':([0,2,],[8,8,]),'ins_insert':([0,2,],[9,9,]),'ins_select':([0,2,37,39,40,],[10,10,60,61,62,]),'tipo_alter':([13,],[24,]),'tipo_drop':([14,],[27,]),'tipo_create':([15,],[30,]),'ins_replace':([15,],[31,]),'arg_distict':([17,],[35,]),'option_all':([19,20,21,],[37,39,40,]),'if_exist':([28,46,],[43,75,]),'colum_list':([35,],[50,]),'columns':([35,81,],[51,110,]),'aggregates':([35,81,],[54,54,]),'alter_database':([41,],[63,]),'alteracion_tabla':([42,],[66,]),'alterar_tabla':([42,96,],[67,123,]),'puntocoma':([48,102,129,],[77,128,158,]),'as_id':([51,110,],[82,152,]),'dot_table':([53,],[85,]),'definicion_columna':([76,],[105,]),'columna':([76,97,98,142,],[106,124,125,164,]),'list_expressions':([80,],[108,]),'param':([87,88,89,90,91,],[114,117,118,119,120,]),'create_opciones':([103,],[129,]),'tipo_dato':([104,],[132,]),'list_vls':([107,],[143,]),'val_value':([107,166,],[144,176,]),'definicion_valor_defecto':([132,],[161,]),'ins_constraint':([161,],[169,]),'tipo_default':([162,],[171,]),'restriccion_columna':([177,],[178,]),'ins_references':([190,],[191,]),'accion':([193,194,],[195,199,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_inicio','Lexico.py',158),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Lexico.py',161),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','Lexico.py',162),
  ('instruccion -> ins_use','instruccion',1,'p_instrucciones_evaluar','Lexico.py',165),
  ('instruccion -> ins_show','instruccion',1,'p_instrucciones_evaluar','Lexico.py',166),
  ('instruccion -> ins_alter','instruccion',1,'p_instrucciones_evaluar','Lexico.py',167),
  ('instruccion -> ins_drop','instruccion',1,'p_instrucciones_evaluar','Lexico.py',168),
  ('instruccion -> ins_create','instruccion',1,'p_instrucciones_evaluar','Lexico.py',169),
  ('instruccion -> ins_insert','instruccion',1,'p_instrucciones_evaluar','Lexico.py',170),
  ('instruccion -> ins_select','instruccion',1,'p_instrucciones_evaluar','Lexico.py',171),
  ('ins_use -> USE ID','ins_use',2,'p_instruccion_use','Lexico.py',174),
  ('ins_show -> SHOW DATABASES','ins_show',2,'p_instruccion_show','Lexico.py',178),
  ('ins_create -> CREATE tipo_create','ins_create',2,'p_instruccion_create','Lexico.py',182),
  ('tipo_create -> ins_replace DATABASE if_exist ID create_opciones puntocoma','tipo_create',6,'p_tipo_create','Lexico.py',186),
  ('tipo_create -> TABLE ID PARABRE definicion_columna PARCIERRE PUNTO_COMA','tipo_create',6,'p_tipo_create','Lexico.py',187),
  ('definicion_columna -> definicion_columna COMA columna','definicion_columna',3,'p_definicion_columna','Lexico.py',190),
  ('definicion_columna -> columna','definicion_columna',1,'p_definicion_columna','Lexico.py',191),
  ('columna -> ID tipo_dato definicion_valor_defecto ins_constraint','columna',4,'p_columna','Lexico.py',194),
  ('tipo_dato -> VARCHAR','tipo_dato',1,'p_tipo_dato','Lexico.py',197),
  ('tipo_dato -> INTEGER','tipo_dato',1,'p_tipo_dato','Lexico.py',198),
  ('tipo_dato -> CHAR','tipo_dato',1,'p_tipo_dato','Lexico.py',199),
  ('tipo_dato -> TEXT','tipo_dato',1,'p_tipo_dato','Lexico.py',200),
  ('tipo_dato -> BIGINT','tipo_dato',1,'p_tipo_dato','Lexico.py',201),
  ('tipo_dato -> DECIMAL','tipo_dato',1,'p_tipo_dato','Lexico.py',202),
  ('tipo_dato -> NUMERIC','tipo_dato',1,'p_tipo_dato','Lexico.py',203),
  ('tipo_dato -> REAL','tipo_dato',1,'p_tipo_dato','Lexico.py',204),
  ('definicion_valor_defecto -> DEFAULT tipo_default','definicion_valor_defecto',2,'p_definicion_valor_defecto','Lexico.py',208),
  ('definicion_valor_defecto -> <empty>','definicion_valor_defecto',0,'p_definicion_valor_defecto','Lexico.py',209),
  ('ins_constraint -> CONSTRAINT ID restriccion_columna','ins_constraint',3,'p_ins_constraint','Lexico.py',212),
  ('ins_constraint -> <empty>','ins_constraint',0,'p_ins_constraint','Lexico.py',213),
  ('restriccion_columna -> NOT NULL','restriccion_columna',2,'p_restriccion_columna','Lexico.py',216),
  ('restriccion_columna -> NULL','restriccion_columna',1,'p_restriccion_columna','Lexico.py',217),
  ('restriccion_columna -> PRIMARY KEY','restriccion_columna',2,'p_restriccion_columna','Lexico.py',218),
  ('restriccion_columna -> UNIQUE','restriccion_columna',1,'p_restriccion_columna','Lexico.py',219),
  ('restriccion_columna -> FOREIGN KEY ID PARABRE ID PARCIERRE ins_references','restriccion_columna',7,'p_restriccion_columna','Lexico.py',220),
  ('ins_references -> ON DELETE accion','ins_references',3,'p_references','Lexico.py',224),
  ('ins_references -> ON UPDATE accion','ins_references',3,'p_references','Lexico.py',225),
  ('accion -> CASCADE','accion',1,'p_accion','Lexico.py',228),
  ('accion -> SET NULL','accion',2,'p_accion','Lexico.py',229),
  ('accion -> SET DEFAULT','accion',2,'p_accion','Lexico.py',230),
  ('accion -> NO ACTION','accion',2,'p_accion','Lexico.py',231),
  ('tipo_default -> NUMERIC','tipo_default',1,'p_tipo_default','Lexico.py',234),
  ('tipo_default -> DECIMAL','tipo_default',1,'p_tipo_default','Lexico.py',235),
  ('tipo_default -> NULL','tipo_default',1,'p_tipo_default','Lexico.py',236),
  ('ins_replace -> OR REPLACE puntocoma','ins_replace',3,'p_ins_replace','Lexico.py',239),
  ('ins_replace -> <empty>','ins_replace',0,'p_ins_replace','Lexico.py',240),
  ('if_exist -> IF NOT EXIST puntocoma','if_exist',4,'p_if_exist','Lexico.py',243),
  ('if_exist -> IF EXIST','if_exist',2,'p_if_exist','Lexico.py',244),
  ('if_exist -> <empty>','if_exist',0,'p_if_exist','Lexico.py',245),
  ('create_opciones -> OWNER SIGNO_IGUAL ID','create_opciones',3,'p_create_opciones','Lexico.py',248),
  ('create_opciones -> MODE SIGNO_IGUAL NUMERO','create_opciones',3,'p_create_opciones','Lexico.py',249),
  ('puntocoma -> PUNTO_COMA','puntocoma',1,'p_puntocoma','Lexico.py',252),
  ('puntocoma -> <empty>','puntocoma',0,'p_puntocoma','Lexico.py',253),
  ('ins_alter -> ALTER tipo_alter','ins_alter',2,'p_alter','Lexico.py',256),
  ('tipo_alter -> DATABASE ID alter_database PUNTO_COMA','tipo_alter',4,'p_tipo_alter','Lexico.py',260),
  ('tipo_alter -> TABLE ID alteracion_tabla PUNTO_COMA','tipo_alter',4,'p_tipo_alter','Lexico.py',261),
  ('alteracion_tabla -> alteracion_tabla COMA alterar_tabla','alteracion_tabla',3,'p_alteracion_tabla','Lexico.py',264),
  ('alteracion_tabla -> alterar_tabla','alteracion_tabla',1,'p_alteracion_tabla','Lexico.py',265),
  ('alterar_tabla -> ADD COLUMN columna','alterar_tabla',3,'p_alterar_tabla','Lexico.py',268),
  ('alterar_tabla -> ALTER COLUMN columna','alterar_tabla',3,'p_alterar_tabla','Lexico.py',269),
  ('alterar_tabla -> DROP COLUMN ID','alterar_tabla',3,'p_alterar_tabla','Lexico.py',270),
  ('alterar_tabla -> DROP CONSTRAINT ID','alterar_tabla',3,'p_alterar_tabla','Lexico.py',271),
  ('alter_database -> RENAME TO ID','alter_database',3,'p_alter_database','Lexico.py',274),
  ('alter_database -> OWNER TO ID','alter_database',3,'p_alter_database','Lexico.py',275),
  ('ins_drop -> DROP tipo_drop','ins_drop',2,'p_drop','Lexico.py',278),
  ('tipo_drop -> DATABASE if_exist ID PUNTO_COMA','tipo_drop',4,'p_tipo_drop','Lexico.py',281),
  ('tipo_drop -> TABLE ID PUNTO_COMA','tipo_drop',3,'p_tipo_drop','Lexico.py',282),
  ('ins_insert -> INSERT INTO ID VALUES PARABRE list_vls PARCIERRE PUNTO_COMA','ins_insert',8,'p_ins_insert','Lexico.py',288),
  ('list_vls -> list_vls COMA val_value','list_vls',3,'p_list_vls','Lexico.py',293),
  ('list_vls -> val_value','list_vls',1,'p_list_vls','Lexico.py',294),
  ('val_value -> CADENA','val_value',1,'p_val_value','Lexico.py',297),
  ('val_value -> NUMERO','val_value',1,'p_val_value','Lexico.py',298),
  ('val_value -> NUM_DECIMAL','val_value',1,'p_val_value','Lexico.py',299),
  ('val_value -> FECHA_HORA','val_value',1,'p_val_value','Lexico.py',300),
  ('val_value -> TRUE','val_value',1,'p_val_value','Lexico.py',301),
  ('val_value -> FALSE','val_value',1,'p_val_value','Lexico.py',302),
  ('ins_select -> ins_select UNION option_all ins_select','ins_select',4,'p_ins_select','Lexico.py',305),
  ('ins_select -> ins_select INTERSECT option_all ins_select','ins_select',4,'p_ins_select','Lexico.py',306),
  ('ins_select -> ins_select EXCEPT option_all ins_select','ins_select',4,'p_ins_select','Lexico.py',307),
  ('ins_select -> SELECT arg_distict colum_list FROM list_expressions','ins_select',5,'p_ins_select','Lexico.py',308),
  ('option_all -> ALL','option_all',1,'p_option_all','Lexico.py',311),
  ('option_all -> <empty>','option_all',0,'p_option_all','Lexico.py',312),
  ('arg_distict -> DISTINCT','arg_distict',1,'p_arg_distict','Lexico.py',315),
  ('arg_distict -> <empty>','arg_distict',0,'p_arg_distict','Lexico.py',316),
  ('colum_list -> colum_list COMA columns as_id','colum_list',4,'p_colum_list','Lexico.py',319),
  ('colum_list -> columns as_id','colum_list',2,'p_colum_list','Lexico.py',320),
  ('colum_list -> SIGNO_POR','colum_list',1,'p_colum_list','Lexico.py',321),
  ('columns -> ID dot_table','columns',2,'p_columns','Lexico.py',325),
  ('columns -> aggregates','columns',1,'p_columns','Lexico.py',326),
  ('dot_table -> PUNTO ID','dot_table',2,'p_dot_table','Lexico.py',329),
  ('dot_table -> <empty>','dot_table',0,'p_dot_table','Lexico.py',330),
  ('as_id -> AS ID','as_id',2,'p_as_id','Lexico.py',333),
  ('as_id -> AS CADENA','as_id',2,'p_as_id','Lexico.py',334),
  ('as_id -> CADENA','as_id',1,'p_as_id','Lexico.py',335),
  ('as_id -> <empty>','as_id',0,'p_as_id','Lexico.py',336),
  ('aggregates -> COUNT PARABRE param PARCIERRE','aggregates',4,'p_aggregates','Lexico.py',340),
  ('aggregates -> SUM PARABRE param PARCIERRE','aggregates',4,'p_aggregates','Lexico.py',341),
  ('aggregates -> AVG PARABRE param PARCIERRE','aggregates',4,'p_aggregates','Lexico.py',342),
  ('aggregates -> MAX PARABRE param PARCIERRE','aggregates',4,'p_aggregates','Lexico.py',343),
  ('aggregates -> MIN PARABRE param PARCIERRE','aggregates',4,'p_aggregates','Lexico.py',344),
  ('param -> ID','param',1,'p_param','Lexico.py',347),
  ('param -> SIGNO_POR','param',1,'p_param','Lexico.py',348),
  ('list_expressions -> AS ID','list_expressions',2,'p_list_expressions','Lexico.py',351),
  ('list_expressions -> <empty>','list_expressions',0,'p_list_expressions','Lexico.py',352),
]
