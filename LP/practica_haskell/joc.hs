
-- CAROLINA MIDDEL SORIA

-------------------------------------------------------------------------

import System.Random


type Tauler = [[Char]]
type Jugador = Char
type Torn = Bool


-- Per a fer números random (ENUNCIAT)
-------------------------------------------------------------
randInt :: Int -> Int -> IO Int
-- randInt low high is an IO action that returns a
-- pseudo-random integer between low and high (both included).

randInt low high = do
    random <- randomIO :: IO Int
    let result = low + random `mod` (high - low + 1)
    return result
-------------------------------------------------------------


-- imprimir numeros de les columnes del tauler
-------------------------------------------------------------
imprimir_int:: Int -> Int -> IO Int
imprimir_int c n = do
    if (c == n) then do return 1
    else do
        putStr $ show c
        imprimir_int (c+1) n
-------------------------------------------------------------


-- serveix per a treballar les columnes com a llistes
------------------------------------------------------------
transposar_f_c :: Tauler -> Tauler
transposar_f_c ([]:_) = []
transposar_f_c tauler = (map head tauler) : transposar_f_c (map tail tauler)
------------------------------------------------------------



-- Calcula les diagonals del tauler (per obtenir les contraries provar reverse)
------------------------------------------------------------
diagonals_tauler :: Tauler -> Tauler
diagonals_tauler [] = []
diagonals_tauler ([]:xs) = xs
diagonals_tauler tauler = zipWith (++) ([]:(diagonals_tauler (map tail tauler))) (map ((:[]). head) tauler ++ repeat [])
------------------------------------------------------------



-- posicio a la qual ha d'anar la fitxa    
------------------------------------------------------------
buscar_buit :: [Char] -> Int -> Int
buscar_buit [] pos = -1
buscar_buit (x:xs) pos
    | x == '.' = pos
    | otherwise = buscar_buit xs (pos+1)
------------------------------------------------------------
    
    
--busca la posició buida a la qual ha d'anar la fitxa en la columna triada
-----------------------------------------------------------
busca_pos :: Int -> Tauler -> Int
busca_pos _ [] = 0
busca_pos n (x:xs)
    | n == 0 = buscar_buit x 0
    | otherwise = busca_pos (n-1) xs
----------------------------------------------------------
    
    
-- substitueix la nova columna "fila abans de transposar" amb el valor canviat
-----------------------------------------------------------
remplaza :: Jugador -> Int -> [Char] -> [Char] -> [Char]
remplaza _ _ ll [] = reverse ll
remplaza j pos ll (x:xs) 
    | pos == 0 = remplaza j (pos-1) (j:ll) xs
    | otherwise = remplaza j (pos-1) (x:ll) xs
-----------------------------------------------------------

    
-- crea la nova matriu amb el valor canviat
-----------------------------------------------------------
remplaza_mat :: Jugador -> Int -> Int -> Tauler -> Tauler -> Tauler
remplaza_mat _ c pos mat [] = reverse mat
remplaza_mat j c pos mat (x:xs)
    | c == 0 = remplaza_mat j (c-1) pos ((remplaza j pos [] x):mat) xs
    | otherwise = remplaza_mat j (c-1) pos (x:mat) xs
-----------------------------------------------------------
    
    
    
-- comprova quants caràcters seguits d'aquest jugador hi ha
-----------------------------------------------------------
comprova_linia :: [Char] -> Jugador -> Int -> Int -> Int
comprova_linia (_:[]) _ cont _ = cont
--comprova_linia _ _ c n = n
comprova_linia (x:y:xs) j cont n
    | cont == n = n
    |(x == j && y == j) = comprova_linia (y:xs) j (cont+1) n
    |otherwise = comprova_linia (y:xs) j 1 n
-----------------------------------------------------------



-- comprova si algu ha guanyat (per llista)
-----------------------------------------------------------
comprova_guanyador :: Tauler -> Jugador -> Int -> Bool
comprova_guanyador [] _ _ = False
comprova_guanyador (x:xs) j n
    |((comprova_linia x j 1 n) == n) = True
    |otherwise = comprova_guanyador xs j n
-----------------------------------------------------------



-- comprova si algu ha guanyat
-----------------------------------------------------------
comprova_guanyador_h_v_d :: Tauler -> Jugador -> Int -> Bool
comprova_guanyador_h_v_d t j n
    |(comprova_guanyador t j n || comprova_guanyador (transposar_f_c t) j n || comprova_guanyador (diagonals_tauler t) j n || comprova_guanyador (diagonals_tauler (reverse t)) j n) = True
    |otherwise = False
