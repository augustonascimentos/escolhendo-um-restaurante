from random import choice
import os


def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    os.system('pause')


def case1():
    restpoor = ["ESCADINHA(SABOR DA PASSAGEM)", "VELHO(PORTINHA)", "ÁGUIA", "MIDWAY(GALERIA)", "PODRÃO DO METRÔ"]
    choice1 = choice(restpoor)
    print("VC ESTÁ COM O VALE QUASE ZERADO, ALMOCE NO {}!".format(choice1))


def case2():
    restmed = ["MR. ÔPI(MOURISCO)", "CULINARE", "PREFÁCIO(LIVRARIA)", "LUPULINO"]
    choice2 = choice(restmed)
    print("AINDA ESTÁ SOBRANDO ALGUNS TROCADOS NO SEU VALE, VAMOS ALMOÇAR NO {}!".format(choice2))


def case3():
    restrich = ["OUTBACK", "FIAMMETTA", "EMPÓRIO PAX", "CHURRASCARIA FOGO DE CHÃO", "MIZU"]
    choice3 = choice(restrich)
    print("VC TA RICO, LARGA DE SER MÃO DE VACA E VAI ALMOÇAR NO {}".format(choice3))


def menu():

    rest = str(input("============================\n"
                     "|--SORTEIO DE RESTAURANTES--|\n"
                     "============================\n"
                     "\n"
                     "Digite '1' para restaurantes com preços normais. \n"
                     "Digite '2' para restaurantes com preços médios. \n"
                     "Digite '3' para restaurantes TOP. \n"
                     "\n"))

    if rest != '1' and rest != '2' and rest != '3':
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE.")
        pause()
        clear_screen()
        return menu()

    else:
        if rest == '1':
            case1()
            pause()
            clear_screen()
            return menu()
        if rest == '2':
            case2()
            pause()
            clear_screen()
            return menu()
        if rest == '3':
            case3()
            pause()
            clear_screen()
            return menu()


menu()
