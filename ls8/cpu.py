"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
POP = 0b01000110
PUSH = 0b01000101
SP = 7


class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.halted = False
        self.pc = 0
        self.reg[SP] = 0xF4

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        if len(sys.argv) != 2:
            print("usage: ls8.py filename")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    line = line.strip()
                    if line == '' or line[0] == "#":
                        continue
                    try:
                        str_value = line.split("#")[0]
                        value = int(str_value, 2)
                    except ValueError:
                        print(f"Invalid number: {str_value}")
                        sys.exit(1)
                    self.ram[address] = value
                    address += 1
        except FileNotFoundError:
            print(f"File not found: {sys.argv[1]}")
            sys.exit(2)

        # program = [

        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(
            f"TRACE: %02X | %02X %02X %02X |" % (
                self.pc,
                #self.fl,
                #self.ie,
                self.ram_read(self.pc),
                self.ram_read(self.pc + 1),
                self.ram_read(self.pc + 2)),
            end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while not self.halted:
            instruction = self.ram[self.pc]
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if instruction == HLT:
                self.halted = True
                self.pc = 0

            elif instruction == LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3

            elif instruction == PRN:
                print(self.reg[operand_a])
                self.pc += 2

            elif instruction == MUL:
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3

            elif instruction == POP:
                reg_num = self.ram_read(self.pc + 1)
                top_of_stack_address = self.reg[
                    SP]  # Get the top of stack addr
                value = self.ram_read(
                    top_of_stack_address
                )  # Get the value at the top of the stack

                self.reg[reg_num] = value  # Store the value in the register
                self.reg[SP] += 1  # Increment the SP
                self.pc += 2  # Increment program counter to the next instruction

            elif instruction == PUSH:
                self.reg[SP] -= 1  # Decrement Stack Pointer(SP)
                reg_num = self.ram_read(self.pc + 1)  # Get the reg num to push
                value = self.reg[reg_num]  # Get the value to push
                top_of_stack_address = self.reg[
                    SP]  # Copy the value to the SP address
                self.ram[top_of_stack_address] = value
                self.pc += 2

            # else:
            #     print(f"unknown instruction {instruction} at address {pc}")
            #     sys.exit(1)
