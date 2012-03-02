import gzip2, gzip
from cStringIO import StringIO

def test_write_read2():
    """Test write with gzip and read with gzip2."""
    buf = StringIO()
    f = gzip.GzipFile(fileobj=buf, mode="w")
    f.write("hello")
    f.close()
    
    buf.seek(0)
    f = gzip2.GzipFile(fileobj=buf)
    assert f.read() == "hello"
    
def test_write2_read():
    """Test write with gzip2 and read with gzip."""
    buf = StringIO()
    f = gzip2.GzipFile(fileobj=buf, mode="w")
    f.write("hello")
    f.close()
    
    buf.seek(0)
    f = gzip.GzipFile(fileobj=buf)
    assert f.read() == "hello"

def test_members():
    """Test write multiple members with gzip2 and read with gzip."""
    buf = StringIO()
    f = gzip2.GzipFile(fileobj=buf, mode="w")
    f.write_member("hello")
    f.write_member("world")
    f.close()

    buf.seek(0)
    f = gzip.GzipFile(fileobj=buf)
    assert f.read() == "helloworld"
    
    buf.seek(0)
    f = gzip2.GzipFile(fileobj=buf)
    assert f.read() == "helloworld"

    buf.seek(0)
    f = gzip2.GzipFile(fileobj=buf)
    assert f.read_member() == "hello"
    assert f.read_member() == "world"
    