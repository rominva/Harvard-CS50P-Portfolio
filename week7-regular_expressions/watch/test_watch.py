from watch import parse

def test_default():
    s1 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(s1) == "https://youtu.be/xvFZjo5PgG0"

    s2 = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(s2) == "https://youtu.be/xvFZjo5PgG0"

    s3 = '<iframe width="560" height="315" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen> src="https://www.youtube.com/embed/xvFZjo5PgG0"</iframe>'
    assert parse(s3) == "https://youtu.be/xvFZjo5PgG0"

    s4 = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(s4) == "https://youtu.be/xvFZjo5PgG0"

    s5 = '<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(s5) == "https://youtu.be/xvFZjo5PgG0"


def test_invalidformat():
    s = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    assert parse(s) == None

    s2 = '<iframe width="560" height="315" src="www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(s2) == None

    s3 = "<iframe 'https://www.youtube.com/embed/xvFZjo5PgG0'></iframe>"
    assert parse(s3) == None

    s4 = '<iframe src="https://www.youtube.com/xvFZjo5PgG0"></iframe>'
    assert parse(s4) == None

    s5 = '<iframe src="https://www.youtube/embed/xvFZjo5PgG0"></iframe>'
    assert parse(s5) == None