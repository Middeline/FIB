symbolicOutput(0).  % set to 1 to see symbolic output only; 0 otherwise.

%:- include(entradaHoraris1).
numCursos(4).
numAssignatures(23).
numAules(3).
numProfes(5).

% Sintaxi: assig(curs,assignatura,hores,llistaAules,llistaProfessors).
assig(1,1,3,[3],[2,3,4,5]).
assig(1,2,2,[2,3],[1,2,3,4,5]).
assig(1,3,4,[2,3],[1,2,3,4,5]).
assig(1,4,2,[2,3],[2,3,4,5]).
assig(1,5,2,[1,2,3],[1,5]).

assig(2,6,3,[1,3],[1,4,5]).
assig(2,7,4,[1,2,3],[1,2,3,4,5]).
assig(2,8,2,[1,2,3],[5]).
assig(2,9,3,[1,2,3],[1,2,5]).
assig(2,10,4,[1,3],[4,5]).

assig(3,11,2,[1],[3,4]).
assig(3,12,2,[2],[2,3,4,5]).
assig(3,13,3,[1,2,3],[1,2,3,5]).
assig(3,14,2,[1,2,3],[1,2,3,4,5]).
assig(3,15,2,[1],[2,3,4,5]).
assig(3,16,3,[1],[1]).

assig(4,17,4,[2,3],[5]).
assig(4,18,3,[1],[1,2,4,5]).
assig(4,19,2,[1,2,3],[1,4]).
assig(4,20,2,[1,2,3],[1,2,3]).
assig(4,21,3,[1,2,3],[1,3,5]).
assig(4,22,4,[1],[2,4]).
assig(4,23,2,[1,2,3],[4]).

% Sintaxi: horesProhibides(professor,llistaHores).
horesProhibides(1,[1,10,11,12,17,21,24,27,43,49]).
horesProhibides(2,[4,5,8,9,12,18,19,28,38,46,49,51,53,55,60]).
horesProhibides(3,[2,3,4,7,8,9,11,16,21,25,26,33,37,40,45,52,53,55,57]).
horesProhibides(4,[1,2,9,10,20,23,25,26,29,31,32,34,37,40,42,44,45,47,48,49,50,51,52,53,57,58,59]).
horesProhibides(5,[3,4,8,9,15,24,25,30,32,33,38,39,43,45,46,49,51,52,58]).
%%%%%% Some helpful definitions to make the code cleaner:

year(Y) :- numCursos(N), between(1,N,Y).
hora(H) :- between(1,60,H).
profe(T) :- numProfes(N), between(1,N,T).
profesAsig(S,Ts) :- assignatura(S), assig(_,S,_,_,Ts).
aulasAsig(S,Rs) :- assignatura(S), assig(_,S,_,Rs,_).
numClasesAsig(S,L) :- assig(_,S,N,_,_), between(1,N,L).
curso(C) :- numCursos(N), between(1,N,C).
aula(R) :- numAules(N), between(1,N,R).
assignatura(S) :- numAssignatures(N), between(1,N,S).
whichDay(H,D) :- D is (H-1)//12.
firstHourOfDay(D,H) :- H is (D*12)+1.
lastHourOfDay(D,H) :- H is (D+1)*12.
dia(D) :- between(0,4,D).
sameDay(H1,H2) :- hora(H1), hora(H2), whichDay(H1,D1), whichDay(H2,D2), D1 = D2.
asigMismoCurso(S1,S2) :-  year(Y1), year(Y2), assig(Y1,S1,_,_,_), assig(Y2,S2,_,_,_), Y1 \= Y2.
asigCurso(S,Y) :- year(Y), assignatura(S), assig(Y,S,_,_,_).
profeNoClasesEnHora(T,H) :- profe(T), horesProhibides(T,X), member(H,X).

