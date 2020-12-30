
%%Carolina Middel Soria

%%%%%% Input:
numEquipos(16).
nofuera(7,10).
nofuera(6,10).
nofuera(9,10).
nofuera(10,10).
nofuera(11,10).
nofuera(7,30).
nofuera(6,30).
nofuera(9,30).
nofuera(10,30).
nofuera(11,30).
nocasa(7,1).
nocasa(8,1).
nocasa(9,1).
nocasa(10,1).
nocasa(11,1).
nocasa(12,1).
norepes(1,2).
norepes(2,3).
norepes(28,29).
norepes(29,30).
nopartido(1,2,30).
nopartido(1,2,1).
nopartido(1,2,2).
nopartido(1,2,3).
nopartido(1,2,4).
nopartido(1,2,5).
nopartido(1,2,6).
nopartido(1,2,7).
sipartido(2,3,30).
sipartido(4,5,30).

%%%%%% Some helpful definitions to make the code cleaner:
equip(N) :- numEquips(M), between(1, M, N).
equipsdiferents(I, J) :- equip(I), equip(J), I /= J.
jornada(N) :- numEquips(M), K is (M-1)*2, between(1, K, N).
jornadesConsecutives(K1, K2) :- jornada(K1), K2 is K1+1, jornada(K2).
jornadesComplementaries(K1, K2):- K1 < numEquipos, jornada(K1), K2 is K1+numEquipos-1, jornada(K2).
3equipsdiff (I, J, K):- equip(I), equip(J), equip(K), I\=J, I\=K.



%%%%%%  1. SAT Variables:
% p (K, I, J) significa que en la jornada K l'equi I juga contra l'equip J (a casa I).
satVariable( p(K, I, J) ) :-  jornada(K), equip(I), equip(J).

%%%%%%  2. Clause generation:

writeClauses :-
 %% - un equip mai juga contra si mateix
contraellmateix,
 %% - els partits tenen lloc una sola vegada
 unpartitpercampionat,
 %% - un equip només juga un partit en cada jornada

 %% - es respecta el mateix ordre a la segona volta
  segonavolta,
 %restriccions adicionals
 %–el equipo i no quiere jugar en casa la jornada j,
 %–el equipo i sı́ quiere jugar en casa la jornada j,
 %–en las jornadas i e i + 1 no se admiten repeticiones: dos partidos seguidos en casa, o dos partidos seguidos fuera,
 %–el partido i-i 0 (es decir, en casa del equipo i) no debe ser la jornada j
 %–el partido i-i 0 (es decir, en casa del equipo i) sı́ debe ser la jornada j.
 
 %+ relacions partit I-J una jornada K
 %+ relacionades amb un equip I i una jornada K
 %+ relacionades amb 2 jornades jornadesConsecutives K i K+1
 %+ triplets
 
 
 
writeClauses :- told, nl, write('writeClauses failed!'), nl, nl, halt.

contraellmateix :- jornada(K), equip(I), writeClause([-p(K,I,I)]), fail.
contraellmateix.

unpartitpercampionat :- equipsdiferents(I, J), findall(p(K, I, J), jornada(K), Lits), exactly(1, Lits), fail.
unpartitpercampionat.

partitperjornada :- equip(I), jornada(K), findall(p(K, I, J), equip(J), Lits), findall(p(K,J,I), equip(J), Lits1), append(Lits, Lits1, Lits

segonavolta :- jornada(K1), jornadesComplementaries(K1, K2), equipsdiferents(I, J), writeClause([-p(K1, I, J), p(K2, J, I)]), fail.
segonavolta.

notriplets :- 3equipsdiffs(I, J, N), jornada(K)writeClause([-p(


%%%%%%  3. DisplaySol: show the solution. Here M contains the literals that are true in the model:


displaySol(M):- nl, jornada(K), write('Jornada '), write(K), nl,
findall(I-J, member(partit(K,I,J),M), L), member(I-J, L), write(I), write(' - '), write(J),
nl, fail.

displaySol(M):- nl, equip(I), write('Partits del equip '), write(I), nl,
findall(K-J, member(partit(K,I,J),M), L), member(K-J, L), write('Jornada '), write(K), write(': '), write(J), nl, fail.

displaySol(_):- nl.


























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
