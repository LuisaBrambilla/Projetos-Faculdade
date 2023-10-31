import System.IO

-- Questão 01: Construa um código que receba o tamanho do raio de uma pizza em centímetros
-- e o número de pessoas que irão compartilhar a pizza e retorne a área em centímetros 
-- quadrados que cada um tem direito.

areaPizza :: Float -> Float
areaPizza raio = pi * (raio ** 2)

areaPessoa :: Float -> Float -> Float
areaPessoa area pessoa = area / pessoa

-- Questão 02: Solicitar a idade de uma pessoa em anos e retorne a idade em dias.

convDia :: Int -> Int
convDia anos = anos * 365

-- Questão 03: Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32),leu um valor de temperatura em Fahrenheit e exibi-lo em Celsius.

fahrenheitParaCelsius :: Double -> Double
fahrenheitParaCelsius fahrenheit = (5/9) * (fahrenheit - 32)

-- Questão 04: Converter um inteiro informado menor que 32 para sua representação em binário.

decimalBinario :: Int -> String
decimalBinario n
  | n < 2 = show n
  | otherwise = decimalBinario (n `div` 2) ++ show (n `mod` 2)

-- Questão 05: Dado o tamanho de um arquivo em bytes e a velocidade de transferência de dados
-- de uma conexão de internet em megabits por segundo, construa um código que calcule o
-- tempo necessário para transferir o arquivo

tempoTransferencia :: Int -> Float -> Float
tempoTransferencia tamanhoArquivo velocidadeMbps =
    (fromIntegral (tamanhoArquivo * 8)) / (velocidadeMbps * 1e6)

-- Questão 06: Escreva uma função recursiva em Haskell chamada `somaPares` que recebe uma
-- lista de números inteiros e retorna a soma dos números pares na lista. Utilize recursividade
-- para implementar esta função.

somaPares :: [Int] -> Int
somaPares [] = 0
somaPares (x:xs)
    | even x = x + somaPares xs
    | otherwise = somaPares xs

-- Questão 07: Agora, escreva uma função recursiva em Haskell chamada `fibonacci` que recebe
-- um número inteiro `n` e retorna o n-ésimo termo da sequência de Fibonacci. Utilize
-- recursividade para implementar esta função.

fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

-- Questão 08: Escreva uma função recursiva em Haskell chamada
-- `reverterLista` que recebe uma lista de elementos e retorna a lista invertida. Por exemplo,
-- `reverterLista [1, 2, 3, 4]` deve retornar `[4, 3, 2, 1]`. Utilize recursividade para implementar
-- esta função.

reverterLista :: [a] -> [a]
reverterLista [] = []
reverterLista (x:xs) = reverterLista xs ++ [x]

-- Questão 09: Construa um código que aloque um vetor do tipo H, D, E, B, I, F, G, C, A
-- na seguinte árvore binária.

data ArvoreBinaria a = No a (ArvoreBinaria a) (ArvoreBinaria a)
                    | Folha a
                     deriving (Show)

construirArvore :: String -> ArvoreBinaria Char
construirArvore expressao = snd (construirArvore' expressao [])

construirArvore' :: String -> [ArvoreBinaria Char] -> (String, ArvoreBinaria Char)
construirArvore' [] [arvore] = ([], arvore)
construirArvore' (c:cs) pilha
    | c == ' ' = construirArvore' cs pilha 
    | c == '(' = construirArvore' cs pilha 
    | c == ')' = (cs, topo) 
    | c `elem` "+-*/^" = construirArvore' cs (novoNo:pilhaRestante)
    | otherwise = construirArvore' cs (Folha c:pilha)
    where
        pilhaRestante = dropWhile (isOperatorHigherOrEqual c) pilha
        novoNo = head pilhaRestante
        topo = No c (pilhaRestante !! 1) (pilha !! 0)

isOperatorHigherOrEqual :: Char -> ArvoreBinaria Char -> Bool
isOperatorHigherOrEqual op (Folha _) = False
isOperatorHigherOrEqual op (No op' _ _) = precedencia op <= precedencia op'

precedencia :: Char -> Int
precedencia '+' = 1
precedencia '-' = 1
precedencia '*' = 2
precedencia '/' = 2
precedencia '^' = 3
precedencia _ = 0

imprimirArvore :: ArvoreBinaria Char -> String
imprimirArvore (Folha a) = [a]
imprimirArvore (No op esq dir) = "(" ++ imprimirArvore esq ++
    [op] ++ imprimirArvore dir ++ ")"
    
main :: IO ()
main = do
    putStrLn "Digite o raio:"
    raio <- readLn
    putStrLn "Digite a quantidade de pessoas:"
    pessoa <- readLn
    let area = areaPizza raio
        pedaco = areaPessoa area pessoa
    putStrLn ("Área da pizza: " ++ show area)
    putStrLn ("Área que cada pessoa tem direito: " ++ show pedaco)

    putStrLn "Digite a idade em anos:"
    n <- readLn
    let idadeAnos = convDia n
    putStrLn ("Idade em dias: " ++ show idadeAnos)

    putStrLn "Digite a temperatura em Fahrenheit:"
    inputFahrenheit <- getLine
    let fahrenheit = read inputFahrenheit :: Double
        celsius = fahrenheitParaCelsius fahrenheit
    putStrLn ("A temperatura em Celsius é: " ++ show celsius)

    putStrLn "Digite o número menor que 32:"
    numero <- readLn
    let binario = decimalBinario numero
    putStrLn ("Representação binária: " ++ binario)

    putStrLn "Digite o tamanho do arquivo em bytes:"
    tamanhoArquivo <- readLn
    putStrLn "Digite a velocidade de transferência em megabits por segundo:"
    velocidadeMbps <- readLn
    let tempo = tempoTransferencia tamanhoArquivo velocidadeMbps
    putStrLn ("Tempo necessário para a transferência: " ++ show tempo ++ " segundos")

    putStrLn "Digite a quantidade de números na lista: "
    n <- readLn
    let ordem = [1..n]
        soma = somaPares ordem
    putStrLn ("A lista é " ++ show ordem)
    putStrLn ("A soma dos valores pares é: " ++ show soma)

    putStrLn "Digite um valor para descobrir sua sequência de Fibonacci"
    n <- readLn
    let sequencia = fibonacci n
    putStrLn ("A sequência Fibonacci do número é: " ++ show sequencia)

    putStrLn "Digite a quantidade de números na lista: "
    n <- readLn
    let tamanhoLista = [1..n]
        inverte = reverterLista tamanhoLista
    putStrLn ("A lista é: " ++ show tamanhoLista)
    putStrLn ("A lista invertida é: " ++ show inverte)

    let expressao = "A + ((B + ((D + (H)) (E)) (C + ((F + (I)) (G)))"
        arvore = construirArvore expressao
    putStrLn ("Expressão: " ++ expressao)
    putStrLn ("Árvore: " ++ imprimirArvore arvore)