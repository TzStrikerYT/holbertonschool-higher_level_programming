 #!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
     n_t = [0, 0]
     _t = (tuple_a, tuple_b)
     for i in range(2):
         if (len(_t[0])) > i:
             n_t[i] += _t[0][i]
         if (len(_t[1])) > i:
             n_t[i] += _t[1][i]
     return(n_t[0], n_t[1])
