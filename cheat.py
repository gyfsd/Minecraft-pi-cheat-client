#import
import mcpi.minecraft as minecraft
import time
import os
import mcpi.block as block
#import keyboard
#import mouse
#intilization
mc = minecraft.Minecraft.create()
entityIds = mc.getPlayerEntityIds()
mc.camera.setNormal(entityIds[0])
#defs
def freecam():
    pos = mc.player.getPos()
    mc.camera.setFixed()
    mc.player.setPos(pos.x,pos.y + 1000,pos.z)
    while True:
        pos = mc.player.getPos()
        mc.camera.setPos(pos.x,pos.y - 1000,pos.z)
def setblocks(x,y,z,x1,y1,z1,block_):
    mc.setBlocks(x,y,z,x1,y1,z1,block_)
def tp(x,y,z):
    mc.player.setPos(x,y,z)
def playertp(num):
    entityIds = mc.getPlayerEntityIds()
    mc.setPos(mc.entity.getPos(entityIds[num]))
def playerkill(num):
    entityIds = mc.getPlayerEntityIds()
    mc.camera.setFixed()
    while True:
        mc.camera.setPos(mc.entity.getPos(entityIds[num]))
#gui
while True:
 print(''' /```````````\
| 1.freecam   |
| 2.playerkill|
| 3.tp        |
| 4.playertp  |
| 5.setblocks |
| 6.creativeon|
| 7.crativeoff|
|             |
 \___________/''')
 input0 = int(input('input a number > '))
 if input0 = 1:
     freecam()
 if input0 = 2:
     playerkill(input('num > '))
 if input0 = 3:
     tp(input('x > '),input('y > '),input('z > '))
 if input0 = 4:
     playertp(input('player > '))
 if input0 = 5:
     setblocks(input('x > '),input('y > '),input('z > '),input('x1 > '),input('y1 > '),input('z1 > '),input('block > '))
 if input0 = 7:
     os.system('sudo rm /opt/minecraft-pi-reborn-client/mods/cmcp.so')
 if input0 = 6:
     os.system('sudo cp ~/cmcp.so /opt/minecraft-pi-reborn-client/mods')