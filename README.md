# This is my invastigation into ACZ's memory!

## Controller communication
While reading about PS2 controller interface (https://hackaday.io/project/170365-blueretro/log/186471-playstation-playstation-2-spi-interface), I learned that rumble state is determined by a byte.


Maybe, some of the values that increase when I stall the aircraft are related to this controller output? Maybe other values as well.
I have to check this. Could be a way off sniffing player input!

source: (https://hackaday.io/project/170365-blueretro/log/186471-playstation-playstation-2-spi-interface#:~:text=Dual%20Analog%20%26%20DualShock%201,is%20right%20and%20down.)

    Dual Analog & DualShock 1/2 (SCPH-1180, SCPH-1200, SCPH-10010)  (In Analog mode)
                    ┌Rumble(Could be map to any byte via CMD 0x4D,
                    │       but typically:
                ┌───┴──┐    1st byte: Right small motor (On-0xFF/Off-0x00)
    TX: 014200000000000000    2nd byte: Left big motor (Variable/Off-0x00))
    RX: FF735AFFFF80808080
        ├┘  └┬─┘└──┬───┘
        ID Buttons └Axes(RX RY LX LY)
    Axis ideal neutral position is 0x80, 0x00 is left & up and 0xFF is right and down.




    Idea for disassembly: Since I know the memory addresses to change to disable interlacing, I could use ghidra to analyse them and find something. I should also find in what .dat file they are stored so I can find their location and use ghidra.


## Gamestate/Freelook byte - ACZ Multiplayer mod
At the address 0x20765231, a byte toogles gamestgates as follows:
    0x00 = debug mode,
    0x02 = normal gameplay,
    0xFF during menu, briefing and aircraft selection, changes to 0x00 at loading

As a way to detect changes in game state, mainly when the game has started or is on the menus, I should:

1. Add a breakpoint to this address and records the intructions that alter it.
1. From then, work my way back into memory and assembly, so to pass this data to my future multiplayer mod. It will help detect changes in game state and determine if a match can start.
1. If I could know which mission and stage is currently being played, it would be even better, as a automatic matchmake can be done.