%%%%%%  1. SAT Variables:
%ESTAS VARIABLES SERAN SIMBOLICAS. ES DECIR, NO LAS QUE TE DEVUELVE TAL CUAL PICOSAT.
satVariable( st(S,T) ) :- profe(T), assignatura(S). %assig(_,S_,_,ListaProfes), member(T,ListaProfes).
satVariable( slh(S,L,H) ) :- assignatura(S), numClasesAsig(S,L), hora(H).
satVariable( sr(S,R) ) :- assignatura(S), aula(R).
satVariable( sh(S,H)) :- assignatura(S), hora(H).   %algunas de las sesiones de la asignatura S, se imparte en la hora H.
satVariable( sd(S,D)) :- assignatura(S), dia(D).  %algunas de las sesiones de la asignatura S, se imparten el dia D.
satVariable( dlh(Y,D1,H)) :- year(Y), dia(D1), hora(H). %hay clases en las horas < H del dia D en el curso Y
satVariable( dgh(Y,D1,H)) :- year(Y), dia(D1), hora(H). %hay clases en las horas > H del dia D en el curso Y
satVariable( ah(Y,H)) :- year(Y), hora(H). %hay clases en la hora H en el curso Y
%%%%%%  2. Clause generation:

writeClauses:- %se especifican las restricciones.
      horesp,
      definitionOfVariableDayLessThanHour, %definicion de la variable dlh(Y,D,H)
      definitionOfVariableDayGreaterThanHour, %definicion de la variable dgh(Y,D,H)
      definitionOfVariableAtHour, %definicion de la variable ah(Y,H)
      definitionOfVariableSubjectDay,  %definicion de la variable sd(S,D)
      definitionOfVariableSubjectHour, %definicion de la variable sh(S,H)
      una_leccion,        %Cada sesion de una asignatura solo ocurre 1 vez a la semana
      distinto_profe, %no pueden haber 2 sesiones de 2 asignaturas distintas al mismo tiempo con el mismo profe.
      distinta_classe,    %no pueden haber 2 sesiones de 2 asignaturas distintas al mismo tiempo en el mismo aula.
      unapordia,      %Cada asignatura, hace maximo una hora al dia.
      profe_por_assig,   %Cada asignatura, tiene un unico profe.
      una_room_assig,      %Cada asignatura, tiene un unico aula.
      cadahora,  % para cada hora, no pueden haber >1 sesiones de >1 asignaturas distintas que pertenezcan al mismo curso.
      assigs6,
      horari_com,
       true,!.

writeClauses:- told, nl, write('writeClauses failed!'), nl,nl, halt.


definitionOfVariableAtHour:- year(Y), hora(H), findall(sh(S,H), asigCurso(S,Y), Lits),
                             expressOr(ah(Y,H), Lits), fail.
definitionOfVariableAtHour.

definitionOfVariableDayLessThanHour:- year(Y), dia(D), hora(H1),
                                      firstHourOfDay(D,Hini), lastHourOfDay(D,Hfin), whichDay(H1,D),
                                      findall(sh(S,H2), (asigCurso(S,Y), hora(H2), H2 >= Hini, H2 =< Hfin, H2 < H1), Lits),
                                      expressOr(dlh(Y,D,H1), Lits), fail.
definitionOfVariableDayLessThanHour.

definitionOfVariableDayGreaterThanHour:- year(Y), dia(D), hora(H1),
                                      firstHourOfDay(D,Hini), lastHourOfDay(D,Hfin), whichDay(H1,D),
                                      findall(sh(S,H2), (asigCurso(S,Y), hora(H2), H2 >= Hini, H2 =< Hfin, H2 > H1), Lits),
                                      expressOr(dgh(Y,D,H1), Lits), fail.
definitionOfVariableDayGreaterThanHour.

definitionOfVariableSubjectDay:- assignatura(S), dia(D1),
                                 findall(sh(S,H), (hora(H), whichDay(H,D2), D1 = D2), Lits),
                                 expressOr(sd(S,D1), Lits), fail.
definitionOfVariableSubjectDay.

definitionOfVariableSubjectHour:- assignatura(S), hora(H),
                                  findall(slh(S,L,H), numClasesAsig(S,L), Lits),
                                  expressOr(sh(S,H), Lits), fail.
