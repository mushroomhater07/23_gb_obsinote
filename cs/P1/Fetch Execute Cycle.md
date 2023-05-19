# Processor
Control Unit: decodes the program instruction in the CIR, selects machine resources such as a data source register and a required arithmetic operation, and coordinates activation of those resources
Clock
General-Purpose Register: 
	ALU(arithmetic logic unit): Do arthemetic, relation op - : performs mathematical and logical operation
	Accumulator: Register that store the result of ALU
Dedicated Register (all needed in FEC):
	Prog. Counter:an incrementing counter that keeps track of the memory address of which instruction needs to be executed next (holds the address to be fetched)
	Curr. Instruc. Reg:a temporary holding place for the instruction while its being decoded or executed
	MAR:stores the address of the instruction to be read or written
	MBR: two-way register that holds the data that has been fetched from memory or data waiting to be stored in memory
	Status Reg: bits that are set or cleared depending on the result of an instruction (bit for overflow)
# FDE ccycle
## Fetch
causes the next instruction to be fetched from main memory
MAR ← [PC] //*address bus* to main memory
	1.The address of the next instruction is copied from the PC to the MAR. The address is sent via the address bus to main memory.
MBR ←[Memory]MAR; PC ←[PC]+1
	2.The instructions held at that address is returned along the *data bus* to the MBR. Simultaneously, the content of the PC is incremented so that it holds the address of the next instruction.
CIR ← [MBR]
	3.The contents of the MBR are copied to the CIR.
## Decode - determine wahta to do
Decode instructions in CIR → split into opcode and operand
	4.The instructions held in the CIR is decoded. The instruction is split into opcode and operand and the opcode is used to determine the type of instruction and what hardware to use to execute it.  Additional data is fetched if necessary, and passed to the registers.
## Execute
[CIR] executes
	5.The instruction is executed, using the ALU if necessary, and results are stored in the accumulator (general purpose register)