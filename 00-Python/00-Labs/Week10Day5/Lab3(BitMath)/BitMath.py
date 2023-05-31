def SET_BIT(Var,Bit):
	Var = int(Var)
	Bit = int(Bit)
	Var |=(1<<Bit)
	return Var
def CLEAR_BIT(Var,Bit):
	Var = int(Var)
	Bit = int(Bit)
	Var &=~(1<<Bit)
	return Var

def Toggle_Bit(Var,Bit):
	Var = int(Var)
	Bit = int(Bit)
	Var ^=(1<<Bit)
	return Var

def Get_Bit(Var,Bit):
	Var = int(Var)
	Bit = int(Bit)
	return ((Var>>Bit)&1)
	

Reg = 5

print(SET_BIT(Reg,1))
print(CLEAR_BIT(Reg,1))
print(Toggle_Bit(Reg,1))
print(Get_Bit(Reg,1))
