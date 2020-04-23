#Łukasz Stachoń
#zadanie 2
#żołmierzy sortujemy merge sortem, odwracamy tablię a następnie a następni wycinamy z niej podane indeksy
#złożoność czasowa - mergesort (O nlog(n)), odwrócenie tablicy O(n/2) całość algorytmu ma złożoność O(nlog(n))
#opcjonalnie można zastosować algorytm quickselect do wybierania k-tego najmneijszego elementu nieposortowanej tablicy(średnia złożoność O(n), jednak najgorsza o(N^2)

def znajdz_srodek(A):
    a = len(A) / 2
    a = int(a)
    return a

# funkcja łącząca dwie posorotwane tablice w jedną posortowaną
def merge(A, B):
    a = 0
    b = 0
    posortowana_lista = []
    if A == None or len(A) == 0:
        return B
    if B == None or len(B) == 0:
        return A
    while a != len(A) and b != len(B):
        if A[a] <= B[b]:
            posortowana_lista.append(A[a])
            a += 1
        else:
            posortowana_lista.append(B[b])
            b += 1
    while a != len(A):
        posortowana_lista.append(A[a])
        a += 1
    while b != len(B):
        posortowana_lista.append(B[b])
        b += 1
    return posortowana_lista

#główna funckja sortująca
def mergesort(A, start, koniec):
    if (len(A) > 1):
        mid = znajdz_srodek(A)
        tab_lewa = mergesort(A[:mid], start, mid)
        tab_prawa = mergesort(A[mid:], mid + 1, koniec)

        posortowana_tab = merge(tab_lewa, tab_prawa)
        return posortowana_tab
    return A

def odwroc_tab(T):
    i = 0
    k = len(T)-1

    while i < k:
        T[i],T[k]=T[k],T[i]
        i+=1
        k-=1
    return T

def section(T,p,q):
    if p > q:
        return []

    wynik = [0] * ((q - p)+1)
    posortowana = mergesort(T,0,len(T))
    posortowana = odwroc_tab(posortowana)
    print(posortowana)

    j = 0
    for i in range(p, q+1):
        print(i)
        wynik[j] = posortowana[i]
        j+=1

    return wynik



T = [7,9,2,4,8, 8, 8]

T = section(T,1,3)
print(T)