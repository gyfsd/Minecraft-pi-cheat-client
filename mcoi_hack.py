import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import subprocess
mc = minecraft.Minecraft.create()
def blockfly(break0):
 while True:
  pos = mc.player.getTilePos()
  mc.setBlock(pos.x,pos.y-1,pos.z,block.DIAMOND_BLOCK.id)
  if break0 == 1:
   mc.setBlocks(pos.x - 2,pos.y,pos.z - 2,pos.x +2,pos.y + 1,pos.z + 2,block.AIR.id)
  mc.setBlock(pos.x - 1,pos.y - 1,pos.z - 1,block.AIR.id)
  mc.setBlock(pos.x + 1,pos.y - 1,pos.z - 1,block.AIR.id)
  mc.setBlock(pos.x - 1,pos.y - 1,pos.z + 1,block.AIR.id)
  mc.setBlock(pos.x + 1,pos.y - 1,pos.z + 1,block.AIR.id)
  mc.setBlock(pos.x - 1,pos.y - 1,pos.z,block.AIR.id)
  mc.setBlock(pos.x,pos.y - 1,pos.z - 1,block.AIR.id)
  mc.setBlock(pos.x,pos.y - 1,pos.z + 1,block.AIR.id)
  mc.setBlock(pos.x + 1,pos.y - 1,pos.z,block.AIR.id)
  mc.setBlock(pos.x,pos.y - 2,pos.z,block.AIR.id)
  mc.setBlock(pos.x - 1,pos.y - 2,pos.z,block.AIR.id)
  mc.setBlock(pos.x,pos.y - 2,pos.z - 1,block.AIR.id)
  mc.setBlock(pos.x,pos.y - 2,pos.z + 1,block.AIR.id)
  mc.setBlock(pos.x + 1,pos.y - 2,pos.z,block.AIR.id)
def antifall():
  pos = mc.player.getTilePos()
  falllblock = mc.getBlock(pos.x,pos.y - 10,pos.z,block.AIR.id)
  if fallblock == False:
   mc.setBlock(pos.x,pos.y - 10,pos.z,block.WATER_FLOWING.id)
def run(list0):
 subprocess.run(list0)
def antiwater():
 while True:
  pos = mc.player.getTilePos()
  block0 = mc.getBlock(pos.x,pos.y,pos.z,block.WATER_FLOWING.id)
  block1 = mc.getBlock(pos.x,pos.y,pos.z,block.WATER.id)
  block2 = mc.getBlock(pos.x,pos.y,pos.z,block.WATER_STATIONARY.id)
  block3 = mc.getBlock(pos.x,pos.y,pos.z,block.LAVA_STATIONARY.id)
  block4 = mc.getBlock(pos.x,pos.y,pos.z,block.LAVA_FLOWING.id)
  block5 = mc.getBlock(pos.x,pos.y,pos.z,block.LAVA.id)
  if block0 or block1 or block2 or block3 or block4 or block5 == True:
   mc.setBlocks(pos.x - 4,pos.y + 1,pos.z - 4,pos.x + 4,pos.y + 1,pos.z + 4,block.AIR.id)
def spam(messege,delay):
 while True:
  mc.postToChat(messege)
  time.sleep(int(delay))
while True:
 print("/****************|")
 print("|1 flyhack       |")
 print("|2 teleport      |")
 print("|3 spam          |")
 print("|4 antiwater/lava|")
 print("\________(test)__/")
 input0 = input("please input>")
 print(input0)
 if input0 == "1":
  blockfly(int(input("break?(1 or 0)")))
 if input0 == "2":
  x = input("x:")
  y = input("y:")
  z = input("z:")
  mc.player.setPos(x,y,z)
 if input0 == '3':
  spam(input("enter spam messege >"),input('input delay(seconds)'))
 if input0 == '4':
  antiwater()
 if input0 == '999':
  run(['git','clone','https://github.com/gyfsd/Minecraft-pi-cheat-client.git'])
  run(['python3', '-m', 'py_compile', './Minecraft-pi-cheat-client/mcoi_hack.py'])
  run(['cp','./Minecraft-pi-cheat-client/__pycache__/*','.'])
  run(['rm','mcoi_hack.py','mcoi_hack.cpython-39.pyc'])
 print("done")
