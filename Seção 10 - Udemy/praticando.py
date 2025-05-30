# 🟡 Ex. 2 – Conversor de notas
# Peça ao usuário uma nota entre 0 e 10.
# Trate:
# - Entrada que não seja número
# - Nota fora do intervalo permitido
# Diga se o aluno foi aprovado (nota >= 7).
# Use try/except/else/finally.

def verificar_nota():
    while True:
        try:
            nota = float(input('Digite a nota do aluno(a) (0 a 10): '))
            if nota < 0 or nota > 10:
                print('❌ Nota fora do intervalo permitido.')
            elif nota >= 7:
                print('✅ Aluno aprovado!')
                break
            else:
                print('❌ Aluno reprovado.')
                break
        except ValueError:
            print('❌ Erro! Digite um número válido.')
        finally:
            print('--- Fim da verificação ---')

verificar_nota()

# 🔵 Ex. 4 – Simulador de login com tentativas
# Simule um login com usuário e senha.
# A senha correta é "python123".
# O usuário tem 3 tentativas.
# Trate qualquer erro de input.
# Mostre mensagens claras no else e finally.

tentativas = 0

while True:
    try:
        senha = input('Digite a sua senha: ')
        tentativas += 1
        if tentativas > 3:
            print('Usuario bloqueado!')
            break
        elif senha == 'python123':
            print('Login efetuado com sucesso!')
            break
        elif senha != 'python123':
            print('Senha incorreta!')
    except:
        print('Erro!!!')

    finally:
        print('Programa finalizado!')


# 🟣 Ex. 5 – Calculadora com tratamento de erros
# Peça ao usuário dois números e uma operação (+, -, *, /).
# Execute a operação e mostre o resultado.
# Trate os possíveis erros:
# - Entrada inválida (ex: letras ao invés de números)
# - Divisão por zero
# Use try/except/else/finally

def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2
        else:
            print("❌ Operação inválida.")
            return

    except ValueError:
        print("❌ Entrada inválida! Digite apenas números.")
    except ZeroDivisionError:
        print("❌ Erro! Divisão por zero não é permitida.")
    else:
        print(f"✅ Resultado: {resultado}")
    finally:
        print("--- Cálculo finalizado ---")

calculadora()

