'''
The Jaccard coefficient measures similarity between finite sample sets, and is defined as the size of the intersection
divided by the size of the union of the sample sets:

J(A, B) = | intersection(A, B) | / | union(A, B) |

Implement a function "jacquard" that measures the similarity of two texts, where each text is represented as a string. For the computation of the jacquard index, you should represent the texts as sets (i.e., you should ignore number of times a specific word occurs in the text). The function s.split() might be useful, see the other exercise (tty.py).

2 Points.
'''


lorem_ipsum_1 = '''Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'''

lorem_ipsum_2 = '''Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. '''

def jacquard(text1, text2):
    a = set(text1.split(" "))
    b = set(text2.split(" "))
    c = a.intersection(b)
    return float(len(c)/(len(a)+len(b)-len(c)))

if __name__ == '__main__':
    print(jacquard(lorem_ipsum_1, lorem_ipsum_2))