definitionOfVariableSubjectHour.

profe_por_assig:- assignatura(S), profesAsig(S,Ts),
                         findall(st(S,T),member(T,Ts),Lits),
                         exactly(1,Lits),fail.
profe_por_assig.


una_room_assig:- assignatura(S), aulasAsig(S,Rs),
                      findall(sr(S,R), member(R,Rs), Lits),
                      exactly(1,Lits), fail.
una_room_assig.


una_leccion:-  assignatura(S), numClasesAsig(S,L),
                              findall(slh(S,L,H), hora(H), Lits),
                              exactly(1,Lits), fail.
una_leccion.


distinto_profe:-  hora(H), assignatura(S1), assignatura(S2),
                        S1 \= S2, profe(T),
                        writeClause([ -sh(S1,H), -sh(S2,H), -st(S1,T), -st(S2,T)]),
                        fail.
distinto_profe.


distinta_classe:-     hora(H), assignatura(S1), assignatura(S2),
                        S1 \= S2, aula(R),
                        writeClause([ -sh(S1,H), -sh(S2,H), -sr(S1,R), -sr(S2,R)]),
                        fail.
distinta_classe.


unapordia:-  assignatura(S), hora(H1), hora(H2), H1 < H2,
                                  sameDay(H1,H2), writeClause([ -sh(S,H1), -sh(S,H2) ]),
                                  fail.
unapordia.


cadahora :- year(Y), hora(H),
                                 findall(slh(S,L,H), (asigCurso(S,Y), numClasesAsig(S,L)), Lits),
                                 atMost(1,Lits), fail.
cadahora.

assigs6:- year(Y), dia(D),
                           findall(sd(S,D), asigCurso(S,Y), Lits),
                           atMost(6,Lits), fail.
assigs6.

horari_com:- year(Y), dia(D), hora(H), whichDay(H,D),
                    writeClause( [-dlh(Y,D,H), ah(Y,H), -dgh(Y,D,H)] ),
                    fail.
horari_com.

horesp :- assignatura(S), profe(T), profeNoClasesEnHora(T,H),
                  writeClause( [-sh(S,H), -st(S,T)]), fail.
horesp.

%%%%%%  3. DisplaySol: show the solution. Here M contains the literals that are true in the model:

extraBlank(N):-
    N < 10, !, write(' ').
extraBlank(_).

drawTail(Y, Hour):-
    Hour > 48,
    write('  Curs: '), write(Y), nl.
drawTail(_, _).

drawCell(Y, S, M):-
    member(slh(C,L,S), M),                   %% -------- ADAPTA la SAT variable cls(C,L,S)
    assig(Y, C, _, _, _), !,
    write(' '), extraBlank(C), write(C), write(' - '),
    extraBlank(L), write(L),
    write('  ['), member(sr(C,R), M),        %% -------  ADAPTA la SAT variable cr(C,R)
    write('A:'), extraBlank(R), write(' '), write(R), write(']'),
    write('  ['), member(st(C,T), M),        %% -------  ADAPTA la SAT variable ct(C,T)
    write('P:'), extraBlank(T), write(' '), write(T), write(']'),
    write(' ').
drawCell(_, _, _):-
    write('                           ').

drawRow(Row, _):-
    1 is Row mod 2,
    H is Row // 2 + 8,
    extraBlank(H),
    write(' '), write(H), write(':00 '),
    between(1, 141, _), write('='),
    fail.
drawRow(Row, _):-
    1 is Row mod 2, !, nl.

drawRow(Row, M):-
    year(Y),
    write('       |'),
    between(0, 4, Day),
    Hour is Row // 2 + Day * 12,
    drawCell(Y, Hour, M),
    write('|'),
    drawTail(Y, Hour),
    fail.
drawRow(_, _).

drawHeader:-
    nl, nl,
    write(' Format de sortida: Assignatura - Hora [A: Aula] [P: Professor]'),
    nl, nl,
    write('                 Dilluns                     Dimarts                     dimecres                     Dijous                    Divendres').

