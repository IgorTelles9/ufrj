(* Recebe um inteiro e uma lista de inteiro. Retorna 
    uma lista com todos os elementos da lista anterior
    que são menores que o inteiro informado 
    na chamada função.
*)

fun menores (e, nil) = nil
    | menores (e, list) = 
        if hd(list) < e then hd(list) :: menores(e, tl(list))
        else menores (e, tl(list));
