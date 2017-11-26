def assertIn(v, c):
  if not v in c:
    raise AssertionError('{} not in {}'.format(v, c))

def assertNin(v, c):
  if v in c:
    raise AssertionError('{} in {}'.format(v, c))

def assertEq(l, r):
  if l != r:
    raise AssertionError('{} != {}'.format(l, r))

def assertNeq(l, r):
  if l == r:
    raise AssertionError('{} == {}'.format(l, r))

def assertGt(l, r):
  if l <= r:
    raise AssertionError('{} <= {}'.format(l, r))

def assertGe(l, r):
  if l < r:
    raise AssertionError('{} < {}'.format(l, r))

def assertLt(l, r):
  if l >= r:
    raise AssertionError('{} >= {}'.format(l, r))

def assertLe(l, r):
  if l > r:
    raise AssertionError('{} > {}'.format(l, r))

def assertIsInstance(v, t):
  if not isinstance(v, t):
    raise AssertionError('{} is not instance of {}'.format(v, t))

def assertNisInstance(v, t):
  if isinstance(v, t):
    raise AssertionError('{} is instance of {}'.format(v, t))

def assertThrow(f, E):
  try:
    f()
  except E:
    return
  except:
    raise AssertionError('{} didn\'t raised {}'.format(f, E))
  raise AssertionError('{} didn\'t raised'.format(f))

def assertNoThrow(f):
  try:
    f()
  except:
    raise AssertionError('{} raised'.format(f))

# Tests.
if __name__ == "__main__":

  def check(f, *args):
    try:
      f(*args)
      import traceback
      traceback.print_stack()
      exit(1)
    except AssertionError:
      pass

  # In.
  assertIn(3, [3])
  check(assertIn, 3, [])
  # Nin.
  assertNin(3, [])
  check(assertNin, 3, [3])
  # Eq.
  assertEq(3, 3)
  check(assertEq, 3, 4)
  # Neq.
  assertNeq(3, 4)
  check(assertNeq, 3, 3)
  # Gt.
  assertGt(4, 3)
  check(assertGt, 3, 3)
  check(assertGt, 3, 4)
  # Ge.
  assertGe(4, 4)
  assertGe(4, 3)
  check(assertGe, 3, 4)
  # Lt.
  assertLt(3, 4)
  check(assertLt, 3, 3)
  check(assertLt, 4, 3)
  # Le.
  assertLe(3, 3)
  assertLe(3, 4)
  check(assertLe, 4, 3)
  # IsInstance
  assertIsInstance(3, int)
  check(assertIsInstance, 3, str)
  # NisInstance
  assertNisInstance(3, str)
  check(assertNisInstance, 3, int)
  # Throw.
  def do_raise():
    raise Exception('devil')
  assertThrow(do_raise, Exception)
  check(assertThrow, lambda: 3, Exception)
  # NoThrow
  assertNoThrow(lambda: 3)
  check(assertNoThrow, do_raise)
