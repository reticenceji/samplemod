# -*- coding: utf-8 -*-
from .context import src
import pytest

def test_thoughts():
    assert src.add(1,1)==2

def test_raises():
    with pytest.raises(ZeroDivisionError) as e:
        1/0
        
    
