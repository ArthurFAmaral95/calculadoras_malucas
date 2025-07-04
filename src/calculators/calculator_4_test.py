from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
  def __init__(self, body: Dict):
    self.json = body

class MockDriverHandler():
  def mean(self, numbers: List[float]) -> float:
    return 2
  
def test_calculate():
  mock_request = MockRequest({'numbers': [10,20]})

  driver = MockDriverHandler()

  calculator_4 = Calculator4(driver)
  formated_response = calculator_4.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'Calculator': 4, 'result': 2}}

def test_calculate_integration():
  mock_request = MockRequest({'numbers': [10,20]})
  driver = NumpyHandler()

  calculator_4 = Calculator4(driver)
  formated_response = calculator_4.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'Calculator': 4, 'result': 15.0}}

def test_calculate_with_body_error():
  mock_request = MockRequest({'numb': [10,20]})
  driver = MockDriverHandler()
  calculator_4 = Calculator4(driver)

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)
  
  assert str(excinfo.value) == 'body mal formatado'
