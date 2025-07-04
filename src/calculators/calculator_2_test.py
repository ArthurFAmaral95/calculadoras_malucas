from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
  def __init__(self, body: Dict):
    self.json = body

#criamos essa classe para fazer um teste unitario para avaliar o funcionamento da calculadora
#o retorno da classe pode ser qualquer coisa porque o objetivo é testar a calculadora
class MockDriverHandler():
  def standard_deviation(self, numbers: List[float]) -> float:
    return 3

#do jeito que esta definido não é um teste unitario porque alem de testar o funcionamento da calculadora, testa a integracao com o driver
def test_calculate_integration():
  mock_request = MockRequest({'numbers': [2.12, 4.62, 1.32]})

  driver = NumpyHandler()

  calculator_2 = Calculator2(driver)
  formated_response = calculator_2.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'Calculator': 2, 'result': 0.08}}

#agora é um teste unitario porque não estamos usando o driver de verdade no teste
def test_calculate():
  mock_request = MockRequest({'numbers': [2.12, 4.62, 1.32]})

  driver = MockDriverHandler()

  calculator_2 = Calculator2(driver)
  formated_response = calculator_2.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'Calculator': 2, 'result': 0.33}}

def test_calculate_with_body_error():
  mock_request = MockRequest({'num': [1.84, 8.16, 9.25]})

  driver = NumpyHandler()
  calculator_2 = Calculator2(driver)
  with raises(Exception) as excinfo:
    calculator_2.calculate(mock_request)
  
  assert str(excinfo.value) == 'body mal formatado'