-----------------------------------------------------------

{-
compta_col :: [Char] -> Jugador -> Int -> Int -> Int
compta_col (x:xs) j pos c
    | pos == 0 = c
    | x == j = compta_col xs (pos-1) (c+1)
    | otherwise = compta_col xs (pos-1) c

    
compta_fil_d :: [Char] -> Jugador -> Int -> Int -> Int
compta_fil_d (x:xs) j pos c


compta_f_seguides ::  -> Int -> Jugador -> Int 

compta_fitxes_col :: Tauler -> Jugador -> [Int]
compta_fitxes_col (x:xs) j = (compta_col x j (buscar_buit x 0) 0) ++ compta_fitxes_col xs j


comta_fitxes_fil :: Tauler -> Jugador -> Int
compta_fitxes_fil (x:xs) j = compta_fil ((transposar_f_c (x:xs))!!(buscar_buit (reverse x) 0)) j  
-}


-- comprova que es respectin els limits del tauler
-----------------------------------------------------------
limits :: Tauler -> Int -> Bool
limits t n
    | n > ((length t)-1) || ((t !! n) !! ((length (t !! 0))-1) /= '.') = False
    | otherwise = True
-----------------------------------------------------------



-- comprova si el tauler està ple
-----------------------------------------------------------
tauler_ple :: Tauler -> Bool
tauler_ple [] = True
tauler_ple (x:xs)
    | (x !! (length (x)-1) /= '.') = tauler_ple xs
    | otherwise = False
-----------------------------------------------------------


-- diu si en fer un moviment "imaginari/futur" guanyaràs
-----------------------------------------------------------
gre_guanya :: Tauler -> Jugador -> Int -> Int -> Int
gre_guanya t j cont n
    | cont == ((length t)-1) = -1
    |((busca_pos cont t /= -1) && (comprova_guanyador_h_v_d (remplaza_mat j cont (busca_pos cont t) [] t) j n)) = cont
    |otherwise = gre_guanya t j (cont+1) n
-----------------------------------------------------------



{-
--escriure amb ratlletes?
-----------------------------------------------------------
escriure_tauler :: Tauler -> Tauler -> Char -> Tauler
escriure_tauler [] t _ = t
escriure_tauler (x:xs) t c = escriure_tauler xs ((zip x take (length ((t!!0)-1)) repeat c):t) c
    -}

    
--IA
-----------------------------------------------------------
--RANDOM: cada tirada de l'ordinador és una columna a l'atzar.

--GREEDY: cada tirada de l'ordinador és a la columna que li permet posar en ratlla el nombre més alt de fitxes pròpies i que evita (si pot) que el contrari faci 4-en-ratlla a la jugada següent. En cas d'empat, tria arbitràriament.

--SMART:trieu vosaltres una estratègia el més astuta possible. No hauria de ser massa lenta (un parell de segons màxim per jugada, diguem).


--Random
-----------------------------------------------------------
raandom :: Tauler -> IO Int
raandom tauler = do
    let c = ((length tauler)-1)
    let f = ((length (tauler !! 0))-1)
    r1 <- randInt 0 c
    
    if (((tauler !! r1) !! f) /= '.') then
        raandom tauler
    else return r1
    
-----------------------------------------------------------



--Humà
-----------------------------------------------------------
huma_bugejar :: Tauler -> IO Int 
huma_bugejar tauler = do
    putStrLn "Jugador 2, tria la columna a la qual vols tirar la teva fitxa"
    fitxa <- getLine
    let fit = read fitxa :: Int
    
    if (limits tauler fit) then
        return fit
    else do
        putStrLn "!!!! Moviment il·legal !!!!\n\n"
        huma_bugejar tauler
-----------------------------------------------------------
        
        


--Greedy
-----------------------------------------------------------
greedy :: Tauler -> IO Int
greedy tauler = do
    
    let c = ((length tauler)-1)
    let f = ((length (tauler !! 0))-1)
    r1 <- randInt 0 c
    
    if (((tauler !! r1) !! f) /= '.') then do greedy tauler
    else do
        let j = gre_guanya tauler 'O' 0 4
        print j
        print r1
        if (j /= -1) then return j
        else do
            let k = gre_guanya tauler 'X' 0 4
            print k
            if (k /= -1) then return k
            else do
                let j = gre_guanya tauler 'O' 0 3
                print (busca_pos j tauler)
                print j
                if (j /= -1) then return j
                else do
                    let j = gre_guanya tauler 'O' 0 2
                    print j
                    if (j /= -1) then return j
                    else return r1
------------------------------------------------------------




