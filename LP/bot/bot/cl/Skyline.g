grammar Skyline;

root : ini EOF ;

ini: expr | assig;

assig: IDENT ':=' creadora
    | IDENT ':=' expr
    ;


expr : '(' expr ')'
    | RESTA expr
    | expr MULT expr
    | expr MULT NUM
    | expr SUMA expr
    | expr SUMA NUM
    | expr RESTA NUM
    | IDENT
    | creadora
    ;


creadora : simple
    | composta
    | aleatoria
    ;

simple : '(' NUM ',' NUM ',' NUM ')' ;

composta: '[' simple (',' simple)* ']' ;

aleatoria: '{' NUM ',' NUM ',' NUM ',' NUM  ',' NUM '}' ;

NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;

IDENT: [a-zA-Z] [a-z0-9A-Z]* ;

MULT:  '*';
SUMA:  '+';
RESTA: '-';
