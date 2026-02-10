import pytest
from lib.todo_search import todo_search

def test_returns_true_for_todo():
    result = todo_search('#TODO by milk')
    assert result == True

def test_returns_false_for_no_TODO():
    result = todo_search('drink tea')
    assert result == False

def test_throws_error_if_not_passed_a_string():
    with pytest.raises(TypeError) as error:
        todo_search(2)
    error_message = str(error.value)
    assert error_message == 'Entry must be a string'