displaySchedule(M):-
    drawHeader, nl,
    between(1, 25, Row),
    drawRow(Row, M),
    fail.

drawHeaderYear(Y):-
    nl, nl,
    write('----------------------------------------------------------------------------------------------------------------------------------------------------'),
    nl,
    write(' Horari del curs '), write(Y),
    nl,
    write(' Format de sortida: Assignatura - Hora [A: Aula] [P: Professor]'),
    nl, nl,
    write('                 Dilluns                     Dimarts                     dimecres                     Dijous                    Divendres').

drawTailYear(Hour):-
    Hour > 48, nl.
drawTailYear(_, _).

drawRowYear(Row, _, _):-
    1 is Row mod 2,
    H is Row // 2 + 8,
    extraBlank(H),
    write(' '), write(H), write(':00 '),
    between(1, 141, _), write('='),
    fail.
drawRowYear(Row, _, _):-
    1 is Row mod 2, !, nl.
drawRowYear(Row, Y, M):-
    write('       |'),
    between(0, 4, Day),
    Hour is Row // 2 + Day * 12,
    drawCell(Y, Hour, M),
    write('|'),
    drawTailYear(Hour),
    fail.
drawRowYear(_, _, _).

displayScheduleYear(Y,M):-
    drawHeaderYear(Y), nl,
    between(1, 25, Row),
    drawRowYear(Row, Y, M),
    fail.

displaySol(M):- displaySchedule(M), fail.
displaySol(M):- year(Y), displayScheduleYear(Y,M), fail.
displaySol(_).
%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Everything below is given as a standard library, reusable for solving
%    with SAT many different problems.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Express that Var is equivalent to the disjunction of Lits:
expressOr( Var, Lits) :- symbolicOutput(1), write( Var ), write(' <--> or('), write(Lits), write(')'), nl, !.
expressOr( Var, Lits ):- member(Lit,Lits), negate(Lit,NLit), writeClause([ NLit, Var ]), fail.
expressOr( Var, Lits ):- negate(Var,NVar), writeClause([ NVar | Lits ]),!.

% Express that Var is equivalent to the conjunction of Lits:
expressAnd( Var, Lits) :- symbolicOutput(1), write( Var ), write(' <--> and('), write(Lits), write(')'), nl, !.
expressAnd( Var, Lits):- member(Lit,Lits), negate(Var,NVar), writeClause([ NVar, Lit ]), fail.
expressAnd( Var, Lits):- findall(NLit, (member(Lit,Lits), negate(Lit,NLit)), NLits), writeClause([ Var | NLits]), !.


%%%%%% Cardinality constraints on arbitrary sets of literals Lits:

exactly(K,Lits):- symbolicOutput(1), write( exactly(K,Lits) ), nl, !.
exactly(K,Lits):- atLeast(K,Lits), atMost(K,Lits),!.

atMost(K,Lits):- symbolicOutput(1), write( atMost(K,Lits) ), nl, !.
atMost(K,Lits):-   % l1+...+ln <= k:  in all subsets of size k+1, at least one is false:
	negateAll(Lits,NLits),
	K1 is K+1,    subsetOfSize(K1,NLits,Clause), writeClause(Clause),fail.
atMost(_,_).

atLeast(K,Lits):- symbolicOutput(1), write( atLeast(K,Lits) ), nl, !.
atLeast(K,Lits):-  % l1+...+ln >= k: in all subsets of size n-k+1, at least one is true:
	length(Lits,N),
	K1 is N-K+1,  subsetOfSize(K1, Lits,Clause), writeClause(Clause),fail.
atLeast(_,_).

negateAll( [], [] ).
negateAll( [Lit|Lits], [NLit|NLits] ):- negate(Lit,NLit), negateAll( Lits, NLits ),!.

negate( -Var,  Var):-!.
negate(  Var, -Var):-!.

