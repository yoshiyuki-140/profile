TARGET = ./bin/Main
TARGET_OBJECT = ./bin/LifeGame.class

Main.class:Main.java LifeGame.class
	javac.exe -encoding utf-8 $<
LifeGame.class:gameRule.java
	javac.exe -encoding utf-8 $<
run:
	java.exe Main
cmpRun:
	make && make run
clear:
	rm Main.class LifeGame.class