--Smart
-----------------------------------------------------------
smart :: Tauler -> IO Int
smart tauler = do
    let c = ((length tauler)-1)
    let f = ((length (tauler !! 0))-1)
    r1 <- randInt 0 c
    
    if (((tauler !! r1) !! f) /= '.') then do greedy tauler
    else do
        let j = gre_guanya tauler 'O' 0 4
        if (j /= -1) then return j
        else do
            let k = gre_guanya tauler 'X' 0 4
            if (k /= -1) then return k
            else do
                let j = gre_guanya tauler 'O' 0 3
                if (j /= -1) then return j
                else do
                    let j = gre_guanya tauler 'X' 0 3
                    if (j /= -1) then return j
                    else do 
                        let j = gre_guanya tauler 'O' 0 2
                        if (j /= -1) then return j
                        else return r1
    

-----------------------------------------------------------
-----------------------------------------------------------



-- Main JUGAR
-----------------------------------------------------------
jugar :: Tauler -> Torn -> (Tauler -> IO Int) -> IO Int
jugar tauler t est = do
    
    if (tauler_ple tauler) then do
            putStrLn "Hi ha hagut un empat!"   
            return 1
    else do
        if (t) then do
            
            putStrLn "Jugador 1, tria la columna a la qual vols tirar la teva fitxa:"
            fitxa <- getLine
            let fit = read fitxa :: Int
            
            
            if (limits tauler fit) then do
                return fit
            else do
                putStrLn "!!!! Moviment il·legal !!!!\n\n"
                jugar tauler t est
            
            let pos = busca_pos fit tauler
            let jugada =  remplaza_mat 'X' fit pos [] tauler

                        --imprimir tauler
            ----------------------------------------------------
            let col = (length jugada)
            imprimir_int 0 col
            let linias = take (col) ['_', '_' .. ]
            putStr "\n"
            --putStrLn $ linias
            putStrLn $ unlines $ reverse $ transposar_f_c jugada
            ---------------------------------------------------
            
            if (comprova_guanyador_h_v_d jugada 'X' 4) then do 
                putStrLn " Has guanyat!"
                return 1
            else jugar jugada (not t) est
            
        else do
            fit <- est tauler
            
            let pos = busca_pos fit tauler
            let jugada =  remplaza_mat 'O' fit pos [] tauler
            
            putStrLn "El jugador 2 ha fet el seu moviment: \n"

                
            --imprimir tauler
            ----------------------------------------------------
            let col = (length jugada)
            imprimir_int 0 col
            let linias = take (col) ['_', '_' .. ]
            putStr "\n"
            --putStrLn $ linias
            putStrLn $ unlines $ reverse $ transposar_f_c jugada
            ---------------------------------------------------
            
            
            if (comprova_guanyador_h_v_d jugada 'O' 4) then do 
                putStrLn "Ha guanyat el teu contrincant!"
                return 1
            else jugar jugada (not t) est
-----------------------------------------------------------




--MAIN
-----------------------------------------------------------
main :: IO ()
-- main program that throws two dice.

main = do
    putStrLn "----- BENVINGUT AL 4 EN RATLLA ----- \n"

    putStrLn "Abans de començar a jugar.. \nIntrodueix les files que vols pel tauler:"
    files <- getLine
    putStrLn "Perfecte, ara introdueix les columnes:"
    columnes <- getLine
    
    let f = read files :: Int
    let c = read columnes :: Int
    -- canvio files per columnes per a treballar amb columnes i després transposar
    let tauler = take c (repeat $ take f ['.', '.' .. ])
    
    
    putStrLn "Indica el nivell de dificultat del teu contrincant (indica el número): \n 1. Random -  (fàcil)\n 2. Greedy -  (mitjà)\n 3. Smart  -  (difícil)\n 4. Humà   -  (depèn de la persona ;))"
    
    iA <- getLine
    let ia = read iA :: Int
    
    putStr "Seràs el Jugador 1"
    
    if (ia ==1) then do
        putStrLn ", has triat un nivell pel teu contrincant fàcil \n"
        p <- jugar tauler True raandom
        return ()
    else if (ia == 2) then do
        putStrLn ", has triat un nivell pel teu contrincant mitjà \n"
        p <- jugar tauler True greedy
        return ()
     else if (ia ==3) then do
         putStrLn ", has triat un nivell pel teu contrincant difícil \n"
         p <- jugar tauler True smart
         return ()
        else if (ia ==4) then do 
        p <- jugar tauler True huma_bugejar
        return ()
    else return ()
                    
-----------------------------------------------------------   
