class Scalar:

    def check_lerp(self, u, v, t):
        if (type(u) != int and type(u) != float) or (type(v) != int and type(v) != float) or (type(t) != int and type(t) != float):
            raise TypeError("Result is undefined")

    def lerp(self, u, v, t):
        self.check_lerp(u,v,t)
        return u + t * (v-u)