from pytest import raises, mark
from codigo.bytebank import Funcionario

class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given (Contexto)
        entrada = '13/03/2000'
        funcionario = Funcionario('teste', entrada, 0)

        # When (ação)
        resultado = funcionario.idade()

        # Then (Desfecho)
        assert resultado == 23

    def test_quando_sobrenome_recebe_Pedro_Henrique_deve_retornar_Henrique(self):
        # Given
        entrada = ' Pedro Henrique '
        funcionario = Funcionario(entrada, '11/11/2000', 0)

        # When
        resultado = funcionario.sobrenome()

        # Then
        assert resultado == 'Henrique'

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        funcionario = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        # When
        funcionario.decrescimo_salario()

        # Then
        assert funcionario.salario == 90000

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given
        entrada_salario = 1000
        funcionario = Funcionario('test', '11/11/2000', entrada_salario)

        # When
        bonus = funcionario.calcular_bonus()

        # Then
        assert bonus == 100

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with raises(Exception):
            # Given
            entrada_salario = 1000000
            funcionario = Funcionario('test', '11/11/2000', entrada_salario)

            # When
            bonus = funcionario.calcular_bonus()

            # Then
            assert bonus
