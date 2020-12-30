%unPaso(EstadoAcual, EstadoFinal )
% unPaso([_,Y],[5,Y]).
% unPaso([X,_],[X,8]).

% unPaso([_,Y],[0,Y]).
% unPaso([X,_],[X,0]).

% unPaso([X,Y],[XF,YF]):- S is X+Y, YF is min(S,8), A is 8-Y, R is X-A, XF is max(0,R).
% unPaso([X,Y],[XF,YF]):- S is X+Y, XF is min(S,5), A is 5-X, R is Y-A, YF is max(0,R).  

compleix([M1F,C1F,M2F,C2F]) :-  S1 is M1F+M2F , S1=3 , S2 is C1F + C2F, S2= 3 .

%anada
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):- M2F is M2 + 2, M1F is M1-2, C1F is C1, C2F is C2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):- C2F is C2 + 2, C1F is C1-2, M1F is M1, M2F is M2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):- M2F is M2 + 1, M1F is M1-1, C1F is C1, C2F is C2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):- C2F is C2 + 1, C1F is C1-1, M1F is M1, M2F is M2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):- C2F is C2 + 1, M2F is M2+1, C1F is C1-1, M1F is M1-1,M1F>=C1F ,M2F>=C2F,compleix([M1F,C1F,M2F,C2F]).
%tornada
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):-  M2F is M2 - 2, M1F is M1+2, C1F is C1, C2F is C2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):-  C2F is C2 - 2, C1F is C1+2, M1F is M1, M2F is M2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):-  M2F is M2 - 1, M1F is M1+1, C1F is C1, C2F is C2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):-  C2F is C2 - 1, C1F is C1+1, M1F is M1, M2F is M2, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).
unPaso([M1,C1,M2,C2],[M1F,C1F,M2F,C2F]):-  C2F is C2 - 1, M2F is M2-1, C1F is C1+1, M1F is M1+1, M1F>=C1F ,M2F>=C2F, compleix([M1F,C1F,M2F,C2F]).




camino( E,E, C1, C2):- reverse(C1,C2).
%camino(E,E,C,C).
camino( EstadoActual, EstadoFinal, CaminoHastaAhora, CaminoTotal ):-
   unPaso( EstadoActual, EstSiguiente ),
   \+member(EstSiguiente,CaminoHastaAhora),
   camino( EstSiguiente, EstadoFinal, [EstSiguiente|CaminoHastaAhora], CaminoTotal ).



solucionOptima:-
   nat(N),                        % Buscamos soluci ́on de "coste" 0; si no, de 1, etc.
   camino([3,3,0,0],[0,0,3,3],[[3,3,0,0]],C), 
   length(C,N),                   % -el coste es la longitud de C.
   %reverse(C,CR),
   write(C), write(N).
    %write(CR).


nat(0).
nat(N):- nat(N1), N is N1 + 1.