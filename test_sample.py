import searchNews


def test01():
    assert searchNews.searchFile('OR','Care,Quality,Commission') == '0 1 2 3 4 5 6'


def test02():
    assert searchNews.searchFile('OR','September,2004') == '9'
    
def test03():
    assert searchNews.searchFile('OR','general,population,generally') == '6 8'

def test04():
    assert searchNews.searchFile('AND','Care,Quality,Commission,admission') == '1'


def test05():
    assert searchNews.searchFile('AND','general,population,Alzheimer') == '6'

