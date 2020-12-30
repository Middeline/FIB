grammar Skyline;

root : assign EOF
    | op EOF;

assign : ID ':=' constructor
    | ID ':=' op
    ;

constructor : edifici
    | '[' edifici (',' edifici)* ']'
    | '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}'
    ;

edifici : '(' NUM ',' NUM ',' NUM ')';

op : '(' op ')'
    | SUB op
    | op MULT op
    | op MULT NUM
    | op ADD NUM
    | op SUB NUM
    | op ADD op
    | ID
    | constructor
    ;

NUM : [0-9]+ ;
ID : [a-zA-Z] [a-zA-Z0-9]*; 
MULT : '*' ; 
SUB : '-' ;
ADD : '+' ;
WS : [ \r\t\n]+ -> skip ;