subsetOfSize(0,_,[]):-!.
subsetOfSize(N,[X|L],[X|S]):- N1 is N-1, length(L,Leng), Leng>=N1, subsetOfSize(N1,L,S).
subsetOfSize(N,[_|L],   S ):-            length(L,Leng), Leng>=N,  subsetOfSize( N,L,S).


%%%%%% main:

main:-  symbolicOutput(1), !, writeClauses, halt.   % print the clauses in symbolic form and halt
main:-  initClauseGeneration,
tell(clauses), writeClauses, told,          % generate the (numeric) SAT clauses and call the solver
tell(header),  writeHeader,  told,
numVars(N), numClauses(C),
write('Generated '), write(C), write(' clauses over '), write(N), write(' variables. '),nl,
shell('cat header clauses > infile.cnf',_),
write('Calling solver....'), nl,
shell('picosat -v -o model infile.cnf', Result),  % if sat: Result=10; if unsat: Result=20.
	treatResult(Result),!.

treatResult(20):- write('Unsatisfiable'), nl, halt.
treatResult(10):- write('Solution found: '), nl, see(model), symbolicModel(M), seen, displaySol(M), nl,nl,halt.
treatResult( _):- write('cnf input error. Wrote anything strange in your cnf?'), nl,nl, halt.


initClauseGeneration:-  %initialize all info about variables and clauses:
	retractall(numClauses(   _)),
	retractall(numVars(      _)),
	retractall(varNumber(_,_,_)),
	assert(numClauses( 0 )),
	assert(numVars(    0 )),     !.

writeClause([]):- symbolicOutput(1),!, nl.
writeClause([]):- countClause, write(0), nl.
writeClause([Lit|C]):- w(Lit), writeClause(C),!.
w(-Var):- symbolicOutput(1), satVariable(Var), write(-Var), write(' '),!.
w( Var):- symbolicOutput(1), satVariable(Var), write( Var), write(' '),!.
w(-Var):- satVariable(Var),  var2num(Var,N),   write(-), write(N), write(' '),!.
w( Var):- satVariable(Var),  var2num(Var,N),             write(N), write(' '),!.
w( Lit):- told, write('ERROR: generating clause with undeclared variable in literal '), write(Lit), nl,nl, halt.


% given the symbolic variable V, find its variable number N in the SAT solver:
:-dynamic(varNumber / 3).
var2num(V,N):- hash_term(V,Key), existsOrCreate(V,Key,N),!.
existsOrCreate(V,Key,N):- varNumber(Key,V,N),!.                            % V already existed with num N
existsOrCreate(V,Key,N):- newVarNumber(N), assert(varNumber(Key,V,N)), !.  % otherwise, introduce new N for V

writeHeader:- numVars(N),numClauses(C), write('p cnf '),write(N), write(' '),write(C),nl.

countClause:-     retract( numClauses(N0) ), N is N0+1, assert( numClauses(N) ),!.
newVarNumber(N):- retract( numVars(   N0) ), N is N0+1, assert(    numVars(N) ),!.

% Getting the symbolic model M from the output file:
symbolicModel(M):- get_code(Char), readWord(Char,W), symbolicModel(M1), addIfPositiveInt(W,M1,M),!.
symbolicModel([]).
addIfPositiveInt(W,L,[Var|L]):- W = [C|_], between(48,57,C), number_codes(N,W), N>0, varNumber(_,Var,N),!.
addIfPositiveInt(_,L,L).
readWord( 99,W):- repeat, get_code(Ch), member(Ch,[-1,10]), !, get_code(Ch1), readWord(Ch1,W),!. % skip line starting w/ c
readWord(115,W):- repeat, get_code(Ch), member(Ch,[-1,10]), !, get_code(Ch1), readWord(Ch1,W),!. % skip line starting w/ s
readWord(-1,_):-!, fail. %end of file
readWord(C,[]):- member(C,[10,32]), !. % newline or white space marks end of word
readWord(Char,[Char|W]):- get_code(Char1), readWord(Char1,W), !.
%========================================================================================
