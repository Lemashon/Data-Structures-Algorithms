"""
write a little function that will verify whether a statement containing brackets--(, [, or {--is
balanced, that is, whether the number of closing brackets matches the number of opening
brackets. It will also ensure that one pair of brackets really is contained in another:
"""

class Stack:
    def check_brackets(statement):
        stack = stack()
        for ch in statement:
            if ch in ('{', '[', '('):
                stack.push(ch)
            if ch in ('}', ']', ')'):
                last = stack.pop()
                
            if last is '{' and ch is '}':
                continue
            elif last is '[' and ch is ']':
                continue
            else:
                return False
            
        if stack.size > 0:
            return False
        else:
            return True
                
    sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
    )

    for s in sl:
        m = check_brackets(s)
        print("{}: {}".format(s, m))
