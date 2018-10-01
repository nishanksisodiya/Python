class triangles:
    sides=3
    def __init__(self,a1,a2,a3):
        self.a1=int(a1)
        self.a2=int(a2)
        self.a3=int(a3)

    def check_angles(self):
        sum=self.a1 + self.a2 + self.a3
        if(sum==180):
            return True
        else:
            return False

def main():
    a1=input()
    a2=input()
    a3=input()
    tri=triangles(a1,a2,a3)
    if(tri.check_angles()):
        print(tri.sides)
    else:
        print("Given angles dont form a triangle")

main()
