input = 'ababaaaabb'
k = 3

# pole None jest na podwyraz a 0 to licznik wystąpień danego podwyrazu
tab =[[None,0] for i in range(len(input))]

for i in range(k-1,len(input)):
    a =''
    b = i - k +1
    # tworzymy podwyraz idąc od prawej do lewej
    while b is not i+1:
        a+= input[b]
        b+=1
    flag = 0
    # sprawdzamy czy dany wyraz juz istnieje w tab jesli tak to zwiekszamy jego licznik
    for j in range(k-1,len(input)):
        if tab[j][0] == a:
            tab[j][1]+=1
        # jesli nie to ustawiamy flage na miejsce gdzie ma sie znajdowac
        if tab[j][0] is None and flag is 0:
            flag = j
    # wstawiamy wyraz jesli go nie ma w tab
    if flag is not 0:
        tab[flag][0]=a
        tab[flag][1]+=1


max = -1
sentence =''
#szukamy wyrazu z najwieksza liczba powtorzen i go zapisujemy pod sentence
for i in range(len(tab)):
    if(tab[i][1]> max):
        max = tab[i][1]
        sentence = tab[i][0]


print(tab)
print(sentence)


