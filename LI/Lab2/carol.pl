
prod([], 1).
prod([X|L], P) :- prod(L, P1), P is X*P1.


%3
pescalar(L1, L2, _) :- length(L1, N1), length(L2, N2), N1 \= N2, !, fail.
%pescalar([], _, _), !.
%pescalar(_, [], _), !. 
pescalar([], [], 0).
pescalar([X|L1], [Y|L2], P) :- pescalar(L1, L2, P1), P is X*Y + P1.

%4
interseccion([], _, []).
interseccion(_, [], []).
interseccion([], [], []).
interseccion([X|L1], L2, [X|L3]) :- member(X, L2), interseccion(L1, L2, L3).
interseccion([X|L1], L2, L3) :- \+member(X, L2), interseccion(L1, L2, L3).

%4
union([],L,L).
union([X|L1], L2, L3) :- member(X,L2), !, union(L1,L2,L3).
union([X|L1], L2, [X|L3]) :- union(L1, L2, L3).

%5
ultimo(L,X) :- append(_, [X],L).

inverso([], []).
inverso(L, [X|L1]) :- append(L2,[X],L), inverso(L2, L1).

%6
fib(0, 1).
fib(1, 1).
fib(2, 1).
fib(N, F) :- N1 is N-1, N2 is N-2, fib(N1, F1), fib(N2, F2), F is F1+F2.

%7
dados(0, 0, []).
dados(P, N, [X|L]) :-
	P>0,
	N<0,
	perm(X, [1, 2, 3, 4, 5, 6]),
	Q is P-X,
	M is N-1, dados(Q, M, L).

%perm2
perm2(X, L, R) :- append(L1, [X|L2], L), append(L1, L2, R).

suma([], 0).
suma([X|L], S) :- suma(L, S1), S is S1+X.

%8
suma_demas(L) :- perm2(X, L, R), suma(R, X), !.

%9
suma_ants(L) :- append(L1, [X|_], L), suma(L1, X), !.

%10
car([], []).
car([X|L], [[X, M]|Cr]) :-  car(L, C), perm2([X,N], C, Cr), !, M is N+1.
car([X|L], [[X, 1]|C]) :- car(L, C).
car(L) :- car(L,C), write(C).

%11
esta_ordenada([]).
esta_ordenada([_]) :- !.
esta_ordenada([X,Y|L]) :- X =< Y, esta_ordenada([Y|L]).

%perm3
perm3([], []).
perm3(L, [X|P]) :- perm2(X, L, R), perm3(R, P).

%12
ordenacion(L1, L2) :- perm3(L1, L2).

%14
insercion(X, [], [X]).
insercion(X, [Y|L], [X, Y|L]) :- X =< Y, !.
insercion(X, [Y|L], [Y|L1]) :- insercion(X, L, L1).

ordenacion2([], []).
oredenacion2([X|L], L1) :- ordenacion2(L, L2), insercion(X, L2, L1).

%15 ¿Qué número de comparaciones puede llegar a hacer en el caso peor el algoritmo de ordenación basado en la inserción?

% 1 + 2 + .. + n-1 = (n*(n-1))/2

%16
split([], [], []).
split([A], [A], []).
split([A, B|R], [A|R1], [B|R2]) :- split(R, R1, R2).

mergesort([], []) :- !.
mergesort([L], [L]) :- !.
mergesort(L, R) :- split(L, L1, L2), mergesort(L1, L1s), mergesort(L2, L2s), merge(L1s, L2s, R).

merge(L, [], L) :- !.
merge([], L, L) :- !.
merge([L1|Ll1], [L2|Ll2], [L1|R]) :- L1 =< L2, !, merge(Ll1, [L2|Ll2], R).
merge([L1|Ll1], [L2|Ll2], [L2|R]) :- merge([L1|Ll1], Ll2, R).

%17
diccionario(A, N) :- nmembers(A, N, S), escribir(S), fail.

nmembers(_, 0, []) :- !.
nmembers(L, N, [X|S]) :- perm(X, L), N1 is N-1, nmembers(L, N1, S).

escribir([]) :- write(' '), nl, !.
escribir([X|L]) :- write(X), escribir(L).


%18
%setof para sacar las repeticiones
palindromos(L) :- setof(L2, (perm(L, L2), es_palindromo(L2)), R), write(R). %perm

es_palindromo([]).
es_palindromo([L|L1]) :- lastElement(L1, Last), Last = L, append(Nlist, [_], L), es_palidromo(Nlist).

%19
suma([], [], [], C, C).
suma([X1|L1], [X2|L2], [X3|L3], Cin, Cout) :-
	X3 is (X1 + X2 + Cin) mod 10,
	C is (X1 + X2 + Cin) // 10,
	suma(L1, L2, L3, C, Cout).

mas_dinero :-
	
	L = [S, E, N, D, M, O, R, Y, _, _],
	perm(L, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
	suma([D, N, E, S], [E, R, O, M], [Y, E, N, O], 0, M),

	write('S = '), write(S), nl,
	write('E = '), write(E), nl,
	write('N = '), write(N), nl,
	write('D = '), write(D), nl,
	write('M = '), write(M), nl,
	write('O = '), write(O), nl,
	write('R = '), write(R), nl,
	write('Y = '), write(Y), nl,
	write('  '), write([S,E,N,D]), nl,
	write('  '), write([M,O,R,E]), nl,
	write('-------------------'), nl,
	write([M,O,N,E,Y]), nl.

mas_dinero_2 :-
	
	L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	perm2(M, [0, 1], _),
	perm2(M, L, L0),
	perm2(O, L0, L1),
	perm2(R, L1, L2),
	perm2(Y, L2, L3),
	perm2(S, L3, L4),
	perm2(E, L4, L5),
	perm2(N, L5, L6),
	perm2(D, L6, _),
	suma([D, N, E, S], [E, R, O, M], [Y, E, N, O], 0, M),


	write('S = '), write(S), nl,
	write('E = '), write(E), nl,
	write('N = '), write(N), nl,
	write('D = '), write(D), nl,
	write('M = '), write(M), nl,
	write('O = '), write(O), nl,
	write('R = '), write(R), nl,
	write('Y = '), write(Y), nl,
	write('  '), write([S,E,N,D]), nl,
	write('  '), write([M,O,R,E]), nl,
	write('-------------------'), nl,
	write([M,O,N,E,Y]), nl.


	
%21



