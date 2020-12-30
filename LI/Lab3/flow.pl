symbolicOutput(0).  % set to 1 to see symbolic output only; 0 otherwise.

%% INPUT

:- include(entradaFlow2).




%% AUX FUNCTIONS
coord(X) :- size(Y), between(1,Y,X). % coordenada
board(X,Y) :- coord(X), coord(Y). % tauler
clr(C) :- c(C,_,_,_,_). % color
ini(X,Y) :- c(_,X,Y,_,_). % posicio inicial
fin(X,Y) :- c(_,_,_,X,Y). % posicio final

neighbor(X,Y,Z,Y) :- X is Z+1, !.
neighbor(X,Y,Z,Y) :- X is Z-1, !.
neighbor(X,Y,X,W) :- Y is W+1, !.
neighbor(X,Y,X,W) :- Y is W-1, !.




%%%%%%  1. SAT Variables:
satVariable( color(X,Y,C) ) :- board(X,Y), clr(C).

% Variables auxiliars
satVariable( next(X,Y,Z,W) ) :- board(X,Y), board(Z,W), neighbor(X,Y,Z,W). % (X,Y) -> neighbor (Z,W)
satVariable( conn(X,Y,A,B) ) :- board(X,Y), board(A,B), ini(A,B). % (X,Y) -> ini (A,B)
satVariable( nextC(X,Y,Z,W,C) ) :- board(X,Y), board(Z,W), neighbor(X,Y,Z,W), clr(C). % color(X,Y,C) ^ color(Z,W,C)




%%%%%%  2. Clause generation:       %RESTRICCIONS
writeClauses :- 
    initNextC,                  % init variable auxiliar NextC
    initColor,                  % cada casella de l'entrada és del color corresponent
    initConnIni,                % cada casella inicial està connectada a ella mateixa
    initConnFin,                % cada casella final està connectada a l'inicial del seu color
    filledBoardClr,             % cada casella té un únic color
    filledBoardCon,             % cada casella està connectada a una única casella inicial
    maxNext,                    % cada casella té un únic successor (excepte l'última que no en té)
    maxPrev,                    % cada casella té un únic predecessor (excepte la primera que no en té)
    chainConn,                  % transició de connexions
    chainColor,                 % cada casella té el mateix color que el seu successor
    true, !.                    % this way you can comment out ANY previous line of writeClauses
writeClauses :- told, nl, write('writeClauses failed!'), nl, nl, halt.



initNextC :-
    board(X,Y), 
    board(Z,W), 
    neighbor(X,Y,Z,W), 
    clr(C), 
    expressAnd(nextC(X,Y,Z,W,C), [color(X,Y,C), color(Z,W,C)]), fail.
initNextC.

initColor :- 
    board(X,Y), 
    clr(C), 
    (c(C,X,Y,_,_);
    c(C,_,_,X,Y)), writeClause([color(X,Y,C)]), fail.
initColor.

initConnIni :- 
    board(X,Y), 
    ini(X,Y), 
    writeClause([conn(X,Y,X,Y)]), fail.
initConnIni.


filledBoardClr :- 
    board(X,Y), 
    findall(color(X,Y,C), clr(C), Lits), 
    exactly(1,Lits), fail.
filledBoardClr.

filledBoardCon :- 
    board(X,Y), 
    findall(conn(X,Y,A,B), 
    (board(A,B), ini(A,B)), Lits), 
    exactly(1,Lits), fail.
filledBoardCon.

maxNext :- 
    board(X,Y), 
    maxNextAux(X,Y), fail.
maxNext.

maxNextAux(X,Y) :- 
    fin(X,Y), !, 
    board(Z,W), 
    neighbor(X,Y,Z,W), 
    writeClause([-next(X,Y,Z,W)]).
maxNextAux(X,Y) :- 
    findall(next(X,Y,Z,W), 
    (board(Z,W), 
    neighbor(X,Y,Z,W)), Lits), 
    exactly(1,Lits).

maxPrev :- 
    board(X,Y), 
    maxPrevAux(X,Y), fail.
maxPrev.

maxPrevAux(X,Y) :- 
    ini(X,Y), !, 
    board(Z,W), 
    neighbor(X,Y,Z,W), 
    writeClause([-next(Z,W,X,Y)]).
maxPrevAux(X,Y) :- 
    findall(next(Z,W,X,Y), 
    (board(Z,W), neighbor(X,Y,Z,W)), Lits), 
    exactly(1,Lits).

% if next(X,Y,Z,W) -> ~next(Z,W,X,Y)
% Sembla que amb la resta de condicions aquesta no cal
repeatedNext :- 
    board(X,Y), 
    board(Z,W), 
    neighbor(X,Y,Z,W), 
    writeClause([-next(X,Y,Z,W), -next(Z,W,X,Y)]), fail.
repeatedNext.

% Si conn(X,Y,A,B) ^ next(X,Y,Z,W) -> conn(Z,W,A,B)
chainConn :- 
    board(X,Y), 
    board(Z,W), 
    neighbor(X,Y,Z,W), 
    board(A,B), 
    ini(A,B), 
    writeClause([-conn(X,Y,A,B), -next(X,Y,Z,W), conn(Z,W,A,B)]), fail.
chainConn.

chainColor :- 
    board(X,Y), 
    board(Z,W), 
    neighbor(X,Y,Z,W), 
    findall(nextC(X,Y,Z,W,C), clr(C), Lits), 
    writeClause([-next(X,Y,Z,W)|Lits]), fail.
chainColor.


%%%%%%  3. DisplaySol: show the solution. Here M contains the literals that are true in the model:

% Custom displaySol per veure colors i posicions
displaySol2(M) :- displayAux1(M), displayAux2(M), fail.
displaySol2(_).

displayAux1(M) :- nl, write('Colors: '), nl, board(X,Y), clr(C), member(color(X,Y,C), M), write(X), write(' '), write(Y), write(' -> '), write(C), nl, fail.
displayAux1(_).

% Display sol oficial (comentar linia displaySol2)
displaySol(_):- nl,nl, write('Input:   '), coord(X), nl, coord(Y), writeInputSq(X,Y), fail. 
displaySol(M):- nl,nl, write('Solution:'), coord(X), nl, coord(Y),
		member(color(X,Y,Color),M), setColor(Color), write(' o'), fail. 
%displaySol(M) :- resetColor, !, displaySol2(M).
displaySol(_):- resetColor, !.

writeInputSq(X,Y):- c(Color,X,Y,_,_), setColor(Color), write(' o'), !.
writeInputSq(X,Y):- c(Color,_,_,X,Y), setColor(Color), write(' o'), !.
writeInputSq(_,_):- resetColor, write(' ·'), !.

setColor(Color):- colorCode(Color,Code), put(27), write('[0;38;5;'), write(Code), write('m'), !.
resetColor:- put(27), write('[0m'), !.

colorCode( blue,       69  ).
colorCode( brown,      138 ).
colorCode( red,        196 ).
colorCode( cyan,       51  ).
colorCode( green,      46  ).
colorCode( yellow,     226 ).
colorCode( pink,       201 ).
colorCode( violet,     90  ).
colorCode( orange,     208 ).
colorCode( darkblue,   21  ).
colorCode( darkgreen,  28  ).
colorCode( darkred,    88  ).
colorCode( darkcyan,   30  ).
colorCode( white,      15  ).
colorCode( grey,       8   ).


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
